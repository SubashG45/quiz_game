print("Welcome to my computer quiz!")

playing = input("Do you want ot play game? ")

if playing.lower() != "yes" :
    quit()
print("Okey then lets paly :)" )
score = 0

ans = input("what country do i live? ")
if ans.lower() == "nepal":
    print("Correct! ") 
    score += 1
else:
    print("You got wrong answer")

ans = input("what country do i live? ")
if ans.lower() == "nepal":
    print("Correct! ") 
    score += 1
else:
    print("You got wrong answer")   

ans = input("what country do i live? ")
if ans.lower() == "nepal":
    print("Correct! ") 
    score += 1
else:
    print("You got wrong answer") 

print("You got "+ str(score) + " correct answers")