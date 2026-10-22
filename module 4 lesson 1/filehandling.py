#file = open("names.txt", "a")
#file.write("Mukesh\n")
#file.close()
file = open("names.txt", "r")
content = file.read()

print(content)
file.close()
