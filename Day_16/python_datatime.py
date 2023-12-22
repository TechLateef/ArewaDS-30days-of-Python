from datetime import datetime, date

now = datetime.now()

print("day: ", now.today)
print("Month: ", now.month)
print("Year: ", now.year)
print("Hour: ", now.hour)
print("Minute: ", now.minute)
print("TimeStampt: ", now.timestamp())

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")

timestamp_format = "%m/%d/%Y, %H:%M:%S"

timestamp = now.strftime(timestamp_format)

print("timeStamp in %m/%d/%Y, %H:%M:%S format: ", timestamp)

# Today is 5 December, 2019. Change this time string to time

str_time = "5 December, 2019"

str__time = datetime.strptime(str_time, "%d %B, %Y")

print("Time: ", str__time)
# Calculate the time difference between now and new year.

today = date(year=now.year, month=now.month, day=now.day)
new_year = date(year=2024, month=1, day=1)

time_left_for_newyear = new_year - today
print('Time left for new year: ', time_left_for_newyear)


# Calculate the time difference between 1 January 1970 and now.
past_year = date(year = 1970, month=1, day= 1)

time_difference = today - past_year

print("time difference between 1 January 1970 and now: ", time_difference)
