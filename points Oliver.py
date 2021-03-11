points  = [3,6,10,10,6] # All the points scored in a game
total_points = 0 # A variable to store the total of all the elements in the points list added together

for i in range(len(points)): # A loop that will run the same amount of times as there are elements in the list
    total_points += points[i] # Add each element of points to whatever total points is

print("The total amount of points is: {}".format(total_points)) # Display the points