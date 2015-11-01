epic_programmer_dict={'tim berners-lee':['tbl@gmail.com',111],
                      'guido van rossum':['gvr@gmail.com',222],
                      'linus torvalds':['lt@gmail.com',333],
                      'larry page':['lp@gmail.com',444],
                      'sergey brin':['sb@gmail.com',555]}
userWantsMore = True

personsName = raw_input('please enter name: ').lower()
personsInfo = epic_programmer_dict[personsName]

try:
    personsInfo = epic_programmer_dict[personsName]
    print 'Name: ' + personsName.title()
    print 'Email: ' + personsInfo[0]
    print 'Number: ' + str(personsInfo[1])
    
except:
    print "No information found for that name"

searchAgain = raw_input('Search again? y/n ')
if searchAgain == 'y':
    userWantsMore == True
elif searchAgain =='n':
        userWantsMore == False
else: userWantsMore == False

while userWantsMore == True:

    personsName = raw_input('please enter name: ').lower()
    personsInfo = epic_programmer_dict[personsName]

    try:
        personsInfo = epic_programmer_dict[personsName]
        print 'Name: ' + personsName.title()
        print 'Email: ' + personsInfo[0]
        print 'Number: ' + str(personsInfo[1])
    
    except:
        print "No information found for that name"
    searchAgain = raw_input('Search again? y/n ')
