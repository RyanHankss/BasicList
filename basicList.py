# Create an empty list named cars

cars = []

# Accept user input (raw_input) with types of cars
model = 0

# Add each new car to the end of the list

while model != "done":

    model = raw_input('what type of car do you want to add to the list?\n')

    cars.append(model)

else:
    cars.remove("done")

# Sort the cars alphabetically

cars.sort()

# Print the list of cars
print cars
