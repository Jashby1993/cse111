#improvements: instead of asking for width, aspect_ratio, and diameter seperately, user inputs what they see right on the tire, the full code, and the program extrapolates the data automatically.
#Also, after entering the info, but before displaying volume, will ask if user is looking to buy tires. If yes, a phone number is requested, and is added to the information printed in text file. Otherwise, nothing happens.
import math
from datetime import datetime

tire_size = input("What is the tire size? Please use input format: xxx/xxRxx  ")
sale_possibility = input("Are you looking to buy tires of this size? Y or N: ").upper()

#separating the parts
parts = tire_size.split('/')

after_slash = parts[1]

after_r_parts = after_slash.split('R')

before_r = after_r_parts[0]

#converting the string to integers and changing variable names.
width = int(parts[0])
aspect_ratio = int(before_r)
diameter = int(after_r_parts[1])



#calculating volume
volume = ((math.pi * width ** 2 * aspect_ratio)*(width*aspect_ratio+(2540 * diameter))) / 10000000000



#determining date
timestamp = datetime.now()
date = timestamp.strftime("%Y-%m-%d")



if sale_possibility == "Y":
    phone = input("Please enter your phone number: ")
    with open("volumes.txt", "at") as volumes:
        print(f"{date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}, {phone}",file=volumes)
elif sale_possibility == "N":
    with open("volumes.txt", "at") as volumes:
        print(f"{date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}",file=volumes)
else:
    "I'm sorry, I didn't understand, please try again."


print("width:", parts[0] )
print("aspect_ratio:", before_r)
print("diameter:", after_r_parts[1])
print(f"Volume: {volume:.2f}")