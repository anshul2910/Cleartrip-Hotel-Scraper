lines_seen = set()
outfile = open('DuplicatesRemoved.txt', "w") #use this ONLY if you encounter some Duplicates
infile = open('HotelLinks.txt', "r")
for line in infile:
    print(line)
    if line not in lines_seen:  # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
