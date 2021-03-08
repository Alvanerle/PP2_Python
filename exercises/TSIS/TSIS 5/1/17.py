def remove_newlines(fname):
    flist = open(fname).readlines()
    return [s.rstrip('\n') for s in flist]

# rstrip removes all white spaces at the end
# of the string 

# strip removes from both sides 

print(*remove_newlines("test.txt"))