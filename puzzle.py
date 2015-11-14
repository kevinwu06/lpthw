def play(choices, answer):
    
    print "What do you do? Pick one:"
    
    for i in range(len(choices)):
        print "%d) %s" % (i+1, choices[i])
        
    pick = raw_input("->")
    
    if int(pick) == answer:
	    return True
		
    else:
	    return False
	
