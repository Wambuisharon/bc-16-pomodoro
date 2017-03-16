#!/usr/bin/env python
from __future__ import print_function
import signal, sys, time

from task import Task
from databases import Storage
from task import seconds_to_time

task = None
print("Pomodoro intro here!")

# signal number and current app frame for the keyboard interrupts
def stop_timer(signum, frame):
    if task is not None and task.status is not 'stopped':
        print('Stopping current task:' + task.name + '')
        task.status = "stopped"
        time.sleep(0.5)
        sys.stdout.write('\r                                    ')
        sys.stdout.flush()
    else:
        sys.exit(0)


signal.signal(signal.SIGINT, stop_timer)

while (True):
    comand = raw_input("pomodoro: ")
    comands = comand.split(" ")
    if comands[0] == 'start':
        task = Task(comands[1])
        task.status = 'pending'
    elif comands[0] == 'config':
        if task is None:
            print("Start a task first")
        else:
            if comands[1] == 'time':
                task.duration = 60 * int(comands[2])
            elif comands[1] == 'cycle_time':
                task.cycle_time = 60 * int(comands[2])
            elif comands[1] == 'short_break':
                task.short_break = 60 * int(comands[2])
            elif comands[1] == 'long_break':
                task.long_break = 60 * int(comands[2])
            elif comands[1] == 'sound':
                task.alarm = bool(comands[2])
            else:
                print("Invalid command")
    elif comands[0] == 'run':
        if task is None:
            print("Start a task first")
        else:
            task.status = 'running'
            db = Storage()
            db.save(task)
            db.close()
            task.start()
    elif comands[0] == 'list':
        db = Storage()
        for task in db.get():
            print("Name: %s, Duration:  %s,  Cycle Time: %s, Short Break %s, Long Break %s, Alarm %s, Status %s" % (
                task.name, seconds_to_time(task.duration), seconds_to_time(task.cycle_time),
                seconds_to_time(task.short_break), seconds_to_time(task.long_break), str(task.alarm), task.status))