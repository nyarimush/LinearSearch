
#generating the table of integers

nlist = [67, 21, 69, 12, 43, 90, 24]
nlist.append(100)

#Using linear search to find the certain integer

searchTerm = 21
#Flag
found = False

for x in range(len(nlist)):
#the if statement checks to see if the search term is in the list
    if (searchTerm == nlist [x]):
        # if the search term was found then it is assigned to true else it would be false
        found = True

#this will check to see what the value found is !

if (found == True):
    print('Found data item')
else:
    print('Not found data item')

