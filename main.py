






#importing all the neccesary libraries
from PySide6.QtWidgets import QApplication,QLabel,QTextEdit, QMainWindow, QWidget, QPushButton, QLineEdit, QVBoxLayout,QGridLayout,QScrollArea,QHBoxLayout
from PySide6.QtCore import QSize, Qt,QThread,Signal
from pathlib import Path
from dotenv import load_dotenv
import os,sys,time,datetime,serial,pyttsx3,ollama






#this is the function where the ai reply gets proccesed
class CookThread(QThread):
    zvoncek_signal = Signal(str,str)

    def __init__(self, order, base_angle, shoulder_angle, head_angle, chat_history, reply, speak):
        super().__init__()
        #order has my input 

        self.order = order
        print(self.order)
        self.base_angle = base_angle
        self.shoulder_angle = shoulder_angle
        self.head_angle = head_angle
        self.chat_history = chat_history
        self.reply = reply
        self.reply.setText("thinking...")
        self.speak = speak

    def run(self):

            ai_prompt = f"current servo positions are : base: {self.base_angle}, shoulder: {self.shoulder_angle}, head: {self.head_angle}. User prompt: {self.order}"
            
            
            #adding it to memory
            self.chat_history.append({"role": "user", "content": ai_prompt})
        
            try:
            
                self.response = ollama.chat(
                    model="qwen2.5-coder:3b",

                    messages=self.chat_history
                )

                self.full_response = self.response['message']['content']

                self.chat_history.append({"role": "assistant", "content": self.full_response})

                if "[" in self.full_response and "]" in self.full_response:
                    parts = self.full_response.split("]",1)
                    self.angles_part = parts[0].replace("[", "").strip() 
                    self.jarvis_text = parts[1].strip()                
                
        #delete line 67 if you dont want to hear it speak
                print(self.full_response)
                print(self.angles_part)
                self.zvoncek_signal.emit(self.angles_part,self.jarvis_text)
                self.speak(self.jarvis_text)
                

            except Exception as e:
                print(f"Error at local communication: {e}")
                







class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        #here we make the UI 
        self.setWindowTitle("Control app")

        self.setFixedSize(600,600) #make the size of the window


        self.scroll = QScrollArea()

        self.central_container = QWidget()

        layout = QVBoxLayout()

        bottom_layout = QHBoxLayout()

        self.reply = QLabel("Ask anything...")
        self.reply.setWordWrap(True)
        

        self.input = QLineEdit()
        self.input.setPlaceholderText("Enter your text")
        self.input.setFixedSize(400,40)



        self.button = QPushButton("")
        self.button.setFixedSize(150,40)
        self.button_is_checked = True
        self.button.clicked.connect(self.the_button_was_clicked)



        self.central_container.setLayout(layout)
    
        
        layout.addWidget(self.reply,alignment=Qt.AlignTop)
        
        layout.addLayout(bottom_layout)

        bottom_layout.addWidget(self.input,alignment=Qt.AlignLeft)

        bottom_layout.addWidget(self.button,alignment=Qt.AlignLeft)

        self.scroll.setWidget(self.central_container)

        self.scroll.setWidgetResizable(True)

        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        
        self.setCentralWidget(self.scroll)
        


#END OF UI 
#the base servo values so the ai can keep track of them 
        self.base_angle = 90
        self.shoulder_angle = 90
        self.head_angle = 90
#system instructions you can change them but always make the ai send 3 servo values if you want
#control the arm
        self.system_instruction = (
        "you are an ai assistant, you help with math problems and stuff"
        "You control 3 servos which make a robotic arm, one for base one for shoulder one for head "
        "the user will give a prompt, reply with a list of 3 servo angles between 1 and 180 in the format [base,shoulder,head] on the first line and a natural language response on the second line. "
        "YOU ALWAYS REPLY WITH SERVO ANGLES EVEN IF IT ISNT RELEVANT,THEY DONT HAVE TO ALWAYS CHANGE THOUGH"
        "you reply in this format [servo_angles] [emotion] text"
        "Example: [90,120,45] . Servo values must be between 1 and 180. "
        "Default for every servo is 90. Reply naturally to the user's prompt."
        
        )
    #here is where the chat history gets stored (ai memory), it gets wiped each time you run the code
        self.chat_history = [
            {"role": "system", "content": self.system_instruction}
        ]


#setting up port
        self.serialcomm = None
        try:
            #change the port if you are using another one
            self.serialcomm = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
            time.sleep(2)  # Čas na stabilizáciu Arduina po resete
            print("Serial port open!.")
        except Exception as e:
            #basically you are running in simulation so the ai doesnt actually control anything
            #since the serialcommunication failed
            print(f"Error while opening the port: {e}.Running in simulation.")


#speak
        #initialize tts engine
        try:
            self.tts_engine = pyttsx3.init()
            print("voice should work")
        except Exception as e:
            print(f"Chyba pri inicializácii TTS: {e}")
            self.tts_engine = None
            
    def speak(self,text):
        try:
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
        except Exception as e:
            print(f"tts error: {e}")


    def send_data(self,angles_text):
        if self.serialcomm and self.serialcomm.is_open:
            try: 
                data_to_send = angles_text.strip() + "\n"
                
                self.serialcomm.write(data_to_send.encode("utf-8"))

                #self.speak(f"[HARDWARE] Sent to Arduino: {data_to_send.strip()}")
            except Exception as e:
                print(f"Problem sending hardware data: {e}")
            else:
                print(f"[SIMULATION] Hardware would receive: {angles_text.strip()}")


    def the_button_was_clicked(self):
        
        self.master_input = self.input.text()
        self.input.clear()
#sending the base angles anjd input to the qthread
        self.cook = CookThread(self.master_input,self.base_angle,self.shoulder_angle,self.head_angle,self.chat_history,self.reply,self.speak)

        
        self.cook.zvoncek_signal.connect(self.print_out)

        self.cook.start()

        


        
#printing out the reply/sending the servo values to the microcontroler
    def print_out(self,angles_part,jarvis_text):
        
        self.send_data(angles_part)

        self.reply.setText(jarvis_text)
        

        


#application handler 
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

