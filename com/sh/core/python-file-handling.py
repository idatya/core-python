#Python File Handling
f = open("/home/impadmin/Desktop/g&v", "rt")
print(f.read())
print("---------------------------")
#Read Only Parts of the File
"""By default the read() method returns the whole text, but you can also specify how many character you want to return:"""
f = open("/home/impadmin/Desktop/g&v", "rt")
print(f.read(20))
print("---------------------------")
#Read one line of the file:
f = open("/home/impadmin/Desktop/g&v", "rt")
print(f.readline())
#By looping through the lines of the file, you can read the whole file, line by line:
f = open("/home/impadmin/Desktop/g&v", "r")
for x in f:
  print(x)

print("---------------------------")
#Write to an Existing File
f = open("/home/impadmin/Desktop/test.txt", "a")
f.write("Now the file has one more line!")
print("append done")
print("---------------------------")
f = open("/home/impadmin/Desktop/test.txt", "w")
f.write("Woops! I have deleted the content!")
print("write mode done")
print("---------------------------")

#Create a New File
"""To create a new file in Python, use the open() method, with one of the following parameters:

"x" - Create - will create a file, returns an error if the file exist
"a" - Append - will create a file if the specified file does not exist
"w" - Write - will create a file if the specified file does not exist"""

#Delete a File
"""To delete a file, you must import the OS module, and run its os.remove() function:"""
import os
file = "test (copy).txt"
path = "/home/impadmin/Desktop/"+file
#os.remove(path)
print("File "+file+" deleted successfully")
print("---------------------------")

#Check if File exist:
"""To avoid getting an error, you might want to check if the file exist before you try to delete it:"""
import os
file = "test (copy).txt"
path = "/home/impadmin/Desktop/"+file
if os.path.exists(path):
  os.remove(path)
else:
  print("The file does not exists, creating file")
  f = open(path, "w")
	




