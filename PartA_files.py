# Part A - Working with files

print("=== Step 1: open file ===")
f = open("quote.txt", "r", encoding="utf-8")

print("=== Step 2: first read ===")
first_read = f.read()
print(first_read)

print("=== Step 3: second read ===")
second_read = f.read()
print(second_read)

print("=== Step 4: move back to beginning with seek(0) ===")
f.seek(0)
print(f.read())

print("=== read the first line ===")
f.seek(0)
line1=f.readline()
print(line1)

print("=== read the second line ===")
line2=f.readline()
print(line2)

print("=== read line by line")
f.seek(0)
for line in f:
    print(line)

f.close()

# write a new file
f1=open("notes.txt","w",encoding="utf-8")
f1.write("This is my W4 practice.\n")
f1.write("I'm learning how to read and write files.\n")
print("notes added")
f1.close
# add new words
with open("notes.txt","a",encoding="utf-8")as f1:
    f1.write("Now I practising the append code.\n")
    f1.write("Using with open is the safest way.\n")

# Read final notes.txt
with open("notes.txt", "r", encoding="utf-8") as f:
    notes_content = f.read()
f1.close()
print(notes_content)