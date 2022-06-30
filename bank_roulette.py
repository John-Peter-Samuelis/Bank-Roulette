import random

print("WELCOME TO THE BANKER'S ROULETTE")
number_of_people    = int(input("Enter the number of people: "))
restaurant_table    = []

for element in range(number_of_people):
    print(f"Enter the {element+1} name: ")
    name = input()
    restaurant_table.append(name)

print(restaurant_table)

who_pays_position   = random.randint(0,len(restaurant_table)-1)
who_pays            = restaurant_table[who_pays_position]

#all of these could be handled using choice function in python. random.choice()

print (f"{who_pays} is going to buy the meal today")
