import os
import sys
import time
from timer_modifier import time_in_sec, timer_modifier







class pomodoro_timer(object):

    def start_task(self):
        self.task_name()
        self.add_task_time()
        self.short_break_function()
        self.long_break_function()
        self.timer("00:00:06")
        self.cycle()


    def cycle(self):   

        cycle = 0


        while cycle <=3:
            self.timer(self.add_task_time)
            self.short_break_function(self.short_break)
            self.cycle +1
            self.long_break_function(self.long_break) 




        
    


    def timer(self, timer):
        tm = time_in_sec(timer)
        while tm:
            for items in range(tm, 0, -1):
                output = str(timer_modifier(items))
                sys.stdout.write("\r" + str(output))
                time.sleep(1)
                sys.stdout.flush()
                # os.system('clear')
                tm -= 1

    def add_task_time(self):
        #tt = time.split(':') #spliting the time into hours:minutes:seconds
        print 
      
        self.choice = raw_input("Press Enter for default or 1 to set your time:")
  
        if self.choice == "":
            self.choice = "00:25:00"
            print "DEFAULT TIME : %s" % self.choice
            self.choice = self.choice.split(':')
            for items in [0, 1, 2]: #Checking if the input follows the require input format'''
                self.choice[items] = int(self.choice[items])
            return self.choice
        elif self.choice=="1":
            self.tt = raw_input("set time ....use {hh:mm:ss}format")
            self.tt = self.tt.split(':')
            if len(self.tt) != 3:
                print "INVALID INPUT! use the correct format"
                return self.tt
            else:
                for items in [0, 1, 2]:
                    self.tt[items] = int(self.tt[items])
                    return self.tt
        else:
            print "INVALID ENTRY"                

     #Add the short break function                   

    def short_break_function(self):
        print "Take a short break"
      
        short_break = raw_input("Enter the first short_break ")
        if short_break == '':
            short_break = "00:05:00"
            print "DEFAULT SHORT BREAK: %s" % short_break
            short_break = short_break.split(':')

            for items in [0, 1, 2]:  '''Checking if the input is valid'''
            short_break[items] = int(short_break[items])

            return short_break

        else:
            short_break = short_break.split(':')
            if len(short_break) != 3:
                print "INVALID INPUT!Enter the correct format"
              
                return short_break()
            else:
                for items in [0, 1, 2]:
                    short_break[items] = int(short_break[items])
                return short_break

    #Add the long break function

    def long_break_function(self):
        print "Take a long break"


        long_break = raw_input("Enter the long break duration")
        if long_break=='':
            long_break="00:15:00"
            print"DEFAULT LONG BREAK: %s" %long_break
            long_break=long_break.split(':')


            for items in [0,1,2]:
                long_break[items] =int(long_break[items])
            return long_break
        else:
            long_break=long_break.split(':')
            if len(long_break) !=3:
                print"INVALID INPUT!Enter the correct format" 
                return long_break()
            else:
                for items in [0,1,2]:
                     long_break[items]= int(long_break[items]) 
                return long_break              
                  

    def set_sound(self):
        print "Select {yes} or {no} or Press {ENTER} to select the default alarm"
       
        alarm_sound = raw_input('=> ')
        alarm_sound = alarm_sound.lower()

        if alarm_sound == '':
            alarm_sound = True
            print "Default alarm is selected"
            return alarm_sound
        else:
            if alarm_sound == 'on':
                alarm_sound = True
                return alarm_sound
            elif alarm_sound == 'off':
                alarm_sound = False
                return alarm_sound
            else:
                print "INVALID INPUT!You did not input any option"
              
                return set_sound()
            return alarm_sound



    def task_name(self):
        print "ENTER THE TASK NAME"
        task_name = raw_input("Enter the task name ")
        return task_name                




Test = pomodoro_timer()
'''Test.timer(6)'''
'''Test.add_task_time()'''
'''Test.short_break_function()'''
'''Test.long_break_function()'''
'''Test.task_name()'''
Test.start_task()











