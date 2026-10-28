# Notes cleaner
#the coding thingy


n = int(input("how many characters to preview? "))
file = open("class-notes.txt", "r")
print(file.read(n))
file.close()
print()

#total lines
file = open("class-notes.txt", "r")
lines = file.readlines()
file.close()
print("total lines:", len(lines))
for i in range(len(lines)):
    print(i+1, "->", lines[i].strip())
print()

#part 3 filter lines
word = input("skip lines starting with: ")
file = open("class-notes.txt", "r")
for line in file:
    if line.startswith(word):
        print("skip ->", line.strip())
    else:
        print("keep ->",line.strip())
file.close()
print()

#old lines copied to new file
file = open("class-notes.txt", "r")
lines = file.readlines()
file.close()
out = open("odd-lines.txt", "w")
for i in range(0, len(lines), 2):
    out.write(lines[i])
out.close
print("odd lines saved to odd-lines.txt")