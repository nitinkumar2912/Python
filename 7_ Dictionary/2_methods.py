#  Dictionary is mutable can be changed
marks = {
    "Whuok" : 100,
    "Nitin" : 200,
    "alltm" : 300,
    "list" : [1,5,6]
  
}

print(marks)
print(marks.items())

print(marks.keys()) # data is left side 
print(marks.values()) # data in right side
marks.update({"Nitin":250 , "jatin" : 100}) # update the data value 
print(marks)





