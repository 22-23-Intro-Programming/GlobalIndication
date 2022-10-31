def con7(l):
    #l is a list
    for i in range (len(l)-1):
        if l[i] == 7:
            if l[i+1] == 7:
                return True
                #return stops the method

    return False

def sumNot0(l):

    total = 0
    for x in l:
        if x == 0:
            break
        total = total + x

    return total


def sum23(l):

    total = 0
    for x in l:
        if x == 2:
            x = 0
        if x == 3:
            x = x
        total = total + x
                
    return total 

    

def main():

    print(con7([1,2,3,7,7]))
    print(con7([1,5,7,5,7]))
    print(con7([7,2,7,7,7]))

    print(sumNot0([12,8,3,0,4,5,0,6]))
    print(sumNot0([17,3,6,2,5,2,0,8]))

    print(sum23([1,6,8,4]))
    print(sum23([1,8,6,2,7,3,4,8]))
        
    


if __name__ == "__main__":
    main()
