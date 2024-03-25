# What does the following code print? 

def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yipeee') # doesn't print anything here. the 'return' on line 5 terminates the function call before it can print