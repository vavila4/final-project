
import time
def Chapter1_intro():
    print(" Chapter 1:")
    time.sleep(1)
    print ("Loud beeping noises, the character is in a dark space pod. He doesn’t wake up until after a few beeping noises. Hes confused, the lights turn on; his heart is pounding louder than ever. He is stuck, and looks around only to find a boy through the crack of his window")
    time.sleep(1)
    print("The man tells you to follow him, and gives you a weapon to choose")
    ch1_1()
def ch1_1():
    print(" Player chooses weapon,Player interacts with NPC that helped him")
    FirstChoice= input("1,2")
    if FirstChoice == "1":
        print("* They found a cabin to hide in *.")
        import Chapter2
    elif FirstChoice == "2":
        print("*look for supplies and go to town*")
        time.steep (1)
        print("Asks man, How did I get here?")
        time.steep(1)
        print("*TRUCK BRUSHES PAST YOU*")
        time.steep (1)
        print ("Whoa that was close!")
        time.steep(1.5)
        print("why is everything so far")
        time.steep(1.5)
        print("this rain isnt helping")
        time.steep (2)
        print ("*YOU ARRIVE AT A TOWN*HO")
        time.steep(3)
        print(" Start, Chapter 2")

Chapter1_intro()