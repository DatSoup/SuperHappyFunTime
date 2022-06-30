'''
This is my very first project that I have ever undertaken alone in programming. I am extremely excited and motivated to begin writting
This enchanting tale. My intention here Is to guide the player through a story that I have created. To start, the player will
select a race and a class. Leading on different journeys for each path (This will require a lot of time to properly build each path). 
The first path I am building is the dragonkin HexTinker. If you are interested in playing an early version this is where you will start!
'''
import random

#Basic combat for Dragonkin HexTinker
def DHCombatBasic (roll, combatPhase, playerHP, enemyHP, playerSkills, playerName, EnemyDamage):
    #Dragon breath combat
        if combatPhase.upper() == 'DB':  
                if roll == 10:
                        print ("\nThe attack from dragon breath critically strikes your foe, dealing massive damage!")
                        enemyHP -= playerSkills[combatPhase.upper()] * 2
                elif roll == 9:
                        print ("\nThe dragons breath critically strikes your foe, damage increased!")
                        enemyHP -= playerSkills[combatPhase.upper()] * 1.5
                elif roll == 8:
                        print ("\nThe dragon breath strikes your foe dealing extra damage!")
                        enemyHP -= playerSkills[combatPhase.upper()] * 1.25           
                elif roll == 7:
                        print ("\nThe dragon breath struck true!")
                        enemyHP -= playerSkills[combatPhase.upper()]            
                elif roll == 6:
                        print ("\nThe enemy managed to partially block the blow.")
                        enemyHP -= playerSkills[combatPhase.upper()] * 0.75            
                elif roll == 5:
                        print ("\nThe enemy managed to mitigate the impact of the dragon breath.")
                        enemyHP -= playerSkills[combatPhase.upper()] * 0.5            
                elif roll == 4:
                        print ("\nThe attack was able to land, but not without a coutner attack from the enemy!")
                        enemyHP -= playerSkills[combatPhase.upper()] * 1
                        playerHP -= EnemyDamage * 0.5
                elif roll == 3:
                        print ("\nThe dragon breath barely struck, but the enemy countered with a solid blow!")
                        enemyHP -= playerSkills[combatPhase.upper()] * 0.75
                        playerHP -= EnemyDamage * 0.75
                elif roll == 2:
                        print ("You managed to clip your foe, but were struck in the process!")
                        enemyHP -= playerSkills[combatPhase.upper()] * 0.5  
                        playerHP -= EnemyDamage * 0.75
                elif roll == 1:
                        print ("\nThe enemy dodged the attack and struck with a powerful counter attack.")
                        enemyHP -= playerSkills[combatPhase.upper()] * 0
                        playerHP -= EnemyDamage
            
#HexPulseGun combat
        elif combatPhase.upper() == 'HPG':  
                if roll == 10:
                        print ("\nThe attack from the HexPulseGun critically strikes your foe, dealing massive damage!")
                        enemyHP -= playerSkills[combatPhase.upper()] * 2
                elif roll == 9:
                        print ("\nThe HexPulse critically strikes your foe, damage increased!")
                        enemyHP -= playerSkills[combatPhase.upper()] * 1.5
                elif roll == 8:
                        print ("\nThe HexPulse critically strikes your foe, dealing extra damage!")
                        enemyHP -= playerSkills[combatPhase.upper()] * 1.25           
                elif roll == 7:
                        print ("\nThe HexPulse struck true!")
                        enemyHP -= playerSkills[combatPhase.upper()]            
                elif roll == 6:
                        print ("\nThe enemy managed to partially block the pulse.")
                        enemyHP -= playerSkills[combatPhase.upper()] * 0.75            
                elif roll == 5:
                        print ("\nThe enemy managed to block the majority of the HexPulse.")
                        enemyHP -= playerSkills[combatPhase.upper()] * 0.5            
                elif roll == 4:
                        print ("\nThe Pulse was able to land, but not without a ranged coutner attack from the enemy!")
                        enemyHP -= playerSkills[combatPhase.upper()] * 1
                        playerHP -= EnemyDamage * 0.5
                elif roll == 3:
                        print ("\nThe Pulse barely struck, but the enemy countered with a aimed shot!")
                        enemyHP -= playerSkills[combatPhase.upper()] * 0.75
                        playerHP -= EnemyDamage * 0.75
                elif roll == 2:
                        print ("\nYou managed to clip your foe, but were struck in the process!")
                        enemyHP -= playerSkills[combatPhase.upper()] * 0.5   
                        playerHP -= EnemyDamage * 0.75
                elif roll == 1:
                        print ("\nThe enemy dodged the attack and struck with precise ranged attack.")
                        enemyHP -= playerSkills[combatPhase.upper()] * 0
                        playerHP -= EnemyDamage
            
