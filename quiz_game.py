print("Welcome to my computer quiz")

playing = input("Do you want to play? ")


if playing.lower() != "yes": 
    quit()

print("OKay! Let's play :)")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')

else: 
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')

else: 
    print("Incorrect!")


answer = input("What does RAM stand for? ")
if answer.lower() == "Random access memory":
    print('Correct!')

else: 
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "Power supply":
    print('Correct!')

else: 
    print("Incorrect!")
