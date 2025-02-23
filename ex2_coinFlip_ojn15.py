#Omarion Neal

#Excercise 2 Coin Flip

#Import a module
import random

#Replicate a coin flip (1 will represent tails, 0 will represent Heads)
flip = random.randint (0,1)

#Apply the multipicative string concatenation to print the output
result = ("Tails" * flip + "Heads" * (1 - flip))

#Display the possibiltity of the flip
print(result)






