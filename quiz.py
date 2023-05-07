print('Welcome to my quiz')
score = 0
playing = input("Do you want to play? ")

if playing.lower() != 'yes':
    quit()
   
print("Okay let's play 😆")   

answer = input("What does CPU stand for? ").lower()

if answer == "central processing unit":
    print("Correct! 👏")
    score += 1
else:
    print("Wrong! 😱")

answer = input("What does GPU stand for? ").lower()

if answer == "graphics processing unit":
    print("Correct! 👏")
    score += 1
else:
    print("Wrong! 😱")

answer = input("What does RAM stand for? ").lower()

if answer == "random access memory":
    print("Correct! 👏")
    score += 1
else:
    print("Wrong! 😱")

answer = input("What does PSU stand for? ").lower()

if answer == "power supply":
    print("Correct! 👏")
    score += 1
else:
    print("Wrong! 😱")

print("You got " + str(score) + " questions correct!")
print("Your score is " + str(score/4 * 100) + "%.")