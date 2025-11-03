
#generating the table of integers

nlist = [67, 21, 69, 12, 43, 90, 24]


#Using linear search to find the certain integer

searchTerm = int(input('Enter an integer:'))
#flag
found = False
count = 0

for x in range(len(nlist)):
#the if statement checks to see if the search term is in the list
    if (searchTerm == nlist [x]):
        # if the search term was found then it is assigned to true else it would be false
        found = True
        count = count + 1

#this will check to see what the value found is !

if (found == True):
    print('Found data item', count, 'times')
else:
    print('Not found data item')
