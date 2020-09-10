import random
lst = ["s","w","g"]
choice = random.choice(lst)
i = 0
tc = 10
comp = 0
human =0
while i < tc:
    print("enter the your choice snake for s ,gun for g ,water for w")
    inpnum = input().lower()
# snake ke samne jab computer ne water dikhaya or snake pani pee gya
    if inpnum == choice:
        print("Tie between you and computer")
        print(f"You Select {inpnum} and computer {choice}")
    elif inpnum=="s" and choice=="w":
        human = human +1
        print(f"you guess is {inpnum} and computer guess is {choice}")
        print("You win 1 point")
        print(f"your point is {human} and computer point is {comp}")
    # snake ke samne gun or gun se snake ko mar diya
    elif inpnum=="s" and choice=="g":
        comp = comp +1
        print(f"you guess is {inpnum} and computer guess is {choice}")
        print("computer win 1 point")
        print(f"your point is {human} and computer point is {comp}")
    elif inpnum=="w" and choice=="s":
        comp = comp +1
        print(f"you guess is {inpnum} and computer guess is {choice}")
        print("computer win 1 point")
        print(f"your point is {human} and computer point is {comp}")
    elif inpnum=="w" and choice=="g":
        human = human +1
        print(f"you guess is {inpnum} and computer guess is {choice}")
        print("You win 1 point")
        print(f"your point is {human} and computer point is {comp}")
    elif inpnum == "g" and choice == "s":
        human = human + 1
        print(f"you guess is {inpnum} and computer guess is {choice}")
        print("computer win 1 point")
        print(f"your point is {human} and computer point is {comp}")
    elif inpnum == "g" and choice == "w":
        comp = comp + 1
        print(f"you guess is {inpnum} and computer guess is {choice}")
        print("You win 1 point")
        print(f"your point is {human} and computer point is {comp}")
    else:
        print("Wrong Input please check your spelling")
    i+=1
    print(f"Total Number of chances{tc},now left {tc-i} ")
print("print game over")
if human==comp:
    print("ties between you")
elif human>comp:
    print("human is winner")
elif human<comp:
    print("computer is winner")
print(f"Your points {human} Computer points {comp}")
