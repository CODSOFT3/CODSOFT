print(''' _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|               _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                              

''')
def add(n1,n2):
    return n1+n2

def substract(n1,n2):
    return n1-n2

def multiple(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations={"+":add,"-":substract,"*":multiple,"/":divide,}
should_countine=True
num1=float(input("What's the first number?: "))
while should_countine:
    
    for symbol in operations:
       print(symbol)
    operation_choice=input("pick an operation: ")
    num2=float(input("what the next number: "))
    answer=operations[operation_choice](num1,num2)
    print(f"{num1} {operation_choice} {num2} = {answer}") 
    user_choice=input(f"type 'y' to continue calculating with {answer} ,or type 'n' to final answer: ")
    if user_choice=="y":
      num1=answer
    else:
        should_countine=False