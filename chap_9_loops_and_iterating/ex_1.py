# The following code causes an infinite loop (a loop that never stops iterating). Why?

counter = 0

while counter < 5:
    print(counter)

# There's no expression made to increment the counter variable, it stays at 0 and loops infinitely 