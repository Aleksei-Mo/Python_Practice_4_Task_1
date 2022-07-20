# Вычислить результат деления двух чисел c заданной точностью d. 
def CheckInput(data):
     try:
        float(data)
        return True
     except ValueError:
        return False

def Div(a,b,prec):
    a=float(a)
    b=float(b)
    prec=int(prec)
    result=round(a/b,prec)
    return result
    
dividend=input("Enter dividend: ")
divider=input("Enter divider: ")
precision=input("Enter the precision. It sould be in range [1;10]: ")
if CheckInput(dividend)==False or CheckInput(divider)==False or CheckInput(precision)==False or float(divider)==0:
    print("Check entered values! Maybe these are wrong or 'Zero Division Error' was detected!")
else:
    if 11>int(precision) and int(precision)>0:
        print(f"The result of division {dividend}/{divider} with precision {precision} is equal to {Div(dividend,divider,precision)}.")
    else:
        print("The entered precision is out of range [1;10]. Enter correct value!")
