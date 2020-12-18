def biggestEqualPart(x, y):
    if( x == y ):
        print(x, y)
        return
    else:
        if(x>y):
            if(x>y*2):
                biggestEqualPart(x-(y*2), y)
            else:
                biggestEqualPart(x-y, y)
        else:
            if(y>x*2):
                biggestEqualPart(x, y-(x*2))
            else:
                biggestEqualPart(x, y-x)

biggestEqualPart(5,4)
biggestEqualPart(1680,640)
