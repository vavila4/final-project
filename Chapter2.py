
import time
def Chapter2():
    print(" YOU WALK INTO TOWN ")
    time.sleep(2)
    print ("They begin running down the alley ways of this small town")
    time.sleep(2)
    print("*Lots of gunshots are heard everywhere")
    time.sleep(2)
    print("A woman crying for help is heard")
    time. sleep(2)
    print ("Starts thinking should i help or ignore her")
    time.sleep(2)
    Ch_2()
def Ch_2():
    SecondChoice = input("--What is your response?--1,2,3:")
    if  SecondChoice == '1':
        print("help her")
        import Chapter3
    elif SecondChoice == '2':
        print ("Walk away")
        import Chapter3
    elif SecondChoice == '3':
        print ("He runs to them and screams to let her go… please?")
        import Chapter3
Chapter2()

