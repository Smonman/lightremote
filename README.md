# lightremote
A simple remote control that operates through changes of brightness.

## What do I need?
* a webcam

## What does it do?
Simply put, this program performes a left click on a significant change in brightness recorded by a webcam. But when would one need that? A simple scenario would be the following: you are watching watching your favorite show or maybe a diashow of the latest holiday pictures on a tv connected to your computer. Now your tv remote suddenly is not capable of pausing what you are watching. This is exactly where this tool comes in handy. Recording the brigthness of the environment, you can now simply pause what you are watching by turning on your living room lights.

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

## Changelog

### 1.1.0
Added the feature to select a specific camera via the cameras index.

### 1.0.0
first version
