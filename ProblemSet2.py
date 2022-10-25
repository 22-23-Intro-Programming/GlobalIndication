def Factorial(number):
    answer = 1        
    for i in range(1, number + 1):
        answer *= i
    print(answer)

def DoubleIt():
    double = ""
    w = input("Enter a phrase:")
    for i in range(len(w)):
        double += w[i] + w[i]
    print(double)

def CamelCase():
    c = input("Enter a phrase (at least 2 words):")
    i = 0
    c = c.title()
    while (i < len(c)):
        if c[i] == "/":
            c = c.replace("/", "-")
        elif c[i] == " ":
            c = c.replace(" ", "")
        

            
            
        i=i+1
            
    print("In camel case, your phrase is: " + c)
        
            
    
    
    
        
        



def main():
    print("factorial(4)")
    Factorial(4)
    print("factorial(6)")
    Factorial(6)
    print("factorial(10)")
    Factorial(10)

    DoubleIt()

    CamelCase()
    

if __name__ == "__main__":
    main()
