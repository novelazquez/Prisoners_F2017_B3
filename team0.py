####
# Team Members: Mr. Niemitalo and .... only me.
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = '0 Nolan & Tim' # Only 10 chars displayed.
strategy_name = 'test the waters '
strategy_description = 'tit for tat but if they colude 5 times then betrays then it checks if they are running tit for tat and will either colode with a tit for tat or betray every thing else  '
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    their_history = their_history.lower()
    if len(my_history)==0: #first move colude
        return 'c'
    elif my_history[-4:] == 'ccbc' and their_history [-3:]== 'ccb':# if they run tit for tat the colude
        return 'c'
    
    elif their_history [-1:]== 'b': #tit for Tat
        return 'b'
    elif their_history.count('b')==19:
        return 'b'
    
    elif their_history [-5:]== 'ccccc':# test the waters, if they colude 5 time betray
        #return 'b'
        if my_history [-1]== 'b':# test the waters, if they colude 5 time betray then couludes again
            return 'c'
        else:
            return 'b'
   
    elif  their_history [-5:]== 'cbcbc': # betray if they alternate
    
        return 'b'
    
    else:
        return 'c'
     
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             