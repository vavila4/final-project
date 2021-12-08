
import time
def Chapter4():
    print("Begin, Chapter 4")
    print ("*you* finds a mirror, should i take it")
    print("hears a noise in the store")
    print(" sees a shadow in the mirror")
    print("*YOU walk towards the shadow")
    print("YOU: Hey whoever is there come out now!")
    print("Women: its me ally the girl you helped")
    FourthChoice = input("-- Your respond with:a,b,c")
    if FourthChoice == "a":
        print(" What are you doing here?")
        print ("Women: i dont know where else to go and im alone here")
        print ("walks out of store")
        Chapter4()
    elif FourthChoice == "b":
        print ("Women: i want to go on this trip with you")
        print("no way, im not here to babysit")
        Chapter4()
    elif FourthChoice == "c":
        print("*tell her to go away and ignore her*")
        print("she still follows")
        print ("Start, Chapter 5")
        import Chapter5
Chapter4()
