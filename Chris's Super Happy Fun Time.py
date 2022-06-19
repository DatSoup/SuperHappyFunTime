'''
This is my very first project that I have ever undertaken alone in programming. I am extremely excited and motivated to begin writting
This enchanting tale. My intention here Is to guide the player through a story that I have created. To start, the player will
select a race and a class. Leading on different journeys for each path (This will require a lot of time to properly build each path). 
The first path I am building is the dragonkin HexTinker. If you are interested in playing an early version this is where you will start!
'''
import random
print("Beyond the illusion of choice, lay a land of dreams and beauty. Select a path, and may your story begin.\n")

#Race selection
while True:
    Race = input("Select a race: Human, Orc, elf, dragonkin : ")
    if Race.lower() not in ('human', 'orc', 'elf', 'dragonkin'):
        print("That race doesn't exist, please try again.")
    else:
        break
    
print("\nA " + Race + ' eh? Quite good. What power does this ' + Race + ' posses?')

#Class selection   
while True:
    Class = input ("\nChose a class: Warrior, Mage, Warlock, Paladin, HexTinker: ")
    if Class.lower() not in ('warrior', 'mage', 'warlock', 'paladin', 'hextinker'):
        print("That class doesn't exist, please try again.")
    else:
        break
Race = Race.lower()
Class = Class.lower()
print ("\nA " + Race + " " + Class + ". So begins the journey...")

#Dragonkin/tinker story
if (Race, Class) == ('dragonkin', 'hextinker'):
    print("\nDeep within the heart of ocean exists an island shrouded in ominous fog. Snow peaked mountain ranges stretching for miles is all that can be seen."
          "\ndDeep within the mountains exists the capital known as Dragon's Nest. Here a young dragonkin HexTinker is hard at work within the HexTinker workshop."
          "\n\n\"You there. what is your name?\" A rough voice bellows")
    playerName = input ("\n***What is your your name: ") #name input
    print ("\n\"" + playerName + ","" hmph\"." + " exhaled the elderly dragonkin."
           "\n\n\"My name is BarShoup. I noticed you have been working far too long. Perhaps it's time to take a break from the hexCrafting.\""
           "\n\"How about a story. Would you like to learn about the origins of the dragonkin?\"")
    
    #dragonKin story selection
    while True:
        answer1 = input("\n***Would you like to hear the story of the dragonkin? (Y/N): ")
        if answer1.upper() == 'Y':
            print("\n\"Good. You have made the correct decision in learning of our heritage young one.\""
                  "\n\"Only in knowing your true identity will your purpose begin to reveal itself...\"")
            print("\n\"Long ago. In the ancient days of our ancestrals dragons, us dragonkins did not yet exist.\""
                  "\n\"During the age of dragons. Few dared to enter these mountains. Our ancestors were mercilous, beasts. Always looking to protect the mark of the gods.\""
                  "\n\"However, the allied races grew bold. The humans, orcs, and elves all came together under one banner to sail to this island and enter the mountains in search of resources.\""
                  "\n\"Thus was the beginning of the great war. Dragons echoing bellows instilled fear into the hearts of their enemies. Even united under the banner of the allied races, fear coursed through their veins.\""
                  "\n\"For months, the dragons fought viciously against the allied races. While fewer in number, the dragons were resilient. Hundreds of their enemies would die for every single dragon slain in battle.\""
                  "\n\"It wasn't until the dragons began to notice the intentions of the allied races did the fighting begin to slow. Our ancestors could not communicate with any living beings beside dragons.\""
                  "\n\"After many had died, and many grew weary of battle, the dragons decided to take a chance upon allied races."
                  "\n\"They decided to allow 1 member of each of the allied races to present themselves before the mark of the gods. Using’s its power, they were able to create the first dragonkin\""
                  "\n\"That is why we can communicate with all races within our world, it is our purpose.\""
                  "\n\"It is why we as dragonkin are here today as servants to the communications of this world. More important even then HexCr-…\"")
            break
            
        elif answer1.upper() == 'N':
            break
        else:
            print("\n \"I'm sorry young one I don't understand your response.\"")
    
     
    print("\nRoaring dragons and screeching comes rumbling through the corridors of the Dragons Nest.")   
    print("\n\"It's a call to arms... " + playerName + ", I'm heading to mark to ensure it's safe, follow me.\"")
    print("\nThe floor beneath you starts to shift. Boom! A cloaked figure jumped through the floor. Snarling blades in hand, a new battle lie ahead.")
    
   #commence first combat phase - player/enemy info
    playerHP = 100
    Enemy1HP = 25
    playerSkills = {'DB': 20, 'HPG' : 15, 'DGHB' : 30}
    print("\nNow starts the combat phase, HexTinker starts with 3 skills DragonBreath (DB - racial), HexPulseGun (HPG - class), or DragonGlassHexBlade(DGHB - racial/class)")
    print("Your starting HP is ", playerHP)
    print("Enemy HP is ", Enemy1HP)
    
    #combat initiation
    while Enemy1HP > 0:
        while True:
            combatPhase1 = input('\n***Select an ability (DB, HPG, or DGHB): ')
            if combatPhase1.upper() not in ('DB', 'HPG', 'DGHB'):
                print("\nThat ability doesn't exist, please try again.")
            else:
                break    
        input ("\nCombat is about to begin, type 'roll' to initiate: ")
        roll = random.randint(1, 10)
        print ('\n' + playerName + " Rolled:", roll)
        
