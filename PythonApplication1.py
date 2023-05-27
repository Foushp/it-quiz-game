print("Welcome to my questionaire")

play = input("Want to start? ")

# the variable play is defined. The input prompt user for an input 


if play.lower() == "yes":      
    print("Lets play the questionaire.")

# if and else statements are involved if they are any conditions if the user type in the input


else:
    print("Exiting the questionaire.")
    quit()

# canceling program if anything other than yes 

reponse = input("What does DHCP stand for? ")
if reponse == "domain host control protocol":
    print("thats it! It's domain host control protocol")

 # We ask an input for question given, if not the answer the condition will print out that they are inccorrect.   

else:
    print("that is incorrect")

reponse = input("What does SMTP stand for? ")
if reponse == "simple mail transfer protocol":
    print("thats it! It's simple mail transfer  protocol")

else:
    print("that is incorrect")

reponse = input("What is ssh port number? ")
if reponse == "port 22":
    print("thats it! It's port 22")

else:
    print("that is incorrect")


