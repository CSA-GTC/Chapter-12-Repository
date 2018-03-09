#Gregory Clarke
#Computer Programming
#3/6/2018

def longest_word(filename):
    with open(filename, 'r') as infile: #opens alice 
        words = infile.read().split() #spilts the words in the file
    max_len = len(max(words, key=len)) #finds the max length
    right_word = [word for word in words if len(word) == max_len] #finds the longest word 
    print(right_word,str(max_len)+" characters long") #prints the word and length
    
longest_word('alice.txt') #sends file alice to the function
