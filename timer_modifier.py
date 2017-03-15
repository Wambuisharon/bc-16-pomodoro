import sys
def timer_modifier(input_time):
	minutes = int(input_time // 60)
	seconds_rem = int(input_time % 60)
	if seconds_rem < 10:
		return (str(minutes) + ':0' + str(seconds_rem))
	else:
		return  (str(minutes) + ':' + str(seconds_rem))


def time_in_sec(input_time):
        total_time = str(input_time).split(':')
        if len(total_time) >2:
        	seconds = int(total_time[2]);
        else:
        	seconds = 0;
        print int(total_time[0])*60*60
        print int(total_time[1]) * 60
       
        timeinsec = int(total_time[0])*60*60 + int(total_time[1]) * 60 + seconds
        return timeinsec
