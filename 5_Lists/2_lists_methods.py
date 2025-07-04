Data = [1 , 55 , 66 , 88 , 44 , 2 , 64 ]
print("Your data is ", Data)

#Insert (Insert the data between the list)
Data.insert(2 ,109) # it will add 109 at index number 2
print("Your new data after inserting is ", Data)

# append(add the data at the end of list)
Data.append(104)
print("Your new data is ",Data)

# Sorting (Make data in order)
Data.sort()
print("Your sorted data is", Data)

# Reverse(Reverse the data)
Data.reverse()
print("Your reversed data is ", Data)

# POP (delete the data at particular index)
Data.pop(2)
print("Your data after poping out is ",Data)

#Remove(remove particualar value from data )
Data.remove(109)
print("Your new data after using remove method is ", Data)


