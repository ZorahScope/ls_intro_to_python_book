text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

'''
# Explain why the code below prints different values on lines 3 and 4. 

On line 3 taking a slice creates a new string from which .rfind will give a different index number as opposed to on line 4 
which accounts for the original string when given a range to search from. 

'''