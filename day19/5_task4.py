# wap to delete all the occurences of a specified characters in a given string

s = "All the occurences  of a specified character in a given string"
s1 = s.replace("a", "")
print(s1)

char = input("Pick a character")
result = ""
for each in s:
    if each.lower() == char.lower():
        continue
    result += each
print(result)