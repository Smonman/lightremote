# lightremote
A simple remote control that operates through changes of brightness.

## What do I need?
* a webcam

## What does it do?
Simply put, this program performes a left click on a significant change in brightness recorded by a webcam. But when would one need that? A simple scenario would be the following: you are watching watching your favorite show or maybe a diashow of the latest holiday pictures on a tv connected to your computer. Now your tv remote suddenly is not capable of pausing what you are watching. This is exactly where this tool comes in handy. Recording the brigthness of the environment, you can now simply pause what you are watching by turning on your living room lights.

__TL;DR__
Simulate a leftclick by turning your room lights on or off.

## Tutorial
Start this program, start your stream, initially set to pause and leave the cursor where clicking would result in a play action. Now simply lay back and turn off the lights of the room.

Notice that it might be possible to adjust different values to make this tool work as expected in a different environment.

### How to start the program

#### Without an installation
Go to the directory where `lightremote.py` is stored: 
```
python lightremote.py
```

#### With an installation
You can just call `lightremote` from any directory
```
lightremote
```

## Installation
```
python setup.py install
```
or go to the downloaded directory and type
```
pip install .
```

## Deinstallation
To uninstall `lightremote` just type
```
pip uninstall lightremote
```

## FAQ

 ### Command not found
Check if you installed `lightremote` using `pip`. Type
```
pip list
```
to list every installed package. If `lightremote` is in this list it is indeed installed.

On Windows you can search for this quicker with these commands:
```
pip list | findstr lightremote
```
When no output is produced, it means `lightremote` is not installed.

Try installing `lightremote` again, and if that does not help, update your `pip` and Python version.

---

### "An error occurred while trying to take a picture"
This error occurs when no picture could be taken by the camera. By default the camera with the index 0 is used to grab a frame, but this might not be the correct camera. Use the `-i` flag to change the index of the camera to use. Note, it might be possible that you have virtual cameras from other software installed e.g. from [OBS](https://obsproject.com/de).

---

### The brightness values do not reflect real conditions
This might be because the wrong camera is selected to be used. You can use the `-i` flag to change the index of the camera to use. As written above, note, that you might have virtual cameras installed from other programms e.g. [OBS](https://obsproject.com/de).

---

### When turning off the lights the multiple clicks occure
Try increasing the _cycle threshold_ parameter via the `-c` flag.

---

### I can't see anything in the console, just the cursor blinking
Try pressing <kbd>⏎ Enter</kbd> inside of the console.

---

### What does `^C` mean?

<kbd>⌃ Control</kbd> + <kbd>C</kbd>

---

## Changelog

### 1.1.0
Added the feature to select a specific camera via the cameras index.

### 1.0.0
first version
