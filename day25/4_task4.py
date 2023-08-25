# Create a function to check whether a input character is vowel or not. Handle the possible exceptions

def is_vowels(char):
    if type(char) =/= str:
        return False
    if char.isnumeric():
        return false
    return char.lower() in  ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

result = is_vowels("2")
print(result)


