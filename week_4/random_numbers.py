import random

def main():
    numbers = [16.2,75.1,52.3]
    print (numbers)
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers,3)
    print(f'{numbers}\n')

def append_random_numbers(numbers_list,quantity=1):
    for i in range quantity:
        random_number = round(random.uniform(0,101),0.1)
        numbers_list.append(random_number)

