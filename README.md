# bc-16-pomodoro
### pomodoro timer
It is a console application that break down work time into sessions separated by short/long break


### How to install
clone repo:
    https://github.com/Wambuisharon/bc-16-pomodoro.git


Create virtual environment and activate it 

First we need to install few dependencies for the project in the virtual env
  1. pyfiglet
  2. colorama
 
    
    
Navigate to the bc-16-pomodoro directory:

 $cd bc-16-pomodoro 

   
### Running instructions
 Run python pomodoro.py to launch the app

A welcome screen as shown below will be displayed

    pomodoro start <task_title>
    pomodoro config_time <duration_in_seconds>
    pomodoro config_short_break <duration_in_seconds>
    pomodoro config_long_break <duration_in_seconds>
    pomodoro config_sound <state>
    pomodoro stop
    pomodoro list
    pomodoro reset 
    pomodoro (-i | --interactive)
    pomodoro (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
### Commands descriptions
start <task_title> - Allows the user to start a task and sets the timer to it's default time i.e Sets the duration to 25 minutes, short break 5 minutes and long break to 15 minutes.

config_time <duration_in_seconds>, config_short_break <duration_in_seconds>, <config_long_break <duration_in_seconds> - Allows the user to specify his/her duration,long break and short break.

<config_sound> - Allows the user to turn off the sound

<config_stop> - Allows the user to stop the timer

<config_reset> - Allows the user to reset the timer back to its default.
   
