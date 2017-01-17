# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
avg = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count+1
        avg += float(line[20:26])
       
print "Average spam confidence:",avg/count   