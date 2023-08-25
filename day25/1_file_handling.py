# We can handle the files using Python
# In file handling , we can study how to open a file, read a file, write   in a file and close a file.


# r => Read Mode
# w => Write Mode
# r+ => Read and Write mode
# w+ => Write and Read mode


filename = "message.txt"
fp = open("filename", "w")
fp.write("This world shall know pain")
fp.close()

fp = open("filename", "r")
data = fp.read()
fp.close()
print(data)

fp = open("filename", "r+")
data = fp.read()
fp.write(".i am learning python")
fp.close()
print(data)

fp = open("filename", "w+")
data = fp.read()
fp.write("i am doing my best")
fp.close()
print(data)