y=0
while y<10 :
    x=int(input("enter the percentage :"))
    if x>90:
        print("your grade is A")
    else :
        if x>80 :
            print("your grade is B")
        else :
            if x>=60 :
                print("your grade is C")
            else :
                print("your grade is D")
