import random

# Snake Water Gun Game
def gameWin(comp, you):
    if comp==you:
        return None
    elif comp=="s":
        if you=="g":
            return False
        elif you=="w":
            return True
    elif comp=="w":
        if you=="g":
            return False
        elif you=="s":
            return True
    elif comp=="g":
        if you=="s":
            return False
        elif you=="w":
            return True

print(f"Comp turn : Snake(s) Water(w) Gun(g)")
randNo = random.randint(1, 3)
if randNo==1:
    comp="s"
elif randNo==2:
    comp="w"
elif randNo==3:
    comp="g"

you = input(f"Your turn : Snake(s) Water(w) Gun(g)")
a = gameWin(comp, you)

print(f"Computer choose {comp}")
print(f"You choose {you}")

if a==None:
    print("The game is tie . ")
elif a:
    print("You win")
else:
    print("You lose")