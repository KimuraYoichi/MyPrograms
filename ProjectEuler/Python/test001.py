x = 76576500
# y= x+0.1
#
# print( y )
#
# print(y.is_integer())


def traiangleJudge(n) :
    testNum = (1 + (1 + 8 * n) ** 0.5)
    if testNum.is_integer() :
        print( testNum )
        return testNum
    else :
        return False


# print( traiangleJudge( 28 ) )
print( traiangleJudge( x ) )

# a = 28.23
# print( a.is_integer() )
