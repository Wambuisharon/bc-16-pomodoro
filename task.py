import time, sys, os


class Task:
    name = ''
    status = 'pending'
    cycle_time = 0
    duration = 0
    short_break = 0
    long_break = 0
    current_cycle = 0
    time_left = 0
    alarm = True
    day = ''

    def __init__(self, name, duration=6000, cycle_time=1500, short_break=360, long_break=600, day='', alarm=True):
        self.name = name
        self.cycle_time = cycle_time
        self.short_break = short_break
        self.long_break = long_break
        self.duration = duration
        self.alarm = alarm
        self.day = day

    def go_long_break(self):
        if self.alarm:
            play_sound()
        counter = self.long_break
        while counter > 0:
            sys.stdout.write("\033[2J\033[;H")
            sys.stdout.write(ascii_art('Long break Left: ' + seconds_to_time(counter)))
            sys.stdout.flush()
            time.sleep(1)
            counter -= 1

    def go_short_break(self):
        if self.alarm:
            play_sound()
        counter = self.short_break
        while counter > 0:
            sys.stdout.write("\033[2J\033[;H") #clear screen 
            sys.stdout.write(ascii_art('Short break Left: ' + seconds_to_time(counter))) #conver text
            sys.stdout.flush()
            time.sleep(1)
            counter -= 1

    def start(self):
        if isinstance(self.alarm, str):
            if self.alarm.lower() == 'on':
                self.alarm = True
            else:
                self.alarm = False
        else:
            self.alarm = bool(self.alarm)
        self.status = 'running'
        self.time_left = self.duration

        counter = 0 #cyle time
        while self.status == 'running' and self.time_left > 0:
            time.sleep(1)
            self.time_left -= 1
            counter += 1
            if self.status == 'running':
                sys.stdout.write("\033[2J\033[;H")
                sys.stdout.write(ascii_art('Time left: ' + seconds_to_time(self.time_left)))
                sys.stdout.flush()
            # checking for break
            if counter == self.cycle_time:
                self.current_cycle += 1
                if self.current_cycle % 4 == 0:
                    self.go_long_break()
                else:
                    self.go_short_break()
                # reset break counter
                counter = 0
                if self.alarm:
                    play_sound()

        if self.alarm:
            play_sound()


def seconds_to_time(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%d : %02d : %02d" % (h, m, s)


t = Task("Cleaning", 120, 10, 5, 10)


# t.start()


def play_sound():
    import os, threading
    class PlayThread(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)

        def run(self):
            uri = "bell.mp3"
            os.system('cvlc ' + uri + ' vlc://quit > /dev/null 2>&1')

    (PlayThread()).run()


def ascii_art(string):#format text ....set up figlet
    from colorama import init
    init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected
    from pyfiglet import figlet_format
    return figlet_format(string, font='georgia11')