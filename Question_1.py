#Question: Given 8 balls randomly. There are 7 balls sharing the same weight and only 1 ball is lighter. Find that one only lightest ball in the 8 balls.

#Thy H. Nguyen's solution:

#Algorithm: Using the binary search, but complementing it in a much tricky way to find the lightest ball the fastest. 

#Step 1:
#Enumerate all of the balls from 1 to 8. (Each ball will have the distinct number.)

#Step 2:
#Take 2 balls and weigh 4 times (weigh all 8 balls)

#Step 3:
#In the group of 2 lightest weight (The weight will be the same for 3 groups and only different in 1 group.

#Step 4:
#Weigh the two balls in that lightest group.

#Step 5:
#Take the weight of the lightest group subtracts the weight of other 3 groups divide by 2, to find the weight of the 1 in 7 equal weight, 
#The result will be the weight of the lightest ball.