#DragonGlassHexBlade combat
        elif combatPhase.upper() == 'DGHB':  
                if roll == 10:
                        print ("\nThe attack from the DragonGlassHexBlade critically strikes your foe, dealing massive damage!")
                        enemyHP -= playerSkills[combatPhase.upper()] * 2
                elif roll == 9:
                        print ("\nThe DragonGlassHexBlade strikes your foe, damage increased!")
                        enemyHP -= playerSkills[combatPhase.upper()] * 1.5
                elif roll == 8:
                        print ("\nThe dragon DragonGlassHexBlade critically lands upon your foe dealing extra damage!")
                        enemyHP -= playerSkills[combatPhase.upper()] * 1.25           
                elif roll == 7:
                        print ("\nThe DragonGlassHexBlade struck true!")
                        enemyHP -= playerSkills[combatPhase.upper()]            
                elif roll == 6:
                        print ("\nThe enemy managed to partially block the blade.")
                        enemyHP -= playerSkills[combatPhase.upper()] * 0.75            
                elif roll == 5:
                        print ("\nThe enemy managed to mitigate the impact of the HexBlade.")
                        enemyHP -= playerSkills[combatPhase.upper()] * 0.5            
                elif roll == 4:
                        print ("\nThe attack was able to land, but not without a coutner attack from the enemy!")
                        enemyHP -= playerSkills[combatPhase.upper()] * 1
                        playerHP -= EnemyDamage * 0.5
                elif roll == 3:
                        print ("\nThe DragonGlassHexBlade barely struck, but the enemy countered with a solid blow!")
                        enemyHP -= playerSkills[combatPhase.upper()] * 0.75
                        playerHP -= EnemyDamage * 0.75
                elif roll == 2:
                        print ("\nYou managed to clip your foe, but were struck in the process!")
                        enemyHP -= playerSkills[combatPhase.upper()] * 0.5
                        playerHP -= EnemyDamage * 0.75
                elif roll == 1:
                        print ("\nThe enemy dodged the attack and struck with a powerful counter attack.")
                        enemyHP -= playerSkills[combatPhase.upper()] * 0
                        playerHP -= EnemyDamage

              
#Use of health pot
        elif combatPhase.upper() == 'CV': 
                if roll == 10:
                        print ("\nYou sense a deep flow of cosmic energy increasing its healing effect!")
                        playerHP += playerSkills[combatPhase.upper()] * 1.5
                elif roll == 9:
                        print ("\nYou tap into the cosmic vein and find an increased source of healing!")
                        playerHP += playerSkills[combatPhase.upper()] * 1.25
                elif roll == 8:
                        print ("\nYou tap into a cosmic vein and find it's full healing effect!")
                        playerHP += playerSkills[combatPhase.upper()] * 1.00           
                elif roll == 7:
                        print ("\nYou tap into the cosmic vein finding a solid pulse of healing")
                        playerHP += playerSkills[combatPhase.upper()] * 0.75            
                elif roll == 6:
                        print ("\nYou tap into a cosmic vein and sense only a mild pulse.")
                        playerHP += playerSkills[combatPhase.upper()] * 0.5            
                elif roll == 5:
                        print ("\nSensing for cosmic energy you are unable to find a healing pulse")
                        playerHP += 0
                elif roll == 4:
                        print ("\nThe enemy notices you tapping into the cosmic enery. Causing you to take some damage in return.")
                        playerHP -= playerSkills[combatPhase.upper()] * 0.75
                        playerHP -= EnemyDamage * 0.5
                elif roll == 3:
                        print ("\nThe enemy notices you tapping into the cosmic enery. Landing a partial blow")
                        playerHP += playerSkills[combatPhase.upper()] * 0.75
                        playerHP -= EnemyDamage * 0.75
                elif roll == 2:
                        print ("\nThe enemy strikes you while tapping into the cosmic energy ")
                        playerHP += playerSkills[combatPhase.upper()] * 0.5
                        playerHP -= EnemyDamage * 0.75
                elif roll == 1:
                        print ("\nYou sense no cosmic energy as the enemy lands a powerful strike.")
                        playerHP += playerSkills[combatPhase.upper()] * 0
                        playerHP -= EnemyDamage * 1.00                

