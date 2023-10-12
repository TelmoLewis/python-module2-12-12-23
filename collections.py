# different ways of storing data
# lists - ordered, mutable (rwd), collection of values [a ,b ,c ...] 
# dictionaries unordered, mutable collection of key-pair values {"key": "value"}
# sets - unordered, mutable, collection of unique values {value1, value2}
# tuples - ordered, immutable, colelction of values (value1, value 2...)

# lists are stored in a variable = []

#colours = ["blue", "red", "green", "yellow"]

#print(colours)

# referencing elements in a list is by their index position
# starts at [0] and also [-1] 

#print(colours[0])
#print(colours[3])
#print(colours[-4])

# slicing - create a sub-list up to but not including the 2nd number in the range

#print(colours[0:2])
#print(colours[1:]) # no 2nd number slices till the end of the list

# altering lists - use index position, need a value, delete with del

#food = ["bread", "cheese", "pasta", "apple"]

#print(food)
#food[0] = "rice" 
#print(food)
#del food[1]
#print(food)

# Checking if item is in a list

#print("pasta" in food)
#print("orange" in food)

# nested list

#numbers = [1, 2, 3, 4]
#letters = ["a", "b", "c", "d"]

#combined = [numbers, letters]

#print(combined[0][1], combined[1][1])

# multiple data types

#my_list = ["red", 5, ["green", "apple"], 10.5]

#print(my_list)
#print(my_list[2][1])
#print(my_list[0])

# list methods

# append 

#my_fruits = ["apple", "orange", "kiwi"]


#my_fruits.append("pear")
#print(my_fruits)

# remove

#my_fruits.remove("apple")
#print(my_fruits)

# insert 

#my_fruits.insert(0, "mango")
#my_fruits.insert(0, "melon")
#print(my_fruits)


# extend - with a list

#my_fruits.extend(["grapes", "cherry"])
#print(my_fruits)

# finding index position

#print(my_fruits.index("mango"))

# reversing

#my_fruits.reverse()
#print(my_fruits)

# sorting

#my_fruits.sort()
#print(my_fruits)
#my_fruits.sort(key=len)
#print(my_fruits)

# join

#x = ", ".join(my_fruits)
#print(x)
#print(type(x))

# Dictionaries {} key:value pairs
# similar to a list, but not indexing
# keys need to be unique, values dont

drinks = {"fizzy": "sprite", "still": "water", "juice": "orange", "alcohlic": "wine"}

print(drinks)
print(drinks["still"]) # can only query with the key not the value 

# add to my dictionary

drinks["non-alcohlic"] = "water"
print(drinks)






