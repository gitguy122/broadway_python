#  remove() method
#  remove method takes list item as a parameter

vowels = ["a", "e", "i", "o", "u"]
vowels.remove('e')
print(vowels)

#  if we pass a parameter not present in the list then it raises error
vowels.remove("p")  # It raises ValueError



# pop() method
# pop takes index as a parameter
vowels = ["a", "e", "i", "o", "u"]
result = vowels.pop(2)
print(result) # 'i'
print(vowels) # [ "a", e , o , u]

# pop vowels also returns a valur from the index passed as the parameter.
# In the above example result gives 'i' becaouse  'i' s at 2nd index. And , finally 'i' us
#also removed from the list vowels
a = [1, 2, 3, 4]



# Clear () method .It clears the lists
vowels = ["a", "e", "i", "o", "u"]
vowels.clear() # it clears the list
print(vowels)


#  index () method. It takes list item as an argument
vowels = ["a", "e", "i", "o", "u"]
result = vowels.index("o")
print(result)  # 3

# index () methods also takes start and end as parameters
vowels = [5, ,4, 10, "o", "u", 10, 4]
result = vowels.index(4, 2, 8)
print(result)  # 6
 result = vowels.index(2, 4, 8)
 print(result) # error as it is not in the list

 # count() method takes list item  as a parameter and returns the number of repetition of that
 # item
vowels = ["a", "e", "i", "o", "u", "o", "o", "a", "i", ]
results = vowels.count("a")
print(results) #2
print(vowels.count("o"))  #3


#reverse() method it reverses the item of the list
fruits = ["banana","apple","mango"]
fruits.