#Sets enemy hp to 0 as opposed to a negative value
        if enemyHP < 0:
                enemyHP = 0
        print("\nThe enemy HP: ", enemyHP)
        print("\n" + playerName + " Hp: ", playerHP)
        return playerHP, enemyHP
        
#Starting the story        
def main():
        
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
#Player name input and setting inventory
                inventory = []
                playerName = input ("\n***What is your your name: ")
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
                enemyHP = 25
                EnemyDamage = 10
                playerSkills = {'DB': 20, 'HPG' : 15, 'DGHB' : 30}
                print("\nNow starts the combat phase, HexTinker starts with 3 skills DragonBreath (DB - racial), HexPulseGun (HPG - class), or DragonGlassHexBlade(DGHB - racial/class)")
                print("\nDragon Breath: This ability is known by all dragonkin. As children of the dragons, this trait was inherited as an icon of the dragons power."
                      "\nThis is a mid damage ability utilized from a mid range. This allows for decent damage with a decent chance of avoiding damage.")
                print("\nHexPulse Gun: Creation of the HexTinkers. This weapon fires a long range projectile pulse, powered by HexEnergy."
                      "\nThis is a lower damage ability utilized from a long range. This allows for minor damage with a high chance of avoiding damage.")
                print("\nDragonGlassHexBlade is a powerful weapon created by HexTinkers. With edges forged by dragon glass, HexEnergy power the blade to increase it power."
                      "\nThis is a high damage ability utilizied from low range. This allows for major damage with a low chance of avoiding damage.")
    
                print("\nYour starting HP is ", playerHP)
                print("Enemy HP is %d With a max damage output of %d" % (enemyHP, EnemyDamage))

#combat initiation
                while enemyHP > 0:
                        while True:
                                combatPhase = input('\n***Select an ability (DB, HPG, or DGHB): ')
                                if combatPhase.upper() not in ('DB', 'HPG', 'DGHB'):
                                        print("\nThat ability doesn't exist, please try again.")
                                else:
                                        break    
                        input ("\nCombat is about to begin, type 'roll' to initiate: ")
                        roll = random.randint(1, 10)
                        print ('\n' + playerName + " Rolled:", roll)
                        playerHP, enemyHP = DHCombatBasic (roll, combatPhase, playerHP, enemyHP, playerSkills, playerName, EnemyDamage)
                        if playerHP <= 0:
                                print("You have died, but the God's will not allow it...yet")
                                playerHP += 100
                                print("Forces beyond you understanding have chosen to give you life. playerHP = " + playerHP)

                                

