#  Flexible Calculator 
def calculator(a,b, op = '+'):
    if op == '+':
        return a + b 
    elif op == '-':
        return a-b 
    elif op == '*':
        return a * b 
    elif op == '/':
        if b == 0 :
            return "Error : canno divide by zero "
        return a/b 
    return "Error: unknown operator '%' "
print(calculator(10, 5))
print(calculator(10, 5,"-"))
print(calculator(10, 5,"*"))
print(calculator(10, 0,"/"))
print(calculator(10, 5,"%"))