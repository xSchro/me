"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# i think that this line creates a list of different strings.
some_words = ['what', 'does', 'this', 'line', 'do', '?']

# i think that this line selects a word from some 
for word in some_words: #printed the words line by line from the list
    print(word)

# i think that the variable x is a key or index for one of the words in some_words and the function will print the word located by x.
for x in some_words:
    print(x) 

# i think that this command prints the full list of words.
print(some_words) # this printed the full list

#checks if the function length of the list is larger than 3
if len(some_words) > 3: #as the length was larger than three it printed the statement
    print('some_words contains more than 3 words')

#defines a function called useful function.
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    #this code checks what playform you are on and then it will print the information about your operating system.
    print(platform.uname()) # checked my systems components including sytem, node, release, cersion. machine. processor.  

# this code will run useful function with any of the inputs inside of the functions.
usefulFunction()
