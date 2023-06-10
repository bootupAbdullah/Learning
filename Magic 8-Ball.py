name = "Sonia"
question = "Will it be sunny on my birthday?"
answer = ""
import random
random_number = random.randint(1, 15)
#print(random_number)
if random_number == 1:
 answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "Maybe, but it will require some doing"
elif random_number == 11:
  answer = "Have you tried asking ChatGPT?"
elif random_number == 12:
  answer = "Uh...give me a minute.."
elif random_number == 13:
  answer = "Desire != Outcome"
elif random_number == 14:
  answer = "Yes, for sure, you can absolutely do this."
elif random_number == 15:
  answer = "I believe this is doable with some planning."  
else:
  answer = "Error"
if question == "":
  print("Hey, why don't you try asking a question?")
else:
  if name == "":
    print("Question: " + question)
    print("Magic 8-Ball's answer: " + answer)
  else:
    print(name + " asks: " + question)
    print("Magic 8-Ball's answer: " + answer)







