"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

age = int(input("What is your current age?  "))

max_hr = 220 - age

range_high = int(max_hr * .85)
range_low = int(max_hr * .65)

print(f"When you physically exercise to strengthen your heart, you should maintain your heart rate within a range for at least 20 minutes. At age {age}, your maximum heart rate is {max_hr}, so you should maintain a heart rate between {range_low} and {range_high} for at least 20 minutes.")