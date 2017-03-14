def timer_modifier(time):
	minutes = int(time // 60)
	seconds_rem = int(time % 60)
	if seconds_rem < 10:
		return (str(minutes) + ':0' + str(seconds_rem))
	else:
		return  (str(minutes) + ':' + str(seconds_rem))


def time_in_sec(time):
        total_time = time.split(':')
        timeinsec = int(total_time[0])*60*60 + int(total_time[1])*60 + int(total_time[2])
        return timeinsec

