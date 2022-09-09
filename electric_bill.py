x=float(input('enter the number of unit used :'))
if x<=100:
    print('your payment amount is: 0')
if x>100:
    y=x-100
    if y<100 :
        print('your payment amount is: ',y*5)
    if y>100 :
        y=x-200
        print('your payment amount is: ',(y*10)+500)
