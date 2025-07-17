import random
user =0
comp =0
def rps():
    global user,comp
    a = input("enter your choice 'r' for rock , 'p' for paper ,'s' for scissors: ")
    print(a)
    choice =["r" , "p" , "s"]
    b = random.choice(choice)
    print(b)
    if a==b :
        print("oh ! its a tie \n")
    if a=="s" and b=="r" :
        print("you loose !!\n")
        comp = comp+1
    if a=="r" and b=="s" :
        print("you win !!\n")
        user = user+1
    if a=="s" and b=="p" :
        print("you win !!\n")
        user = user+1
    if a=="p" and b=="s" :
        print("you loose !!\n")
        comp = comp+1
    if a=="p" and b=="r" :
        print("you win !!\n")
        user = user+1
    if a=="r" and b=="p" :
        print("you loose !!\n")
        comp = comp+1
rps()
c = "y"
while True :
    c = input("enter 'y' if you want to continue playing and 'n' if you wish to stop . : ")
    if c == "n":
        break
    rps()
print(f"your score : {user} || computer score : {comp}\n BYE!!!")