print ("There are two boxes in front of you:\n Yellow and Red. \n Which one do you choose?")
box = input("> ")

if box == "Yellow":
    print("Oh wow, this box is filled with tiny scorpians ready to crawl over you.")
    print("What do you do now?")
    print("Option 1: Eat the scorpiions.")
    print("Option 2: Run away.")

    yellow = input("* ")

    if yellow == "1":
        print("""
        You get indigestion and have to run away! OH NO, but you are a slow runner! \n The scorpions slowly catch up to you and eat your flesh. In front of your eyes. \n GG homie, rest easy.""")

    if yellow == "2":
        print("Okay, so you are a coward. But a smart one, that is acceptable. \n But amidst running, you trip on your shoelaces that you didn't tie up this morning because you thought you were going to have a normal day. HAHAHA, jokes on you. \n Now, what do you do? THe scorpians have become these large mosters! \n 1. Slay your sword that is suddenly in your hands at them? \n 2. Wake up from your nightmare?")

        coward = input("~ ")
        if coward == "1":
            print("Okay, now you have become this elite sword wielder and are now living in glory! Congratulations! Your life will be very different from this very moment.")

        else: 
            print("Good morning, go have some breakfast, you must be starving.")

if box == "Red":
    print("As soon as you open the box, you are in the middle of a beautiful forest, that is filled with flowers and fruits that you can eat without worrying about getting poisoned.")
    print("As you trudge across the marvelous forest, you see a thunderstorm coming your way. \n What do you do?")
    print("Option 1: Look for an umbrella")
    print("Option 2: Run in the skecthy building that is to your left")

    red = input("* ")

    if red == "1":
        print("You enjoy the rain drizzling around you and even get to say a marvelous rainbow! Good choices. ")

    if red == "2":
        print("Have the scary movies not taught you ANYTHING in life?!? Please re-think your life decisions. Thank you for playing. \n I don't think you need me to tell you, but you if you do. You died. There was a troll in the building that sniped people for fun.")