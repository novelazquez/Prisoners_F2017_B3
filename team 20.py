team_name = 'Nolan&Zack&Tim' # Only 10 chars displayed.
strategy_name = 'Does it really mater '
strategy_description = 'do OKAY '
    
def move(my_history, their_history, my_score, their_score):
    their_history = their_history.lower()
    if len(my_history)==0: #first move colude
        return 'c'
    if their_history[-2 :] == 'bb':# betray if they betray twice
        return 'b'
    if their_history[-2 :] == 'cc': #colude if they colude twice
        return 'c'
    if their_history[-4 :] == 'bcbc' or their_history[-4 :] == 'cbcb':#kill alternate 
        return 'b'
    if my_score < their_score: # betray if we are losing 
        return 'b'
    elif my_score == their_score:# colude if we are winning or equal to
        return 'c'
    elif their_history [-5:]== 'ccccc':# test the waters, if they colude 5 time betray
        if my_history [-1]== 'b':# test the waters, if they colude 5 time betray then couludes again
            return 'c'
        else:
            return 'b'
            
    elif their_history.count('b')==15:# always betray if we have been betrayed 15 times 
        return 'b'
    else:
        return 'c'
    #Blah Blah Blah code stuffffffffffffffffff