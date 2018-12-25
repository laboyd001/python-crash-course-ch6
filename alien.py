#dictionaries

alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])
new_points = alien_0['points']
# print("You just earned " + str(new_points) + " points!")
alien_0['x-position'] = 0
alien_0['y-position'] = 25
# print(alien_0)
alien_0['speed'] = 'fast'

print("Original x-position: " +str(alien_0['x-position']))

#Move the alien to the right
#Determine how far to move the alien based on its current speed

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #This increment must be a fast alien.
    x_increment = 3

#The new position is the old position plus the increment.
alien_0['x-position'] = alien_0['x-position'] + x_increment

print("New x-position: " + str(alien_0['x-position']))

#delete the points key/value pair from the dictionary
del alien_0['points']
print(alien_0)