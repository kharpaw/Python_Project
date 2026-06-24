print("Welcome to the quiz game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
    
print("Lets play :))") 
score = 0


answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")
    
answer = input("What stands GPU stand for? ")

if answer.lower() == "graphic processing unit":
        print("Correct!")
        score += 1
else:
    print("Incorrect!")
    
answer = input("What ram stands for? ")

if answer.lower() == "random access memory":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
        
 
print("you got " + str(score) + " questions correct.")    