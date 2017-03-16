import time, sys


class Task: #class variables
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
            sys.stdout.write('\rLong break Left: ' + seconds_to_time(counter))
            sys.stdout.flush()
            time.sleep(1)
            counter -= 1

    def go_short_break(self):
        if self.alarm:
            play_sound()
        counter = self.short_break
        while counter > 0:
            sys.stdout.write('\rShort break Left: ' + seconds_to_time(counter))
            sys.stdout.flush()
            time.sleep(1)
            counter -= 1

    def start(self):
        self.status = 'running'
        self.time_left = self.duration
        counter = 0
        while self.status == 'running' and self.time_left > 0:
            time.sleep(1)
            self.time_left -= 1
            counter += 1
            sys.stdout.write('\rTime left: ' + seconds_to_time(self.time_left))
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


def seconds_to_time(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)


t = Task("Cleaning", 120, 10, 5, 10)


# t.start()


def play_sound():
    import os
    uri = "bell.mp3"
    os.system('cvlc ' + uri + ' vlc://quit > /dev/null 2>&1')