#Post combat 1            
                print("\nYour enemy has been deafeated.")
                print("\nAs you approach the corpse you begin to notice this no creature you have seen before. It's body looked like bones held together by tough muscular sineu."
                      "Like some sort of demon.")
                print("\n\"Drak'Shir\" rumbled BarShoup")
                print("\n\"They are a race who live in caverns deep within the earth. Cavernous holes oozing with hot lava is where these monsters call home.\"")
                print("\n\"I thought they were all purged from this land during the great war. But I'll spare you the stories for now.")
                print("\n\"Be on your guard " + playerName + '. Lets go.\"')
                print("\n***Upon rummaging through the corpse, you found a strange medalion. Perhaps it holds some value")
                inventory.append('Drak\'Shir Medallion')
                print("Inventory: ", inventory)
                print("\n While running towards the mark of the gods the feeling of death and chaos fill the space around you. The images of flames dancing off the bronze structures illuminate the capital.")
                print("\n Wailing screams echo amongst the roaring of dragons. From the corner of you eye the great draconic behemoths rage through the city decimating Drak'Shir in waves of fire.")
                print("\n\"What is this madness? There are so many of them.\" BarShoup speaks with grimmace")
                print("\n A menacing cackle begins to permeate from the battlefield. You notice A flaming demonic figure of bone and torn flesh growing bigger within the dragons fire. As if it simply asorbed the flames of the great dragons.")
                print("\n\"Furnace Fiends.\" BarShoup spoke gravely")
                print("\n\"This is bad. Those monsters may be the greatest threat to dragon kind. " + playerName + " Hurry! We must protect the mark of the gods!")
                print("\nWinding through the corridors echoes grow and fade. The sounds of battles flowing in waves. Then suddly appeares the great bronze doorway, the entryway of the mark.")
                print("\n\"Where are the guards? DragonsBlight!\" Cursed BarShoup.")
                print("\nA furnace fiend ghoulish laugh rippled throughtout the air. Charred bones fell from his gaping maw.")
                print("\n\"The great ones should be protecting the mark through the door, quick " + playerName + " You most go to ensure the guardians still protect the mark! I'll be there soon, leave this pestilent creature to me.")
                print("\nHeading Barshoup word, you run towards the doors while you hear a Barshoup emminate a ferocious roar as he engaged the enemy")
                print("\nSuddenly, while approaching the door a drak'shir mercenary flanks you!")
                
