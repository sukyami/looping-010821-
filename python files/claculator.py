def clac(type, a, b): 
  if type == '+': 
    return a+b 
  elif type == '-': 
    return a-b
  elif type == '/': 
    return a/b 
  elif type == '*': 
    return a*b

def calculator():
  num1 = int (input("Enter number : "))
  while (True):
    operator1 = str (input("Enter operator + or - or * or / or = : "))
    if (operator1 == '+' or operator1 == '-' or operator1 == '/' or operator1 == '*' ):  
      while (True):
        num2 = int (input("Enter number : "))
        operator2 = str (input("Enter operator + or - or * or / or = : "))   
        result=clac(operator1,num1,num2)
        if (operator2 == '='):
          print(result)
          break
        elif (operator2 == '+' or operator2 == '-' or operator2 == '/' or operator2 == '*' ):
          num1=result
          operator1=operator2
        else:
          break
    if (operator1 == '='):
      print(num1)
      break
    else:
      print("Not vaild operator")
      break

calculator()