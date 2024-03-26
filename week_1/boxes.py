item_quantity = int(input("How many items were manufactured? "))
per_box = int(input("What is the maximum number of items that fits in the box? "))
item = input("What item is being manufactured? ")

import math

boxes_needed = math.ceil(item_quantity / per_box)

remainder = item_quantity % per_box

print(f"For {item_quantity} {item}, you will need {boxes_needed} boxes.")

if remainder == 0:
    print("There will be no partially filled boxes, everything should fit perfectly.")

elif remainder == 1:
    print(f"The last box will be partially filled, and will only have 1 {item}.")

else:
    print(f"The last box will only be partially filled, and will only contain {remainder} {item}s.")
