#List
values = [1, 2, "rahlu", 4, 5]
#list is data type that allows multipal values and can be different data type
 
print(values[0]) #1

print(values[3]) #4

print(values[-1]) #5
print(values[1:3]) # 2 Rahul
values.insert(3, "Ghadge")
print(values)
values.append("End")
print(values)

del values[0]

print(values)

# Tuple- Same as a data type but,Immutble

val = [1, 2, "Rahul", 4, 5]

print(val[1])

val2 = "RAHUL"

#Dictionary

dic ={"a":2, 4:"bcd", "c": "hello world"}

print(dic[4])
print(dic["c"])
# how to creat dictinories at run time

dict = {}

dict["firstname"] = "Rahul"

dict["lastname"] = "Ghadge"

dict["Gender"] = "male"

dict["age"] = "26"




print(dict)
