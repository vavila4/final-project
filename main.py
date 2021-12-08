#Vanessa Avila
#11/15/21

def gameintro():
# Use a breakRoint in the code line belov to debua vourscript
    print("*" * 67)
    print("**           Game written and created by Vanessa Avila     **")
    print("**                                                          **")
print("**  A 19 year old kid trying to escape from the place. He got captured to be placed in some sort of on going game of survival, and death **")
print("**   Your goal is to Learn about what’s happening, survive the games every time they are placed     **")
print("** save himself including a boy trapped there as well **")
print("*" * 67)
def main():
    print("Enter your name before starting")
    player = input("[Player Name: ]")
    gameintro()
    answer = input("\n Start the Game ???(Y/N): ")
    answer = answer.upper()
    if answer == 'Y':
        print("Start, Chapter 1")
        import Chapter1
    elif answer == 'N':
        print(" Nope?, to late.")


main()