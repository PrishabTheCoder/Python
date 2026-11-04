#notebook merger
#topics open, split, os.path.exists, os.remove. file merge

import os

#part 1 -- read with autoclose
print("=== Science Notes ===")
with open("science-notes.txt", "r") as f:
    for line in f:
        print(line.strip())
print()

#part 2 check and merge
print("=== Merging notes===")
if os.path.exists("all-notes.txt"):
    print("all-notes.txt already exists- overwriting")
else:
    print("all-notes.txt not found creating now")


#part 3 check and merge
print("=== Merging notes===")
if os.path.exists("all-notes.txt"):
    print("all-notes.txt already exists")
else:
    print("all-notes.txt not found - creating now")
#checks for file if not found it creates it
content = ""
with open("science-notes.txt", "r") as f:
    content += "---science-notes.txt ---\n"
    content += f.read() + "\n"
with open("maths-notes.txt", "r") as f:
#r means read
    content += "--- maths-notes.txt ---\n"
    content += f.read() + "\n"
with open("all-notes.txt", "w") as out:
#w is write
    out.write(content)
print("saved to all-notes.txt")
print()

#part 4 delete the merged file
if os.path.exists("all-notes.txt"):
    os.remove("all-notes.txt")
    print("all-notes.txt")
else:
    print("all-notes.txt doesnt exist.")