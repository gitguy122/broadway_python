# JSON stands  for JavaScript Object Notation
# It is one of the file format to transfer  data around the web or system
# It s a very famous way  of file transfer  in the REST APIs.
# Python has a built-in support for json handling.

# Rules in a json file
# 1. keys and values must be enclosed in double quotes
# 2. Information can be enclosed in an array
# 3. Double quotes are not required for the number datatype
# 4. Extension of the json file is .json
# for example:
student = {"name": "jon", "address": "LTM"}  # This can be valid json
student = {'name': 'jon', 'address': 'LTM'}  # INVALID JSON . Json must have double quotes

student = [
    {"name": "jon", "address": "LTM", "phone": 9873030338},
    {"name": "ram", "address": "KTM", "phone": 9873030338 },
    {"name": "jon", "address": "LTM", "phone": 9873030338},
]  # VALID Json



import json


filename = "student.json"
with open(filename, "w+") as fp:
    data = json.dumps(student, indent=2)
    fp.write(data)
    fp.seek(0)
    data = fp.read()
    data = json.loads(data)

name = data[1]["name"]
print(name)

