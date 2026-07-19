# AI-Robotic-arm




<img width="4032" height="3024" alt="20260719_104822" src="https://github.com/user-attachments/assets/f624336c-6c75-4c1d-a3e7-855f1fdfda69" />

## About the project

its a AI robotic arm controlled by a local ollama ai model(i call him ezekiel)
made from easily accesible materials (i made it from lego but it can be easily recreated with cardboard/or the stl file i included).
You can talk to the AI through a PySide6 app i made,i personally prefer typing my prompts but you can very easily make it voice controlled.
Now here are the steps to make it:
(also disclaimer i used ai to learn some of the libraries like PySide6 and ollama but the code is not copy and paste from AI i worked really hard on it)



## Features
* Moving around in 4 directions (up,down,left,right)
* Capable of having a conversation
* Picking up and putting down magnetic stuff
* AI running fully locally
  





## What you will need:
      1. 3 servomotors(model depends on what you are making the arm from)
      2. A microcontroller(esp,arduino,raspberry_pico)
      3. A oled display(optional but makes it feel alive)
      ## 4. A reliable source of 5V !!! very important.
      5. Some wires and a breadboard.



## Setting up the app/downloading all the neccesary libraries(there is a lot)


Download each library, i will list them all below, and just a heads up you will need to first create a virtual environment

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
Now that you activated the virtual environment you should see (venv) in your terminal
Now to installing the libraries 

* Install PySide6
```sh
pip3 install PySide6
```
* Install Dotenv
```sh
pip3 install python-dotenv
```

* Then just install all these in the format "pip3 install library name"
```
import os,sys,time,datetime,serial,pyttsx3,ollama,pathlib
```


Now that you got all the libraries you need to choose a ollama ai model to use for the project.

## Choosing a AI model.

* For a light AI model for coding and talking use -> qwen2.5-coder:3b

* For conversation use -> Llama 3.2 3B

* For creativity -> Gemma 2 (this one is a bit heavier though so keep that in mind)


There are many other models but if you are going to run the AI on your personal computer where you also do other things
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


## Making the arm
The arm consists of a square base, a shoulder and head.I included 2 stl files one for the body one for the head you can either print
those out or easily recreate it from lego/cardboard. Although you shouold really watch your servo models since a cardboard arm will need lighter servos then a lego one obviously.
I will have a youtube video (maybe its even out by now) where i show closer look of the arm.


## Now to set up the microcontroller
The last step is to set up your microcontroller of choice (i am using a esp32 but it works with all).
Just load the reciever code on to your microcontroller and keep in mind if you are using something else then a esp
you will have to tweak a few stuff (for example baud rate is 9600 for arduino not 115200)

* Here is how the components should be connected to the esp32

<img width="772" height="506" alt="Screenshot_2026-07-19_12-44-58" src="https://github.com/user-attachments/assets/fda8c9f6-24d1-4c60-a686-bcca1cfa458e" />


(keep in mind the servos should be hooked up to the external power supply, in the way that the red cable goes to
5v and the grounds go to ground plus add one ground wire from the esp to the ground so the curcuit is closed)


And congrats the arm should now be working!!!


## Here are some common issues though:

      * if you have trouble installing libraries make sure you have python3 installed,and try replacing pip with pip3
      * when activating .venv if you are on a arch based distro you will have to use .venv/bin/activate.fish
      * triple check the wiring trust me
      * make sure you have the correct AI model in the code 
      * If you have trouble recieving data through serial try changing the baudrate
      * if you are using anythign else then esp32 tweak the code(for example remove the library esp32servo from the code or change the baudrate as i said earlier)
      * also check if you have the correct port very important (you can check what port your using by going to the arduino ide and finding your microcontroller)
      * if the arm is wobbling try playing around with the part lenghts/servo models.



Thats it thank you for reading i hope you like the project and if you have any issues feel free to reach out!!
I am more than happy to help!.


  
          
        



