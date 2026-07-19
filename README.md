# AI-Robotic-arm




<img width="4032" height="3024" alt="20260719_104822" src="https://github.com/user-attachments/assets/f624336c-6c75-4c1d-a3e7-855f1fdfda69" />

#About the project

#its a AI robotic arm controlled by a local ollama ai model and
its made from easily accesible materials (i made it from lego but it can be easily recreated with cardboard/or the stl file i included).
You can talk to the AI through a PySide6 app i made,i personally prefer typing my prompts but you can very easily make it voice controlled.
Now here are the steps to make it:

## What you will need:
      1.  3 servomotors(model depends on what you are making the arm from)
      2. A microcontroller(esp,arduino,raspberry_pico)
      3. oled display(optional but makes it feel alive)
      ##4. A reliable source of 5V !!! very important.
      5.some wires and a breadboard.








## Setting up the app/downloading all the neccesary libraries(there is a lot)


Download each library, i will list them all below, and just a heads up you will need to first create a virtual enviremont

* setting up venv(if it doesnt work try python3 -m venv .venv)
  ```sh
  python -m venv .venv 
  ```
* then activate it
  ```sh
  .venv\Scripts\activate.bat
  ```
* If you are on linux use
  ```sh
  source .venv/bin/activate
  ```
#Now that you activated the virtual envirment you should see (venv) in your terminal
Now to installing the libraries 

* Install PySide6
```sh
pip3 install PySide6
```
*Install Dotenv
```sh
pip3 install python-dotenv
```

#Then just install all these in the format "pip3 install library name"
```
import os,sys,time,datetime,serial,pyttsx3,ollama,pathlib
```


#Now that you got all the libraries you need to choose a ollama ai model to use for the project.
Here are a few of my recommendations based on what you need the ai for.

For a light AI model for coding and talking use -> qwen2.5-coder:3b

For conversation use -> Llama 3.2 3B

For creativity -> Gemma 2 (this one is a bit heavier though so keep that in mind)

#There is many other models but if you are going to run the AI on your personal computer where you also do other sutff
i highly recommend not going over 3b parameters.

Next you need to download the model,follow these steps, i am using qwen2.5:3b for the example just switch that if you want a different model
1,pull the model(this is considering you already pip installed ollama of course)
```
ollama pull qwen2.5:3b
```
2.Try it out in terminal, ollama actually has the function that you can use the ai in the terminal just run
```
ollama run qwen2.5:3b
```
If everything works now you can just copy the Main.py to a coding ide and when you run it, the pyside6 app should show up,
try out the app and if everything is working we can move on


#Next step actually making the arm
The arm consists of a square base, a shoulder and head.I included 2 stl files one for the body one for the head you can either print
those out or easily recreate it from lego/cardboard. Although you shouold really watch your servo weights since a cardboard arm will need lighter servos then a lego one obviously.
I will have a youtube video (maybe its even out by now) where i show closer look of the arm.


#Now to set up the microcontroler
The last step is to set up your microcontroller of choice (i am using a esp32 but it works with all).
just load the reciever code on to your microcontroller and keep in mind if you are using something else then a esp
you will have to tweak a few stuff (for example baud rate is 9600 for arduino not 115200)



