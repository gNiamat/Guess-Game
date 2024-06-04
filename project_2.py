import random
randNum=random.randint(1,100)
value=False
count=0
print(randNum)
print("WELCOME TO GUESS GAME..!!")
print("choose the number between 1 to 100")
while value==False:
    inp=int(input("Guess the number: "))
    if randNum!=inp:
        count+=1
        if count<10:
            if inp>randNum:
                print("you interd greater number...PLZ try again!!")
            elif inp<randNum:
                print("you intered lesser number...PLZ try again!!")   
        else:
            print("EXEEDED max number of guesses :( Better luck next time.") 
            value=True        
    elif randNum==inp:
        print("You gessed the wright number...YOU WON!!")
        score=((10-count)/10)*100 
        print(f"You have taken {count} guesses.") 
        print(f"YOUR SCORE IS: {score}.")
        value=True
with open("ScoreCount.txt","r") as f:
    maxscore=float(f.read())         
if maxscore<score:  
    print("you scored the highest SCORE!! :)")       
    with open("ScoreCount.txt","w")as f  : 
        f.write(str(score)) 
                          