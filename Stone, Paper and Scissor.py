# Stone, Paper and Scissor in python

from random import randint
import csv

out = ['Stone','Paper', 'Scissor']

name = input("What is your name?:")
print("Welcome,",name)

with open(r"C:\Users\91944\Python Projects\player.csv", "a") as fh:
    times = int(input("For how much times you want to play this game?:"))
    score = 0
    for i in range(times):
        computer = out[randint(0,2)]
        print("Press \n\
              1 to play Stone\n\
              2 to play Paper \n\
              3 to play Scissor")
        option = int(input("Enter your number as per the option:"))

        if option == 1 and computer == "Paper":
            print("The computer won this time")
        elif option == 2 and computer == "Scissor":
            print("The computer won this time.")
        elif option == 3 and computer == "Stone":
            print("The computer won this time")
        else:
            print("You won")
            score += 1
    writer = csv.writer(fh)
    writer.writerow([name,score])

with open(r"C:\Users\91944\Python Projects\player.csv","r") as fh:
    option = input("Do you want to know the hall of records of this game?(yes/no):")
    if option == "yes":
        reader = csv.reader(fh)
        print("Name \t score")
        for rec in reader:
            print(rec)
            
