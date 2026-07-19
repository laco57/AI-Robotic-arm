





#include <ESP32Servo.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>


#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET    -1
#define SCREEN_ADDRESS 0x3C 

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

const unsigned int MAX_MESSAGE_LENGTH = 16; 
//servos defined
Servo myServo1;
Servo myServo2;
Servo myServo3;

// Eye parameters
int eye_height = 36;
int eye_width = 32;
int corner_radius = 10;
int space_between = 14;

int left_x = 30;
int cent_y = 32;
int right_x = left_x + eye_width + space_between;

//defined pins
const int servo_podstava_pin = 13;
const int servo_naklanacka1_pin = 12;
const int servo_naklanacka2_pin = 14;


void drawEyes() {
  display.clearDisplay();
  // Left Eye
  display.fillRoundRect(left_x - eye_width / 2, cent_y - eye_height / 2, eye_width, eye_height, corner_radius, SSD1306_WHITE);
  // Right Eye
  display.fillRoundRect(right_x - eye_width / 2, cent_y - eye_height / 2, eye_width, eye_height, corner_radius, SSD1306_WHITE);
  display.display();
}

void blink() {
  // Close eyes fast
  for (int h = eye_height; h > 2; h -= 8) {
    display.clearDisplay();
    display.fillRoundRect(left_x - eye_width / 2, cent_y - h / 2, eye_width, h, corner_radius, SSD1306_WHITE);
    display.fillRoundRect(right_x - eye_width / 2, cent_y - h / 2, eye_width, h, corner_radius, SSD1306_WHITE);
    display.display();
    delay(5);
  }

  for (int h = 2; h <= eye_height; h += 8) {
    display.clearDisplay();
    display.fillRoundRect(left_x - eye_width / 2, cent_y - h / 2, eye_width, h, corner_radius, SSD1306_WHITE);
    display.fillRoundRect(right_x - eye_width / 2, cent_y - h / 2, eye_width, h, corner_radius, SSD1306_WHITE);
    display.display();
    delay(5);
  }
}

void lookLeft() {
  left_x = 24;
  right_x = left_x + eye_width + space_between;
  drawEyes();
}

void lookRight() {
    left_x = 36; 
    right_x = left_x + eye_width + space_between;
    drawEyes();
  }

void centerEyes() {
  left_x = 30;
  right_x = left_x + eye_width + space_between;
  drawEyes();
}

void setup() {
  //start serial
  Serial.begin(115200); 
  if(!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println(F("SSD1306 allocation failed"));
    for(;;);
  }
  display.clearDisplay();
  drawEyes();

//attach servos to pins
  myServo1.attach(servo_podstava_pin);

  myServo2.attach(servo_naklanacka1_pin);

  myServo3.attach(servo_naklanacka2_pin);
}

void loop() {
  
    delay(2500);
    blink();
    delay(1500);
    lookLeft();
    delay(1000);
    lookRight();
    delay(1000);
    centerEyes();
    blink();
  if (Serial.available() > 0) {
    
    // Načítame čísla
    int base_angle     = Serial.parseInt(); 
    int shoulder_angle = Serial.parseInt(); 
    int head_angle     = Serial.parseInt(); 


    if (base_angle != 0 || shoulder_angle != 0 || head_angle != 0) {
      
      myServo1.write(base_angle);
      myServo2.write(shoulder_angle);
      myServo3.write(head_angle);
      
      printDebug(base_angle, shoulder_angle, head_angle);
    
    while (Serial.available() > 0) {
      Serial.read(); 
      }
    }
  }
}

void printDebug(int b, int s, int h) {
  Serial.print("Serva nastavene na: ");
  Serial.print(b); Serial.print(", ");
  Serial.print(s); Serial.print(", ");
  Serial.println(h);
}