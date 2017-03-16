#!/usr/bin/env python
from __future__ import print_function
import signal, sys, time

from task import Task
from databases import Storage
from task import seconds_to_time

task = None
print ("""

                                                    ,,
`7MM\"\"\"Mq.                                        `7MM
  MM   `MM.                                         MM
  MM   ,M9 ,pW\"Wq.`7MMpMMMb.pMMMb.  ,pW\"Wq.    ,M\"\"bMM  ,pW\"Wq.`7Mb,od8 ,pW\"Wq.
  MMmmdM9 6W'   `Wb MM    MM    MM 6W'   `Wb ,AP    MM 6W'   `Wb MM' "'6W'   `Wb
  MM      8M     M8 MM    MM    MM 8M     M8 8MI    MM 8M     M8 MM    8M     M8
  MM      YA.   ,A9 MM    MM    MM YA.   ,A9 `Mb    MM YA.   ,A9 MM    YA.   ,A9
.JMML.     `Ybmd9'.JMML  JMML  JMML.`Ybmd9'   `Wbmd"MML.`Ybmd9'.JMML.   `Ybmd9'
                                         ,,
                                  mm     db
                                  MM
                                mmMMmm `7MM  `7MMpMMMb.pMMMb.  .gP"Ya `7Mb,od8
                                  MM     MM    MM    MM    MM ,M'   Yb  MM' \"'
                                  MM     MM    MM    MM    MM 8M""""""  MM
                                  MM     MM    MM    MM    MM YM.    ,  MM
                                  `Mbmo.JMML..JMML  JMML  JMML.`Mbmmd'.JMML.

""")

def print_usage():
    print("""
    Usage:
        pomodoro start <task_title>
        pomodoro config time <duration>
        pomodoro config short_break <duration>
        pomodoro config long_break <duration>
        pomodoro config sound <state>
        pomodoro stop
        pomodoro list
        pomodoro interactive
    Options:
        -i, --interactive  Interactive Mode
    """)


def get_time(source):
    times = source.split(":")[::-1]
    seconds = 0
    current_multiplier = 1
    for time in times:
        seconds += float(time) * current_multiplier
        current_multiplier *= 60
    return int(seconds)


# signal number and current app frame for the keyboard interrupts
def stop_timer(signum, frame):
    if task is not None and task.status is not 'stopped':
        task.status = "stopped"
        time.sleep(1.5)
        print('\nStopped current task:' + task.name + '\n')
        sys.stdout.write('\r')
        sys.stdout.flush()
    else:
        sys.exit(0)


signal.signal(signal.SIGINT, stop_timer)


def commands():
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
                    task.duration = get_time(comands[2])
                elif comands[1] == 'cycle_time':
                    task.cycle_time = get_time(comands[2])
                elif comands[1] == 'short_break':
                    task.short_break = get_time(comands[2])
                elif comands[1] == 'long_break':
                    task.long_break = get_time(comands[2])
                elif comands[1] == 'sound':
                    task.alarm = comands[2]
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
            import tabulate

            db = Storage()
            headers = ["Name", "Duration", "Cycle Time", "Short Break", "Long Break", "Alarm", "Status"]
            data = []
            for task in db.get():
                row = [task.name, seconds_to_time(task.duration), seconds_to_time(task.cycle_time),
                       seconds_to_time(task.short_break), seconds_to_time(task.long_break), str(task.alarm),
                       task.status]
                data.append(row)
            print(tabulate.tabulate(data, headers))


def interactive():
    name = raw_input("Task name:")
    duration = raw_input("Task duration:")
    cycle = raw_input("Cycle time:")
    short_break = raw_input("Short break:")
    long_break = raw_input("Long break:")
    alarm = raw_input("Alarm state:")
    task = Task(name, get_time(duration), get_time(cycle), get_time(short_break), get_time(long_break), alarm)
    task.start()


if len(sys.argv) == 1:
    print_usage()
    commands()
else:
    if sys.argv[1] == '-i' or sys.argv[1] == '--interactive':
        interactive()