#Dragon breath combat
        if combatPhase1.upper() == 'DB':  
            if roll == 10:
                print ("\nThe attack from dragon breath critically strikes your foe, dealing massive damage!")
                Enemy1HP -= playerSkills[combatPhase1.upper()] * 2
            elif roll == 9:
                print ("\nThe dragons breath critically strikes your foe, damage increased damage!")
                Enemy1HP -= playerSkills[combatPhase1.upper()] * 1.5
            elif roll == 8:
                print ("\nThe dragon breath strikes your foe dealing extra damage!")
                Enemy1HP -= playerSkills[combatPhase1.upper()] * 1.25           
            elif roll == 7:
                print ("\nThe dragon breath struck true!")
                Enemy1HP -= playerSkills[combatPhase1.upper()]            
            elif roll == 6:
                print ("\nThe enemy managed to partially block the blow.")
                Enemy1HP -= playerSkills[combatPhase1.upper()] * 0.75            
            elif roll == 5:
                print ("\nThe enemy managed to mitigate the impact of the dragon breath.")
                Enemy1HP -= playerSkills[combatPhase1.upper()] * 0.5            
            elif roll == 4:
                print ("\nThe attack was able to land, but not without a coutner attack from the enemy!")
                Enemy1HP -= playerSkills[combatPhase1.upper()] * 1
                playerHP -= 5
            elif roll == 3:
                print ("\nThe dragon breath barely struck, but the enemy countered with a solid blow!")
                Enemy1HP -= playerSkills[combatPhase1.upper()] * 0.75
                playerHP -= 7
            elif roll == 2:
                print ("You managed to clip your foe, but were struck in the process!")
                Enemy1HP -= playerSkills[combatPhase1.upper()] * 0.5  
                playerHP -= 7
            elif roll == 1:
                print ("\nThe enemy dodged the attack and struck with a powerful counter attack.")
                Enemy1HP -= playerSkills[combatPhase1.upper()] * 0
                playerHP -= 10
            print("\nThe enemy HP: ", Enemy1HP)
            print("\n" + playerName + " Hp: ", playerHP)
            
#HexPulseGun combat
        elif combatPhase1.upper() == 'HPG':  
            if roll == 10:
                print ("\nThe attack from the HexPulseGun critically strikes your foe, dealing massive damage!")
                Enemy1HP -= playerSkills[combatPhase1.upper()] * 2
            elif roll == 9:
                print ("\nThe HexPulse critically strikes your foe, damage increaased damage!")
                Enemy1HP -= playerSkills[combatPhase1.upper()] * 1.5
            elif roll == 8:
                print ("\nThe HexPulse critically strikes your foe, dealing extra damage!")
                Enemy1HP -= playerSkills[combatPhase1.upper()] * 1.25           
            elif roll == 7:
                print ("\nThe HexPulse struck true!")
                Enemy1HP -= playerSkills[combatPhase1.upper()]            
            elif roll == 6:
                print ("\nThe enemy managed to partially block the pulse.")
                Enemy1HP -= playerSkills[combatPhase1.upper()] * 0.75            
            elif roll == 5:
                print ("\nThe enemy managed to block the majority of the HexPulse.")
                Enemy1HP -= playerSkills[combatPhase1.upper()] * 0.5            
            elif roll == 4:
                print ("\nThe Pulse was able to land, but not without a ranged coutner attack from the enemy!")
                Enemy1HP -= playerSkills[combatPhase1.upper()] * 1
                playerHP -= 3
            elif roll == 3:
                print ("\nThe Pulse barely struck, but the enemy countered with a aimed shot!")
                Enemy1HP -= playerSkills[combatPhase1.upper()] * 0.75
                playerHP -= 5
            elif roll == 2:
                print ("\nYou managed to clip your foe, but were struck in the process!")
                Enemy1HP -= playerSkills[combatPhase1.upper()] * 0.5   
                playerHP -= 5
            elif roll == 1:
                print ("\nThe enemy dodged the attack and struck with precise ranged attack.")
                Enemy1HP -= playerSkills[combatPhase1.upper()] * 0
                playerHP -= 10
            print("\nThe enemy HP: ", Enemy1HP)
            print("\n" + playerName + " Hp: ", playerHP)
            
