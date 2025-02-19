import random
print("select form given data 0 for rock,1 for paper,2 for scissor")
selection=["rock","paper","scissor"]
my_choice=int(input("enter the number 0,1,2\n"))
if my_choice==0:
    print("my choice\nrock")
elif my_choice==1:
    print("my choice\npaper")
else:
    my_choice==2
    print("my_choice\nscissor")
computer_choice=random.randint(0,2)
if computer_choice==0:
    print("computer_choice\nrock")
elif computer_choice==1:
    print("computer_choice\npaper")
else:
    computer_choice==2
    print("computer_choice\nscissor")

if my_choice==computer_choice:
    print("tie the game")
elif my_choice==0 and computer_choice==2:
    print("You win")
elif my_choice==1 and computer_choice==0:
    print("you win")
elif my_choice==2 and computer_choice==1:
    print("you win")
else:
    print("computer win")