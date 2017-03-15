class Task():
	status = 'pending'
	cycle_time = 0
	duration = 0
	short_break= 0
	long_break = 0
	alarm = True
	


	def __init__(self,name,duration=6000, cycle_time=1500, short_break=360,long_break=600,alarm=True):	

		self.name=name
		self.cycle_time =cycle_time
		self.short_break=short_break
		self.long_break =long_break
		self.duration = duration

	def go_long_break(self):
		counter = self.long_break
		while counter > 0:
			sys.stdout.write('\rLONG BREAK:' + seconds_to_time(self.time_left))
			sys.stdout.flush()
			time.sleep(1)
			counter -=1	


	def go_short_break(self):
		counter = self.short_break
		while counter > 0:
			sys.stdout.write('\rSHORT BREAK:' + seconds_to_time(self.time_left))
			sys.stdout.flush()
			time.sleep(1)
			counter -=1	

	def start(self):
		self.status = 'running'
		self.time_left = self.duration
		counter=0
          #task time
	  	while(self.status=='running' and self.time_left>0):
	   		time.sleep(1)
	    	self.time_left -=1
	    	counter += 1
	    	sys.stdout.write('\rTIME LEFT:' + seconds_to_time(self.time_left))
	    	sys.stdout.flush()
	    	if (counter == self.cycle_time):
		 		self.current_cycle +=1
		 		if(self.current_cycle%4==0):
		 			#go long break
		 			self.go_long_break()
		 			
		 		else:
		 			#go short break
		 			self.go_short_break()
		 		
		 			#reset break counter
		 		counter = 0	
def seconds_to_time(seconds):
	m, s =divmod(seconds, 60)	
	h, s =divmod(m, 60)	
	return "%d:%02d:%02d" %(h, m, s)	 

def play_sound():
    import os
    uri ="bell.mp3"
    os.system('cvlc ' + uri + ' vlc://quit > /dev/null 2>&1')

