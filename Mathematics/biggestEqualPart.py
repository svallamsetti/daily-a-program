def biggestEqualPart(x, y):
    if( x == y ):
        return (x, y)
    else:
        if(x>y):
            if(x>y*2):
                return biggestEqualPart(x-(y*2), y)
            else:
                return biggestEqualPart(x-y, y)
        else:
            if(y>x*2):
                return biggestEqualPart(x, y-(x*2))
            else:
                return biggestEqualPart(x, y-x)

biggestEqualPart(5,4)
biggestEqualPart(1680,640)
