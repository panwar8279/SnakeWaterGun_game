import random
lst=['S','W','G']
chance=10
no_of_chance=0
computerPoint=0
humanPoint=0
print('*****This is Snake, Water and gun game******\n')

while no_of_chance<chance:
    print("Press S for snake, W for water and G for Gun")
    input2=input()
    Random=random.choice(lst)
    
    if input2==Random:
         print(f"Your guess {input2} and computer guess is {Random}\n")
         print("Tie both 0 point to each\n")

    elif input2=='S' and Random=='G':
        computerPoint=computerPoint+1
        print(f"Your guess {input2} and computer guess is {Random}\n")
        print('Computer win 1 point\n')
    elif input2=='S' and Random=='W':
        humanPoint=humanPoint+1
        print(f"Your guess {input2} and computer guess is {Random}\n")
        print('You win 1 point\n')

    elif input2=='G' and Random=='W':
        computerPoint=computerPoint+1
        print(f"Your guess {input2} and computer guess is {Random}\n")
        print('Computer win 1 point\n')
    elif input2=='G' and Random=='S':
        humanPoint=humanPoint+1
        print(f"Your guess {input2} and computer guess is {Random}\n")
        print('You win 1 point\n')
    elif input2=='W' and Random=='S':
        computerPoint=computerPoint+1
        print(f"Your guess {input2} and computer guess is {Random}\n")
        print('Computer win 1 point\n')
    elif input2=='W' and Random=='G':
        humanPoint=humanPoint+1
        print(f"Your guess {input2} and computer guess is {Random}\n")
        print('You win 1 point\n')
    else:
        print("You have entered wrong input")
    no_of_chance=no_of_chance+1
    print(f"{chance-no_of_chance} is left out of {chance}")
    # print("Game over")
    if(computerPoint==humanPoint):
      print("Tie")
    elif (computerPoint>humanPoint):
     print("Computer wins and you loose") 
    else:
      print("You wins and computer loose") 
    print(f"your point is {humanPoint} and computer point is {computerPoint}")     
print("Game over")
