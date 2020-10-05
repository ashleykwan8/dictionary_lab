# put your code here.

nFile = open(test.txt)
 
def letter_count_in_dict(nFile):
    ''' Defines count of each letter in dictionary'''
    
   
    counted_letters = {} #empty dictionary 

    for letter in nFile:
        if letter.isalpha() == True: 
            counted_letters[letter] = counted_letters.get(letter, 0) + 1

    return counted_letters

print(letter_count_in_dict(nFile))

