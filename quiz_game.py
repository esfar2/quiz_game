print("Welcome to my computer quiz!!!")

playing = input("Do you want to play? yes or no ")

if playing.lower() != "yes":
    #quits the program and does not run it further 
    quit()
score = 0
print("Awesome!! Let's play")

answer = input("What does CPU stands for? ")

if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
    
answer = input("What does GPU stand for? ")

if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
    
answer = input("What does RAM stand for? ")

if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
print(f"You got {str(score)} questions correct!!")