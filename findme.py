import random

myNo = random.randint(0, 100)
userNo = 0
attempts = 0

print("--------------------------------------------")
print("\n")
print("Welcome to PLAY_WORLD! " + "\n")
print("--------------------------------------------")
print("please enter a Your name")
name = input()
print("Hello " + " " + name)
print( " " + "let's start the game "+ name )
print("--------------------------------------------")

while userNo >= 0:
    print("Guess The My Number")
    userNo = int(input())
    attempts += 1
    if userNo == myNo:
        print("YaHooo You Found it My Number (In " + " " + str(attempts) + " " + "attempt)!!!")
        break
    elif userNo > myNo:
        print("You are Enterning to large number please try again !!")
    else:
        print("You are Enterning to Small Number please try again !!")

print("--------------------------------------------")
print("My number is :: ")
print("----||" + str(myNo) + "||----")
print("--------------------------------------------")
print("\n Thank You I think you'r enjoyed!!! \n")
print("[----'success is a not key point , key point is a sucess keep trying'---] \n")
print("-------***---------***---------***-------")