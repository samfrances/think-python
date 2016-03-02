import time, math
t = math.trunc(time.time())

minutes, seconds = t // 60, t % 60
hours, minutes = minutes // 60, minutes % 60
days, hours = hours // 24, hours % 24

print("{} days, {} hours, {} minutes, {} seconds".format(days,
                                                         hours,
                                                         minutes,
                                                         seconds))
