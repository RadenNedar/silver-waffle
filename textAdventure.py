


import time
import os
import sys
def script():
    sys.argv
    print "You awake with a splitting headache, surrounded by near darkness."
    print ""
    time.sleep(1)
    print "After a while, your eyes begin to adjust and you recognize your surroundings to be that of a cold metal room."
    print "To your left, there is a rusted door which seems to be the only way out."
    print ""
    crowbar = 0
    choice1 = 0
    while choice1 == 0:
        room1 = raw_input("What do you do? ")
        if room1 in ("Search", "search","look","Look","look around","Look around","radiator","search radiator","Radiator","Search radiator"):
            crowbar = 1
            print ""
            print "You decide to check the radiator, as the room seems virtually empty otherwise.."
            time.sleep(1)
            print ""
            print "Lodged behind the radiator is what looks to be a crowbar!"
            print "It must have been left here by someone repairing the heating system"
            time.sleep(1)
            print ""
            print "You take the crowbar"
            print ""
            
        elif room1 in ("open door","Open door","door"):
            if crowbar == 1:
                print ""
                print "You approach the door and lodge your crowbar between the crack"
                time.sleep(1)
                print ""
                print "You heave against the crowbar and slowly manage to creak the door open..."
                time.sleep(2)
                print "Your vision goes blurry for a few seconds..."
                time.sleep(3)
                print ""
                print "All that exhertion after just waking up probably wasn't the best idea. Especially with that awful headache"
                time.sleep(2)
                print "Whatever, what matters now is that you found a way out of that strange room"
                print ""
                time.sleep(1)
                choice1 = 1
                
            else:
                print ""
                print "You approach the door and pull on the handle."
                time.sleep(2)
                print "It doesn't budge"
                print "It seems that the rust has really sealed this door shut"
                time.sleep(1)
                print ""
                print "Maybe there's something in the room that could help open it?"
                print ""
            
        else:
            print ""
            print "That doesn't seem to work"
            print ""
            
    print "You slowly creep through the now open door to find yourself staring up at the back of a four armed creature hunched over a monitor."
    time.sleep(1.5)
    print "In the center of the room, a single light hangs down illuminating two doors out of the room."
    time.sleep(2)
    print ""
    print "Door A would require getting passed this strange creature somehow."
    print "Door B is directly to your right, but you think you can make out a few voices right on the other side..."
    print ""
    time.sleep(1)


    def roomBScenario():
        roomb = 0
        roomb2 = 0
        while roomb == 0:
            print ""
            print "choosing to take your chances rather than a definite confrontation,"
            print "you sneak through the door to your right."
            print ""
            time.sleep(2)
            print "Aha!"
            time.sleep(1)
            print "The voices you had heard previously were actually coming from an array of security monitors"
            print "On the screens, you see hundreds of people that seem to be in a similar situation to you."
            print "Except they are all still trapped within their hauntingly similar rooms"
            time.sleep(3)
            print "Beneath the monitors are tons of keys and button bearing indistinguishable symbols, markings and the occasional english."
            print "One of which, seems to have all of the various languages printed on it."
            time.sleep(1.5)
            print ""
            print "Open"
            print ""
            while roomb2 == 0: 
                roombinput = raw_input("What do you do? ")
                if roombinput in ("Back", "back", "go back", "Go back"):
                    print "You decide to head back, not wanting to mess with whatever this contraption controls"
                    roomb = 1
                elif roombinput in ("open", "Open", "press", "Press", "Press the button", "press the button", "press button" "Press button"):
                    print "You don't know what this will do, but you know it has to be better than seeing all these people trapped."
                    print "You press the button"
                    time.sleep(1)
                    print "On the screen you see all of the doors to the rooms swing open and panic break out."
                    time.sleep(1)
                    print "Hundreds flee their rooms as soon as they open"
                    time.sleep(1)
                    print "Many stay though, seemingly afraid of leaving"
                    time.sleep(2)
                    print ""
                    print "Suddenly, alarms go off all throughout the facility and you can see tons of those creatures fighting with the prisoners"
                    print "Some are subdued, while others manage to kill the four-armed beasts"
                    time.sleep(1)
                    print ""
                    print "Almost instantly, the room fills with the monsters and they surround you"
                    print ""
                    over = raw_input("What do you do? ")
                    print "As you try, your vision begins to fade"
                    time.sleep(1)
                    print "The creatures grab hold of you"
                    time.sleep(2)
                    print "Just before falling unconcious, you notice something sticking out of your arm"
                    time.sleep(3)
                    print ""
                    print "The world goes black"
                    print ""
                    script()
                    
                else:
                    print ""
                    print "You're not quite sure that will work"
                    print ""
                
            
    def bar():
        print "As the creature attempts to push you out of the way,"
        print "you quickly bash it over the head with your crowbar; throwing it off balance"
        time.sleep(2.5)
        print ""
        print "after a back and forth of punches and crowbar-fueled slashes"
        print "you stand over the body of the monster."
        time.sleep(1.5)
        print ""
        print "Injured, but alive."
        
        
        
    choice2 = 0
    while choice2 == 0:
        room2 = raw_input("Which door will you try to get to? ")
        if room2 in ("door a", "a", "forward", "go forward", "Door A", "Door a", "door A", "A", "Go forward", "Forward"):
            choice2 = 1
        elif room2 in ("door b", "b", "right", "go right", "B", "Door B", "Door b", "door B" "Right", "Go right"):
            roomBScenario()
        else:
            print "Not an option"
            
    print "You decide to go forward"
    print "Whatever this *thing* is, you're going to need to get past it somehow..."
    print ""
    print "You could try to make conversation with it or just sneak up behind with your crowbar"
    murder = 0
    while murder == 0:
        doora = raw_input("Which will you choose? ")
        if murder == 1:
            break
        elif doora in ("conversation", "make conversation", "Make Conversation", "Make conversation", "talk", "talk to it", "try to talk to it", "Talk"):
            print "You attempt to make conversation with the creature"
            time.sleep(1)
            print ""
            print "{I'm not sure who you are or where I am, but I'm just trying to figure out what's going on}"
            time.sleep(0.5)
            print ""
            print "<How did you get out of your cell?!>"
            print ""
            print "Quickly, the creature runs towards what looks to be an alarm switch on the wall behind you"
            time.sleep(1)
            print ""
            print "Quick!"
            print ""
            print "1. Bar his way and prepare to fight!"
            print ""
            print "2. Attempt to convince him that you're not a threat and theres no need for alarm"
            murderchoice = raw_input("Choose:  ")
            if murderchoice == "1":
                bar()
                murder = 1
            elif murderchoice == "2":
                print "As you begin explaining that you really are no threat and just want to know where you are"
                print "the creature shoves you out of the way and pulls the alarm"
                time.sleep(2)
                print "Almost instantly, the room fills with the monsters as they surround you"
                over = raw_input("What do you do? ")
                print "As you try, your vision begins to fade"
                time.sleep(1)
                print "The creatures grab hold of you"
                time.sleep(2)
                print "Just before falling unconcious, you notice something sticking out of your arm"
                time.sleep(2)
                print ""
                print "The world goes black"
                print ""
                script()
            else:
                print "The creature shoves you out of the way and pulls the alarm"
                time.sleep(2)
                print "Almost instantly, the room fills with the monsters as they surround you"
                over = raw_input("What do you do? ")
                print "As you try, your vision begins to fade"
                time.sleep(1)
                print "The creatures grab hold of you"
                time.sleep(2)
                print "Just before falling unconcious, you notice something sticking out of your arm"
                time.sleep(2)
                print ""
                print "The world goes black"
                print ""
                script()
        elif doora in ("sneak", "crowbar", "Crowbar", "sneak up behind", "Sneak up behind", "attack", "attack with crowbar"):
            print ""
            print "Slowly, you sneak up behind the strange creature"
            time.sleep(1)
            print "."
            time.sleep(1)
            print "."
            time.sleep(1)
            print "."
            time.sleep(1)
            print "The floor creaks beneath you..."
            time.sleep(1.5)
            print "."
            time.sleep(1)
            print "*WHAM*"
            print ""
            print "you stealthily made your way behind the creature and smashed your crowbar into it's head"
            print "It's body falls to the ground and you are left looking over your victim"
            time.sleep(3)
            murder = 1

    print "After assessing the damage, you are positive he's not coming back..."
    time.sleep(1.5)
    print ""
    print "You walk over the body and proceed to open the door to the next room"
    time.sleep(3)
    print "The door doesn't budge"
    print "<Christ! Again?>"
    print ""
    choice3 = 0
    keys = 0
    while choice3 == 0:
        room22 = raw_input("What do you do? ")
        if room22 in ("Search", "search","Search body","search body","body","search creature","creature"):
            keys = 1
            print ""
            print "You check the monster's body for anything useful"
            time.sleep(2)
            print ""
            print "On his hip you find a ring of keys!"
            time.sleep(1)
            print "Maybe these will open the door?"
            time.sleep(1)
            print ""
            print "You take the Keys"
            print ""
            
        elif room22 in ("open door","Open door","door"):
            if keys == 1:
                print ""
                print "Using your newly acquired keys, the door swings open"
                print ""
                choice3 = 1
                
            else:
                print ""
                print "You approach the door and pull on the handle."
                time.sleep(1)
                print ""
                print "It doesn't budge"
                time.sleep(1)
                print ""
                print "Maybe there's something else that could help open it?"
                print ""
                
        elif room22 in ("crowbar","use crowbar","Crowbar","Use crowbar"):
            print ""
            print "You lodge your crowbar into the crack of the door and begin prying"
            time.sleep(2)
            print ""
            print "the door still doesnt seem to budge..."
            print ""
            time.sleep(1)
            print "Maybe there's something else that can help you get in?"
            print ""
            
        else:
            print ""
            print "That doesn't seem to work"
            print ""


    print ""
    print "Walking through the door reveals a long room with what looks like"
    print "an array of extremely complex medical equipment and machines."
    print ""
    time.sleep(1)
    print "strapped to metal examining tables are two regular people!"
    time.sleep(1)
    print "Both are awake, but hooked up to some machine attached to their heads"
    time.sleep(1)
    print ""
    print "One notices you and hisses out: {Help us! Please!}"
    print ""
    
    room3 = 0
    while room3 == 0: 
        med = raw_input("What do you do? ")
        if med in ("help", "Help", "approach", "walk over", "help him"):
            room3 = 1
        elif med in ("ignore", "keep going", "exit", "search",):
            print "Please... He'll be back soon, get us out of here!"
            print ""

        else:
            print "you take a few extra seconds to reconsider..."
    print ""
    print "You walk over to the pair and take a look at the weird machine they are hooked up to"
    time.sleep(2)
    print "{These monsters are trying to take over our brains!}"
    print "{They're trying to remove our free thought and remove our memories.}"
    time.sleep(2)
    print ""
    print "{The doctor will be back soon... If you press the green button}"
    print "{It should release us from these damn tables and turn off the machine}"
    print ""
    time.sleep(2)
    print "There are two buttons on the machine "
    time.sleep(1)
    print ""
    print "A green button, and a red button"
    print ""

    button = 0
    while button == 0:
        rog = raw_input("Which button do you press? ")
        if rog in ("green", "Green", "green button", "Green button", "the green button", "The green button"):
            button = 1
            print ""
            print "You press the green button, as he suggests"
            time.sleep(2)
            print "The latches on both tables snap open."
            print "The pair take no time in getting up and removing the contraptions from their heads"
            print ""
            time.sleep(2)
            print "{Thank you so much, you've saved both of our lives}"
            print "Suddenly, a door at the end of the room slides open and another"
            print "four armed creature walks into the room"
            time.sleep(2)
            print "Upon seeing you and the freed prisoners, his eyes widen"
            time.sleep(1)
            
        elif rog in ("red", "Red", "red button", "Red button", "the red button", "The red button"):
            button = 2
            print "Ignoring the instructions of the man strapped to the table, you press the red button"
            time.sleep(2)
            print ""
            print "Suddenly their bodies become limp and the monitors above them go dim"
            time.sleep(1.5)
            print "you check their pulse"
            time.sleep(1)
            print "."
            time.sleep(1)
            print "."
            time.sleep(1)
            print "."
            print "nothing..."
            time.sleep(2.5)
            print ""
            print "Suddenly, a door at the end of the room slides open and another"
            print "four armed creature walks into the room"
            time.sleep(2)
            print ""
            print "Upon seeing you and the now limp bodies strapped to the tables, his eyes widen"
            time.sleep(1.5)
            print "{What have you done?!}"
            time.sleep(1.5)
            print "{That was the only thing keeping them alive!}"
            print ""
            time.sleep(1)
        
    print "The creature grabs a syringe off of the table and begins to run towards you"
    sc = 0
    while sc == 0: 
        syringe = raw_input("Again you must make a quick decision: Attempt to reason with the creature, or Defend yourself with your crowbar? ")
        print ""
        if syringe in ("reason", "attempt to reason", "Reason", "Attempt to reason with the creature"):
            print "As you begin to explain that all you want is just to talk"
            print "the creature tackles you and injects you with whatever was in the syringe"
            print time.sleep(2)
            print ""
            over = raw_input("What do you do? ")
            print ""
            print "As you try, your vision begins to fade"
            time.sleep(1)
            print "."
            time.sleep(1)
            print "."
            time.sleep(1)
            print "."        
            print ""
            print "The world goes black"
            print ""
            script()
        elif syringe in ("Defend", "defend", "crowbar", "defend with crowbar", "defend yourself with your crowbar"):
            print "As the creature reaches you, a quick swing of your crowbar shatters it's hand."
            time.sleep(2)
            print ""
            print "As it writhes in pain, you take this opportunity to gain the 'upperhand'"
            time.sleep(3)
            print "You swing your crowbar several times against the creature's skull."
            time.sleep(1)
            print "WHAM"
            time.sleep(1)
            print "WHAM"
            time.sleep(1)
            print "CRACK"    
            print ""
            time.sleep(2)
            print "Breathing heavily, you're sure this thing is dead."
            time.sleep(2.5)
            print ""
            sc = 1
            
    if button == 1:
        print "The pair, again, thank you for setting them free"
        print "and run ahead through the door the creature came from."
    
    print "Surrounded by nothing but death, you decide theres nothing left but to head out this last door"
    print ""
    time.sleep(1)
    print "Slowly, you slide open the door and are blinded by the sun"
    print ""
    time.sleep(2)
    print "As your eyes adjust, you step out of the facility, covered in blood"
    print ""
    time.sleep(1.5)
    print "You look back; seeing a sign attached aboved the door..."
    time.sleep(1)
    print "."
    time.sleep(1)
    print "."
    time.sleep(1)
    print "."
    print ""
    print ""
    print "Vermont Psychiatric Hospital"
    time.sleep(1.5)
    print ""
    print "Intensive Care Unit"
    print ""
            










            
                        
        
script()
