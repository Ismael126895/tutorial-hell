#doesn't allow duplicates, unordered list, randomly organised, you can add but not change item
# you cannot access items in a set but can print them using for loops
fruits = {"orange","banana","lemon"}
print(len(fruits))
print(fruits)
print(type(fruits))

fruitss =set(("orange","banana","lemon")) #use this method to create an empty set
fruits1={}
print(type(fruits1)) # class dict
fruits2=set(())
print(type(fruits2)) # class set
print(fruitss)

fruits3={"watermelon","cherry","fig"}

for item in fruits3:
    print(item)

print("fig" in fruits3)