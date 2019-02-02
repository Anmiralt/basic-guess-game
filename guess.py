print("###############")
print("###############")
print("               ")
print("Guess the word:")
seCRET_WOrd="black"
guess=""
times=0
flag=0
print("NO. OF TRIES>>3")
print("It's in your eye,all over the sky when the moon rises up high")
print("What am I ?")
while seCRET_WOrd != guess and flag==0:
     if times<3:
         guess=input("Enter guess:")
         times+=1
         if(seCRET_WOrd!=guess) and times<=2:
               print("TRY AGAIN")
     else:
          flag=1    
   
if flag==0:
    print("You Win!!") 
else:
    print("You LOSE!!")    
print("###############")
print("###############")   