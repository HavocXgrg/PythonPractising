# CodeWithHarry challenge
# To make a game ko Bancha Crorepati?
import random

print("************ Greetings!, Welcome to VampHavocX present ko Bancha Crorepati ****************")
name = input("what is your name? ")
proceed = input("Do you want to proceed to play the game? yes or no? :")
if proceed == "yes":
    print("Welcome to the game",name)
else:
    exit()

# making the list of the questions:
q_list = ["who is the current prime minister of Nepal?",
          "who is the Home Minister of Nepal?",
          "Who is the Mayor of Kathmandu Metropolitan City?",
          "Which is the national Game of nepal?",
          "Which is the first highway of Nepal?",
          "Who was the Zero inventor?",
          "When did the 14 zonal and 75 districts are divided occur in Nepal?"
          ]

# making the list of the answer with respect to the similar index as above question:
ans_list = ["prachanda", "Rabi Lamichhane", "Balendra Shah",
            "Volleyball", "Tribhuvan Rajpath", "Arya Bhatt", "B.S. 2018 Baikhakh 01"
            ]


# making a function that randomly generate question from q_list:
def generator():
    print(random.choice(q_list))


generator()
