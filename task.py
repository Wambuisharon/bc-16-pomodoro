class Task():
	status = 'pending'
	cycle_time = 0
	duration = 0
	short_break= 0
	long_break = 0
	


	def __init__(self,name,duration=6000, short_break=360,long_break=600,cycle_time=1500):	

		self.name=name
		self.cycle_time =cycle_time
		self.short_break=short_break
		self.long_break =long_break
		self.duration = duration

	def start(self):
		self.status = 'running'
		self.time_left = self.duration
		counter=0
          #task time
	  	while(self.status=='running' and self.time_left>0):
	   		time.sleep(1)
	    	self.time_left -=1
	    	counter += 1
	    	if (counter == self.cycle_time):
		 		self.current_cycle +=1
		 		if(self.current_cycle%4==0):
		 			#go long break
		 			pass
		 		else:
		 			#go short break
		 			pass
		 			#reset break counter
		 		counter = 0	