#DragonGlassHexBlade combat
        elif combatPhase1.upper() == 'DGHB':  
            if roll == 10:
                print ("\nThe attack from the DragonGlassHexBlade critically strikes your foe, dealing massive damage!")
                Enemy1HP -= playerSkills[combatPhase1.upper()] * 2
            elif roll == 9:
                print ("\nThe DragonGlassHexBlade strikes your foe, damage increased damage!")
                Enemy1HP -= playerSkills[combatPhase1.upper()] * 1.5
            elif roll == 8:
                print ("\nThe dragon DragonGlassHexBlade critically lands upon your foe dealing extra damage!")
                Enemy1HP -= playerSkills[combatPhase1.upper()] * 1.25           
            elif roll == 7:
                print ("\nThe DragonGlassHexBlade struck true!")
                Enemy1HP -= playerSkills[combatPhase1.upper()]            
            elif roll == 6:
                print ("\nThe enemy managed to partially block the blade.")
                Enemy1HP -= playerSkills[combatPhase1.upper()] * 0.75            
            elif roll == 5:
                print ("\nThe enemy managed to mitigate the impact of the HexBlade.")
                Enemy1HP -= playerSkills[combatPhase1.upper()] * 0.5            
            elif roll == 4:
                print ("\nThe attack was able to land, but not without a coutner attack from the enemy!")
                Enemy1HP -= playerSkills[combatPhase1.upper()] * 1
                playerHP -= 5
            elif roll == 3:
                print ("\nThe DragonGlassHexBlade barely struck, but the enemy countered with a solid blow!")
                Enemy1HP -= playerSkills[combatPhase1.upper()] * 0.75
                playerHP -= 7
            elif roll == 2:
                print ("\nYou managed to clip your foe, but were struck in the process!")
                Enemy1HP -= playerSkills[combatPhase1.upper()] * 0.5            
            elif roll == 1:
                print ("\nThe enemy dodged the attack and struck with a powerful counter attack.")
                Enemy1HP -= playerSkills[combatPhase1.upper()] * 0
                playerHP -= 10
            print("\nThe enemy HP: ", Enemy1HP)
            print("\n" + playerName + " Hp: ", playerHP)
            
#Use of health pot
        elif combatPhase1.upper() == 'HPPOT':
            playerHP += playerSkills['HPPOT']
            print("\nThe enemy HP: ", Enemy1HP)
            print("\n" + playerName + " Hp: ", playerHP)
            
#Post combat 1            
    print("\nYour enemy has been deafeated.")
    print("\nAs you approach the corpse you begin to notice this no creature you have seen before. It's body looked like bones held together by tough muscular sineu."
          "Like some sort of demon.")
    print("\n\"Drak'Shir\" rumbled BarShoup")
    print("\n\"They are a race who live in caverns deep within the earth. Cavernous holes oozing with hot lava is where these monsters call home.\"")
    print("\n\"I thought they were all purged from this land during the great war. But I'll spare you the stories for now.")
    print("\n\"Be on your guard " + playerName + '. Lets go.\"')
    playerSkills["HPPOT"] = 25
    print("\n***Upon rummaging through the corpse, you found a health pot.")
    print("\n While running towards the mark of the gods the feeling of death and chaos fill the space around you. The images of flames dancing off the bronze structures illuminate the capital.")
    print("\n Wailing screams echo amongst the roaring of dragons. From the corner of you eye the great draconic behemoths rage through the city decimating Drak'Shir in waves of fire.")
    print("\n\"What is this madness? There are so many of them.\" BarShoup speaks with grimmace")
    print("")
        

    
else:
    print("\nThis story has yet to be written, alas, you must select a different fate")
