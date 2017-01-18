#9.4 Write a program to read through the mbox-short.txt and figure
#out ho h was the sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of
#those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's 
#mail address to a count of the number of times 
#they appear in the file. After the dictionary is produced, the
#program reads through the dictionary using a maximum loop to
#find the most prolific committer.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
contacts = dict()
big_count = 0
big_word = 0
for line in handle:
    if line.startswith('From '):
        line = line.split()
        line = line[1]
        contacts[line] = contacts.get(line,0) + 1
        for word,count in contacts.items():
            if big_count is None or count > big_count:
                big_word = word
                big_count = count
print big_word,big_count
        
