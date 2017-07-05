'''
Created on Jun 27, 2017

@author: kyriacos
'''

def superDynaParams(myname, *likes, **relatives): # *n is a list and **n is dictionary
    print '--------------------------'
    print 'my name is ' + myname

    print 'I like the following'

    for like in likes:
        print like

    print 'and my family are'

    for key in relatives:
        if relatives[key] != None:
            print relatives[key]
             

superDynaParams('Mark Paul', 'programming','arts','japanese','literature','music', father='papa',mother='mama',sister='neechan',brother='niichan')
