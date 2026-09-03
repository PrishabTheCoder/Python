#part 1 user input
city = input("enter your city name:")
temp = float(input("enter today's temperature in C: "))

#part 2 If statement
if temp > 35: 
   print("WARNING it is very hot today")

#part 3 if else
if temp > 25:
   print("great day to go outside")
else:
   print("grab a jacket before going out")   

#part 4 if elif else
if temp > 35: 
   print ("weather: very hot")
elif temp > 25:
    print("weather: warm and sunny")   
elif temp > 15:
   print("weather: cool and breezy")    
else :
   print("weather: Very cold")

#part 5 - datetime module
import datetime
import calendar

now = datetime.datetime.now()
print ("city", city)
print("time now", now)

print (calendar.calendar(now.year))