from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC # timezone
import csv
import io
import sys



file1 = open( r'c:/pythontests/events.csv' , 'w')
g = open(r"C:\Users\andre\Downloads\EventsCalendar (1).ics",'rb')
gcal = Calendar.from_ical(g.read())
for component in gcal.walk():
	if component.name =="VEVENT":
		try:
			summary = component.get('summary')
			location = component.get('location')
			description = component.get('description').splitlines()
			description = description[-5:]
			description = " ".join(description)
			print (description)
			summary = summary + '|' + location + '|' + description + "\n"
			test = "test test test\n"
			file1.write(summary)
		except:
			print ("That one didn't work")
			print("Unexpected error:", sys.exc_info())


    
g.close()