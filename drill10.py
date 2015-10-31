epic_programmer_dict={'Tim Berners-Lee':'tbl@gmail.com','Guido van Rossum':'gvr@gmail.com',
                      'Linus Torvalds':'lp@gmail.com','Sergey Brin':'sb@gmail.com',}
print epic_programmer_dict
epic_programmer_dict={'Tim Berners-Lee':['tbl@gmail.com',111],
                      'Guido van Rossum':['gvr@gmail.com',222],
                      'Linus Torvalds':['lt@gmail.com',333],
                      'Larry Page':['lp@gmail.com',444],
                      'Sergey Brin':['sb@gmail.com',555]}
print epic_programmer_dict

personsName = raw_input("please enter a name: ")

personsInfo = epic_programmer_dict[personsName]

try:
    personsInfo = epic_programmer_dict[personsName]
    print personsInfo
except:
    print 'No information found for that name'
    
epic_programmer_dict={'tim berners-lee':['tbl@gmail.com',111],
                      'guido van rossum':['gvr@gmail.com',222],
                      'linus torvalds':['lt@gmail.com',333],
                      'larry page':['lp@gmail.com',444],
                      'sergey brin':['sb@gmail.com',555]}
personsName=raw_input('please enter name: ').lower()
