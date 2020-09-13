#Yusef Bayyat
#8/3/20
#This is a code to have an interactive discussion with a computer

def main():
   firstName = input("Enter your name: ")
   Age = input("How old are you? ")
   myName = str("Yusef")
   birthDay = input("So, when is your birthday?")
   myBirthday = str("August 16")
   print("Hello, " + firstName + "! I'm " +myName+"" )
   print("Wow I didnt know you were " +Age+ "!")
   print("Woah! Your birthday is " +birthDay+ "! Mine is " +myBirthday+ ". ")
   print("So anyway I have a question for you, my favorite animal's name starts with the letter " + myBirthday[0] +", what do you think it is? ")
   print("If you guessed Alligator, you guessed correctly!!")




main()
