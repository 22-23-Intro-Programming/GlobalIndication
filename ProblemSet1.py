def greeting():
    x = input("Please enter your name:")
    print("Oh, " + x + " ,is it? It is nice to meet you! Have a good day!")


def multiple(x, y):
    print("isMultiple(" + str(x) + "," + str(y) + ")")
    if (x % y) > 0:
        print ("no")
    if (x % y) == 0:
        print ("yes")

def palindrome():
    P = input("Please enter a potential palindrome:")
    P2 = P[::-1]
    print (P2)
    if P2 == P:
        print("Amazing, Genius level palindrome")
    if P2 != P:
        print("Too Bad. Not a Palindrome")
    
    



if __name__ == "__greeting__":
    main()
    
if __name__ == "__multiple__":
    main(8, 3)

if __name__ == "__palindrome__":
    main()

greeting()
multiple(8, 3)
palindrome()
