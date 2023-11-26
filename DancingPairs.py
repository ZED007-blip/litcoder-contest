import sys
from itertools import permutations

def Dancing(tiles):
    # Initialize a counter for the number of possibilities
    count = 0
    # Convert the input string into a list of characters
    a = list(tiles)
    # Iterate over all possible lengths of subsequences
    for i in range(1, len(tiles) + 1):
        # Generate all permutations of length 'i' from the list of characters
        per = permutations(a, i)
        # Convert the permutations to a set to remove duplicates
        s = set(per)
        # Iterate over unique permutations and increment the count
        for item in s:
            count += 1
    # Return the total count of possibilities
    return count

#Take Input
inputVal = input()

#Process Output Using Function
outputVal = numTilePossibilities(inputVal)

#Print Output
print(outputVal)
                                                                                                                            
