
def game():
    print(" Chapter 3 Start,")
    print(" You leave after hel[ing out women and continue looking fpr things")
    print("*You* continue to walk through an unfamiliar part of town")
    print("*YOU*: A store")
    print("*you*: looks abandoned ")
    SecondChoice = input("Walk into the store (Y/N):")
    if SecondChoice == "y":
        print("*You* walks into the store and sees things to take")
        import Chapter4
    elif SecondChoice == 'n':
        print ("*you*: This will last me for a week of survival")
        print("*You* takes food and supplies")
        import Chapter4
game()