#Second combat phase 
                enemyHP = 100
                EnemyDamage = 15
                print("\nYour HP is ", playerHP)
                print("Enemy HP is %d With a max damage output of %d" % (enemyHP, EnemyDamage))
                while True:
                        answer = input("\nWould you like to view your abilities?(Y/N): ")
                        if answer.upper() == 'Y':
                                print("\nSkill: ", playerSkills)
                                print("\nDragon Breath: This ability is known by all dragonkin. As children of the dragons, this trait was inherited as an icon of the dragons power."
                                      "\nThis is a mid damage ability utilized from a mid range. This allows for decent damage with a decent chance of avoiding damage.")
                                print("\nHexPulse Gun: Creation of the HexTinkers. This weapon fires a long range projectile pulse, powered by HexEnergy."
                                      "\nThis is a lower damage ability utilized from a long range. This allows for minor damage with a high chance of avoiding damage.")
                                print("\nDragonGlassHexBlade is a powerful weapon created by HexTinkers. With edges forged by dragon glass, HexEnergy power the blade to increase it power."
                                      "\nThis is a high damage ability utilizied from low range. This allows for major damage with a low chance of avoiding damage.")
                                break
                        elif answer.upper() == 'N':
                                break
                        else:
                                print("Please try again")
                
                while enemyHP > 0:
                        while True:
                                combatPhase = input('\n***Select an ability (DB, HPG, DGHB): ')
                                if combatPhase.upper() not in ('DB', 'HPG', 'DGHB'):
                                        print("\nThat ability doesn't exist, please try again.")
                                else:
                                        break    
                        input ("\nCombat is about to begin, type 'roll' to initiate: ")
                        roll = random.randint(1, 10)
                        print ('\n' + playerName + " Rolled:", roll)
                        playerHP, enemyHP = DHCombatBasic (roll, combatPhase, playerHP, enemyHP, playerSkills, playerName, EnemyDamage)
                        if playerHP <= 0:
                                print("You have died, but the God's will not allow it...yet")
                                playerHP += 100
                                print("Forces beyond you understanding have chosen to give you life. playerHP = " + playerHP)
                
                print("////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
                print("\nUpon defeating the enemy you turn towards the supernatural doors to the great mark.")
                print("\nSwirling with a potent energy, you hesitate as you approach the door.")
                print("\nMustering the courage you slowly push open the bronze doors to the halls of the Great mark.")
                print("\nAs you enter, the room swirls with cosmic energy. Constellations dance as reflections upon the jagged rocks filling the room.")
                print("\nWithin the center of the room, 3 ethereal dragons loom with their eyes closed.")
                print("\nEven though their eyes are closed, you can feel them staring at you. As if their own consciousness was some how pressing upon you mind.")
                print("\nBetween them, you see flickers of a glowing stone hidden through their shifting spirit like forms.")
                print("\n\"...Greetings, little dragon...\" Whispered a hoarse femenin voice")
                print("\n\"I am Moth'reza, mother of the dragons. Your heart must be pure to enter within those doors.\" She explained solemnly.")
                print("\n\"We feel the looming darkness crashing at the gates, perversly fighting to get to this rune by force.\" She mused.")
                print("\n\"Our power can hold the room for now, but I fear in time the enemy will penetrate our barrier. We can sense the growing evil of the forces waging against us.\"")
                print("\n\"Little dragon, we have but the power to spare to send you out to the boarders of this land. From here you must go forth in search for aid. Will you accept this calling to save our people?\" She spoke in a soft tone")
                
#The call to adventure
                answer2 = input("\n Will you accept the calling to save you people?(Y/N): ")
                if answer2.upper() == 'N':
                        print("\n\"Unfortunately little dragon, you are our only hope. You must go.")
                elif answer2.upper() == 'Y':
                        print("\n\"Thank you little dragon. We then bestow upon you our blessing before we send you on your way.\"")
                        print("\n***The celestial dragons have bestowed upon you their blessings. Your health has been restored and abilities have been enhanced.")
                        for key, val in playerSkills.items():
                                playerSkills[key] = val + 10
                else:
                        print("The celestial dragons grow inpatient of your indecisiveness. Try again.")
                
                print("\nSuddenly, the door opens again and you see BarShoup hurry in your direction.")
                print("\n\"Ah, BarShoup. It is good to see you again.\" Moth'reza spoke with a hint of excitment")
                print("\n\"It is an honor to be in your presence great ones.\" BarShoup exclaimed while kneeling before the celestial dragons.")
                print("\n\"Rise my child, time runs short. We will be sending you and " + playerName + " to the dragon cliff shores. Intercept the hidden lotus and go to the allied races for help.")
                print("\n\"Yes great mother.\" BarShoup spoke with a hint of pride.")
                print("\n\"Good, we will send you both now. Ah and before we forget. " + playerName + " you notice the ability to sense the cosmic veins around you now. This is apart of our blessing. Tap into this resource if you are ever in need of healing.\"")
                playerSkills.update({'CV' : 20})
                print("***You can now use the ability Cosmic Vein (CV) to enter a healing interaction while in combat")
                print("\nThe ground begins to swirl beneath you as a radiant cloud begins to slowly enshroud you in mist. Dancing cosmic energy sings with an unsettled song. As if it senses the the dark forces trying to subdue it.")
                print("\Within moments, the mist begins to fade and you stand at the edge of a massive cliff. Waves crashing far below you.")
                print("\n\"We will go now.\" BarShoup spoke swiftly")
                print("Then within moments you look onwards are BarShoup transforms into a massive greathawk.")
                print("\nGrabbing you with his talons BarShoup soares into the air flying into the dense mist covering the sea.")
                print("\n" + playerName + " We will now be heading to the hidden lotus. Our hidden jewel which protects our lands from outsider. I was once a scout for this ship. Prepare to prove yourself to the crew before they allow you to sail upon this vessel of legends.")
                print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
                print("\n")                
                        
        

#Paths not yet written    
        else:
                print("\nThis story has yet to be written, alas, you must select a different fate")
main()
