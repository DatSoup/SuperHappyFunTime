'''
This is my very first project that I have ever undertaken alone in programming. I am extremely excited and motivated to begin writting
This enchanting tale. My intention here Is to guide the player through a story that I have created. To start, the player will
select a race and a class. Leading on different journeys for each path (This will require a lot of time to properly build each path). 
The first path I am building is the dragonkin HexTinker. If you are interested in playing an early version this is where you will start!
'''
import random
from DragonkinHextinker import *
from HumanMage import *
        
#Starting the story        
def main():
        
        print("Beyond the illusion of choice, lay a land of dreams and beauty. Select a path, and may your story begin.\n")

#Race selection
        while True:
                Race = input("Select a race: Human, Orc, elf, dragonkin : ")
                if Race.lower() not in ('human', 'orc', 'elf', 'dragonkin', 'battleZone'):
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
        print("////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        print ("\nA " + Race + " " + Class + ". So begins the journey...")

#Dragonkin/tinker story
        if (Race, Class) == ('dragonkin', 'hextinker'):
                print("\nDeep within the heart of ocean exists an island shrouded in ominous fog. Snow peaked mountain ranges stretching for miles is all that can be seen."
                      "\nWoven far within these mountains exists the capital known as Dragon's Nest. Here a young dragonkin HexTinker is hard at work within his workshop."
                      "\n\n\"You there. what is your name?\" A rough voice bellows")
#Player name input and setting inventory
                inventory = []
                playerName = input ("\n***What is your your name: ")
                print("////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
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
                                      "\n\"During the age of dragons, few dared to enter these mountains. Our ancestors were mercilous beasts. Always looking to protect the mark of the gods.\""
                                      "\n\"However, the allied races grew bold. The humans, orcs, and elves all came together under one banner to sail to this island and enter the mountains in search of resources.\""
                                      "\n\"Thus was the beginning of the great war. Dragons echoing bellows instilled fear into the hearts of their enemies. Even united under the banner of the allied races, fear coarsed through their veins.\""
                                      "\n\"For months, the dragons fought viciously against the allied races. While fewer in number, the dragons were resilient. Hundreds of their enemies would die for every single dragon slain in battle.\""
                                      "\n\"It wasn't until the dragons began to notice the intentions of the allied races did the fighting begin to slow. Our ancestors could not communicate with any living beings beside dragons.\""
                                      "\n\"After many had died and many grew weary of battle, the dragons decided to take a chance upon allied races."
                                      "\n\"They decided to allow 1 member of each of the allied races to present themselves before the mark of the gods. Using it's power, they were able to create the first dragonkin\""
                                      "\n\"This is why we can communicate with all races within our world. It is our purpose.\""
                                      "\n\"It is why we as dragonkin are here today as servants to the communications of this world. More important even then HexCr-…\"")
                                break
            
                        elif answer1.upper() == 'N':
                                break
                        else:
                                print("\n \"I'm sorry young one I don't understand your response.\"")
                input ("\n(press enter to continue)")
                print("////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
    
     
                print("\nRoaring dragons and screeching comes rumbling through the corridors of the Dragons Nest.")   
                print("\n\"It's a call to arms... " + playerName + ", I'm heading to mark to ensure it's safe, follow me.\"")
                print("\nThe floor beneath you starts to shift. Boom! A cloaked figure jumped through the floor. Snarling blades in hand, a new battle lie ahead.")
                        
    
   #commence first combat phase - player/enemy info
                playerHP = 100
                enemyHP = 25
                EnemyDamage = 10
                x = ''
                playerSkills = {'DB': 20, 'HPG' : 15, 'DGHB' : 30}
                print("\n---Now starts the combat phase, HexTinker starts with 3 skills DragonBreath (DB - racial), HexPulseGun (HPG - class), or DragonGlassHexBlade(DGHB - racial/class)---")
                print("\n-Dragon Breath: This ability is known by all dragonkin. As children of the dragons, this trait was inherited as an icon of the dragons power."
                      "\nThis is a mid damage ability utilized from a mid range. This allows for decent damage with a decent chance of avoiding damage.-")
                print("\n-HexPulse Gun: Creation of the HexTinkers. This weapon fires a long range projectile pulse, powered by HexEnergy."
                      "\nThis is a lower damage ability utilized from a long range. This allows for minor damage with a high chance of avoiding damage.-")
                print("\n-DragonGlassHexBlade is a powerful weapon created by HexTinkers. With edges forged by dragon glass, HexEnergy power the blade to increase it power."
                      "\nThis is a high damage ability utilizied from low range. This allows for major damage with a low chance of avoiding damage.-")
                input('\n(press enter to continue)')
    
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
                        playerHP, enemyHP, x = DragonkinHextinker.DHCombatBasic (roll, combatPhase, playerHP, enemyHP, playerSkills, playerName, EnemyDamage, x)
                        if playerHP <= 0:
                                print("You have died, but the God's will not allow it...yet")
                                playerHP += 100
                                print("Forces beyond you understanding have chosen to give you life. playerHP = " + playerHP)

                                

#Post combat 1            
                print("\nYour enemy has been deafeated.")
                print("\nAs you approach the corpse you begin to notice this no creature you have seen before. It's body looked like bones held together by tough muscular sineu."
                      " Like some sort of demon.")
                print("\n\"Drak'Shir\" rumbled BarShoup")
                print("\n\"They are a race who live in caverns deep within the earth. Cavernous holes oozing with hot lava is what these monsters call home.\"")
                print("\n\"I thought they were all purged from this land during the great war. But I'll spare you the stories for now.")
                print("\n\"Be on your guard " + playerName + '. Lets go.\"')
                print("\n***Upon rummaging through the corpse, you found a strange medalion. Perhaps it holds some value")
                inventory.append('Drak\'Shir Medallion')
                print("Inventory: ", inventory)
                input('(Press Enter to continue')
                print("////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
                print("\n While running towards the mark of the gods, the feeling of death and chaos fill the space around you. The images of flames dancing off the bronze structures illuminate the capital.")
                print("\n Wailing screams echo amongst the roaring of dragons. From the corner of you eye the great draconic behemoths rage through the city decimating Drak'Shir in waves of fire.")
                print("\n\"What is this madness? There are so many of them.\" BarShoup speaks with grimmace")
                print("\n A menacing cackle begins to permeate from the battlefield. You notice A flaming demonic figure of bone and torn flesh growing bigger within the dragons fire. As if it simply asorbed the flames of the great dragons.")
                print("\n\"Furnace Fiends.\" BarShoup spoke gravely")
                print("\n\"This is bad. Those monsters may be the greatest threat to dragon kind. " + playerName + ", hurry! We must protect the mark of the gods!")
                print("\nWinding through the corridors, echoes grow and fade. The sounds of battles flowing in waves. Then suddly appeares the great bronze doorway. The entryway of the mark.")
                print("\n\"Where are the guards? DragonsBlight!\" Cursed BarShoup.")
                print("\nA furnace fiend\'s ghoulish laugh rippled throughout the air. Charred bones fell from his gaping maw.")
                print("\n\"The great ones should be protecting the mark through the door. Quick, " + playerName + ". You must go to ensure the guardians still protect the mark! I'll be there soon, leave this pestilent creature to me.")
                print("\nHeading Barshoup\'s word, you run towards the doors while you hear Barshoup emminate a ferocious roar as he engaged the enemy")
                print("\nSuddenly, while approaching the door a drak'shir mercenary flanks you!")
                input('(Press Enter to continue')
                print("////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
                
#Second combat phase 
                enemyHP = 100
                EnemyDamage = 15
                x = ''
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
                                combatPhase = input('\n***Select an ability (DB, HPG, or DGHB): ')
                                if combatPhase.upper() not in ('DB', 'HPG', 'DGHB'):
                                        print("\nThat ability doesn't exist, please try again.")
                                else:
                                        break    
                        input ("\nCombat is about to begin, type 'roll' to initiate: ")
                        roll = random.randint(1, 10)
                        print ('\n' + playerName + " Rolled:", roll)
                        playerHP, enemyHP, x = DragonkinHextinker.DHCombatBasic (roll, combatPhase, playerHP, enemyHP, playerSkills, playerName, EnemyDamage, x)
                        if playerHP <= 0:
                                print("You have died, but the God's will not allow it...yet")
                                playerHP += 100
                                print("Forces beyond you understanding have chosen to give you life. playerHP = " + playerHP)
                
                input('(Press Enter to continue')
                print("////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
                print("\nUpon defeating the enemy, you turn towards the supernatural doors to the great mark.")
                print("\nSwirling with a potent energy, you hesitate as you approach the door.")
                print("\nMustering the courage you slowly push open the bronze doors to the halls of the Great mark.")
                print("\nAs you enter, the room swirls with cosmic energy. Constellations dance as reflections upon the jagged rocks filling the room.")
                print("\nWithin the center of the room, 3 ethereal dragons loom with their eyes closed.")
                print("\nEven though their eyes are closed, you can feel them staring at you. As if their own consciousness was some how pressing upon your mind.")
                print("\nBetween them, you see flickers of a glowing stone hidden through their shifting spirit like forms.")
                print("\n\"...Greetings, little dragon...\" Whispered a hoarse feminine voice")
                print("\n\"I am Moth'reza, mother of the dragons. Your heart must be pure to enter within those doors.\" She explained solemnly.")
                print("\n\"We feel the looming darkness crashing at the gates, perversly fighting to get to this rune by force.\" She mused.")
                print("\n\"Our power can hold the room for now, but I fear in time the enemy will penetrate our barrier. We can sense the growing evil of the forces waging against us.\"")
                print("\n\"Little dragon, we have but the power to spare to send you out to the boarders of this land. From here you must go forth in search for aid. Will you accept this calling to save our people?\" She spoke in a soft tone")

                
#The call to adventure
                answer2 = input("\n Will you accept the calling to save you people?(Y/N): ")
                if answer2.upper() == 'N':
                        print("\n\"Unfortunately little dragon, you are our only hope. You must go.")
                elif answer2.upper() == 'Y':
                        print("\n\"Thank you, little dragon. We now bestow upon you our blessing before we send you on your way.\"")
                        print("\n***The celestial dragons have bestowed upon you their blessings. Your health has been restored and abilities have been enhanced.")
                        for key, val in playerSkills.items():
                                playerSkills[key] = val + 10
                else:
                        print("The celestial dragons grow inpatient of your indecisiveness. Try again.")
                
                
                print("\nSuddenly, the door opens again and you see BarShoup hurry in your direction.")
                print("\n\"Ah, BarShoup. It is good to see you again.\" Moth'reza spoke with a hint of excitment.")
                print("\n\"It is an honor to be in your presence great ones.\" BarShoup exclaimed while kneeling before the celestial dragons.")
                print("\n\"Rise my child, time runs short. We will be sending you and " + playerName + " to the dragon cliff shores. Intercept the hidden lotus and go to the allied races for help.")
                print("\n\"Yes, Great Mother.\" BarShoup spoke with pride.")
                print("\n\"Good, we will send you both now. Ah, and before we forget, " + playerName + ", you will notice the ability to sense the cosmic veins around you now. This is a part of our blessing. Tap into this resource if you are ever in need of healing.\"")
                playerSkills.update({'CV' : 20})
                print("***You can now use the ability Cosmic Vein (CV) to enter a healing interaction while in combat")
                input('(Press Enter to continue')
                print("////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
                print("\nThe ground begins to swirl beneath you as a radiant cloud begins to slowly enshroud you in mist. Dancing cosmic energy sings with an unsettled song. As if it senses the the dark forces trying to subdue it.")
                print("Within moments, the mist begins to fade and you stand at the edge of a massive cliff. Waves crashing far below you.")
                print("\n\"We must go now.\" BarShoup speaks swiftly")
                print("\nLooking onwards, you notice that within moments BarShoup transforms into a massive greathawk.")
                print("\nGrabbing you with his talons, BarShoup soares into the air flying into the dense mist covering the sea.")
                print("\n" + playerName + ", we will now be heading to the hidden lotus. It is our jewel which protects our lands from outsider. I was once a scout for this ship. Prepare to prove yourself to the crew before they allow you to sail upon this vessel of legends.")
                input('(Press Enter to continue')
                print("////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
#The Hidden Lotus
                print("\n")   
                print("\nAfter what felt like hours of soaring through the misty clouds above the water you hear a screaching wail rapidly approaching.")
                print("\nWithin seconds you feel a jolt as Bar'Shoup whips around to face the eminating screeching. Then, BarShoup let loose a deep bellowing tone.")
                print("\nRythmic and strong. The sound pulsed with a friendly, yet ferocious vibraton. When Bar'Shoup was finished, the mysterious figure replied with the same melodic tone. Looking up, you notice he too was a greathawk.")
                print("\n\"Gord'esh!\" BarShoup called out. \"Good to see you serving the Lotus honorably.\"")
                print("\n\"BarShoup! What bring you all the way out here?\" Also, who is that with you? Gord'esh spoke dicerningly.")
                print("\n\"Bad news from the Dragon's Nest. The HexTinker is with me. I'll explain on the Lotus, take us there.\"")
                print("\n\"With all due respect. You know the rules of the lotus, no one is allowed onboard unless they've proven themeselves worthy.\" Gord'esh spoke sternly." )
                print("\n\"The mark of the God's is in danger, the Drak'Shir have returned. We have been sent on behalf of the celestial dragon's. The HexTinker isn't here to joing the crew, they will fight for the right to board. I will respect the tradition, but we've no time to waste\" BarShoup spoke gravely.")
                print("\n\"The mark is in danger? Damnation.\" cursed Gord'esh. \"Follow me.\"")
                print("\nA few minutes later a ship appeares in the distance. With a hull formed of reflective dragon glass it cut through the water without making a sound, barely visible to the naked eye from a distance. Its mast was a haze grey, subtly shifting its colot to blend with the passing mists.")
                print("\n\"It has been a long while.\" Bar'Shoup spoke nastolgically. \"I used to serve as a scout on this ship, before leaving I personally took Gord'esh under my wing and trained him. As a fellow druid, a scout's role fit us best onboard.")
                print("\n\"You will have to face him in combat in order to board the ship. The hidden lotus is responsible for protecting our shores from outsiders, this is accomplished by only allowing those truly worthy to join the crew.")
                print("\n\"Since you aren't joining the crew, you will need to merely prove your salt in combat to ensure you won't be a liability on the ship. He wont go all out, but don't get complacent. He wont be a push over")
                print("\n\"Upon approaching the ship you see a stir upon the decks. As you get closer, you hear people calling out and cheering for the return of BarShoup.")
                print("\n\"My friends! it's good to see you all. BarShoup exclaimed.")
                print("\nBarShoup!\" Boomed a commanding voice. \"What brings you here, and who is this stow away in you pocession?\"")
                print("\n\"Captain Karmada!\" BarShoup spoke with a salute. \"We were sent by the celestial dragons. The Drak'shir are back and they are after the mark of the Gods.\"")
                print("\n\"This is " + playerName + ", as fate would have it we met right before the invasion. "+ playerName + " fought with me as we ventured through that hellscape to the Great hall.\"")
                print("\n\"I see. Then it appears we must have a chat\" Spoke the captain calmly.")
                print("\n\"Welcome to the hidden Lotus " +playerName + ". We will need to see what you are made of for you to spend time on this ship. Very few people ever set foot on this ship who are not crew members or captives.\" He said with a sense of caution.")
                print("\n\"It appears you have already met Gord'esh. He will be administering the test. Gord'esh!\" He yelled sharply.")
                print("\n\"Yes sir.\" Gord'esh replied." )
                input('(Press Enter to continue')
                print("////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
                
#Hidden Lotus Combat                
                enemyHP = 200
                EnemyDamage = 45
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
                                print("\nCosmic Vein: This ability allows you to tap into cosmic veins around you to heal while in combat."
                                      "\nDepending on if you can find the cosmic flow through a vein (based off role), you may or may not be able to heal.")
                                break
                        elif answer.upper() == 'N':
                                break
                        else:
                                print("Please try again")                
                while enemyHP > 1:
                        while True:
                                combatPhase = input('\n***Select an ability (DB, HPG, DGHB, CV): ')
                                if combatPhase.upper() not in ('DB', 'HPG', 'DGHB', 'CV'):
                                        print("\nThat ability doesn't exist, please try again.")
                                else:
                                        break    
                        input ("\nCombat is about to begin, type 'roll' to initiate: ")
                        roll = random.randint(1, 10)
                        print ('\n' + playerName + " Rolled:", roll)
                        playerHP, enemyHP, x = DragonkinHextinker.DHLotusFight (roll, combatPhase, playerHP, enemyHP, playerSkills, playerName, EnemyDamage, x)
                        if playerHP <= 1:
                                print("\nYou have been defeated")
                        elif enemyHP <= 1:
                                print("\nGord'esh has been defeated")
                                inventory.append("LotusCoin")
                                print("You recieved a Lotus Coin from Gord'esh, this coin holds a unique value for its rarity.")
                
                input('(Press Enter to continue')
                print("////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")                
                print("\n\"Well done.\" Spoke captain Karmada surely.")
                print("\n\"You two go to medical to treat your wounds. Bar'Shoup, come with me. Lets have a chat. Welcome aboard " + playerName + ".")
                playerHP = 100
                
                
                print("\n\"The lotus has never before left the shores of Var'Nesh. I'd imagine most beings outside of this country still rumor this ship to be only a legend.\" Captain Karmada mused.")
                print("\n\"If the Great Ones will, then we set sail for the shores of Essteria.\" He spoke again surely.")
                print("\n\"It will be an honor to sail amongst this ship once again.\" BarShoup exclaimed with pride.")
                print("\n\"It will be a blessing to have you back for this voyage. I have a feeling an experienced scout with first hand experience of the plague infecting this world will be paramount in persuading the allied races.\"")
                print("\n\"You may go now now BarShoup. I will inform the crew. We set sail immediatly.")
                print("\nA few moments later a bell begins to chime. Sending waves of sound coursing through the ship.")
                print("\nA stacticy, yet sharp voice then followed, \"Good evening Lotus crew, this is captain Karmada speaking.\"")
                print("\n\"I'm sure the rumors have already begun, and I am here to shed light on what is occuring.\" He spoke with a troubled confidence.")
                print("\n\"The Drak'Shir have returned. They have invaded the Dragon's Nest and hunt for the Great Mark.\"")
                print("\n\"The Great Ones power still protect the chamber, but we must make haste to Essteria to rally the allied races.\"")
                print("\n\"This will be the maiden voyage of the hidden lotus across the sea. Prepare the ship, it's time for us to take swift action in defense of our world.\"")
                print("\nFollowed by three piercing whistles the communication became silent as the crew lept into action as if this had been the plan all along. Without question, or hesitation, the crew began preparing the ship.")
                print("\nWhile in the medical facilities, you see BarShoup swing through the corridor. \"" + playerName + "I take it you understand the current situation. I will take to the sky and patrol the sea with Gor'Desh.\" He explained")
                print("\n\"I recommed you take to the deck and aid crew however you can. The seas can be a cruel and unforgiving mistress. Be prepared for anything, at any time.\" BarShoup spoke with a stern voice.")
                print("\nAs you approach the deck, the light overwhelms you senses. Causing you to squint. However, after a few moments of adjusting you begin to feel the exhileration of sailing the sea.")
                print("\nThe heavy winds whip across the deck as the ship begins to slice through the sea at top speeds. The smell of the salty ocean air arouses a deep sensation of joy.")
                print("\nBut as time begins to pass an ominous begins to form in the distance. You begin to sense a hint of trepidation wash over the crew like an tidal wave.")
                print("\n\"Sea sprits.\" a crew member said with a curse.")
                print("\nNot a moment later you see Gor'Desh flying towards the ship. With a scream he yells, \"BarShoup has engaged the sea sprits, prepare to fight!")
                print("\nThen, through crashing lightening you see BarShoup fighting a massive serpentine like water spirit flying through the air.")
                print("\n\"The sprits are savage elemental creatures who destroy everything in their path. They camoflouge over the water and strike in an instant. Be ready.\" A crewmember said with a hint of excitement.")
                print("\nThen, following a flash of lightening overhead a water like form coaleses infront of you as if willed by the wind itself. The mishshapen human-like creature then lunges at you with a blade of pure lightening!")
                input('(Press Enter to continue')
                print("////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
#Sea Sprit combat
                enemyHP = 135
                EnemyDamage = 30
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
                                print("\nCosmic Vein: This ability allows you to tap into cosmic veins around you to heal while in combat."
                                      "\nDepending on if you can find the cosmic flow through a vein (based off role), you may or may not be able to heal.")
                                break 
                        elif answer.upper() == 'N':
                                break
                        else:
                                print("Please try again") 
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
                        playerHP, enemyHP, x = DragonkinHextinker.DHCombatBasic (roll, combatPhase, playerHP, enemyHP, playerSkills, playerName, EnemyDamage, x)
                        if playerHP <= 0:
                                print("You have died, but the God's will not allow it...yet")
                                playerHP += 100
                                print("Forces beyond you understanding have chosen to give you life. playerHP = " + playerHP)     
                print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
                print("\nUpon defeating the sprit you find a rock shaped trinket which is shaped exactly as the sprite was")
                print("\n\"A sprite core, its energy will reinforce you. As nasty as these creatures are their remains do hold value. Embrace your first kill against a sprit.\" Mentioned the crewmember.")
                print("\n\"The names Broxy by the way. I'm a simple HexTinker like yourself. Here is a holster which can harness the power latent in a sprit core, allowing you to benefit from it. Pleased to meet you" + playerName + ".\"")
                inventory.append("sprite core")
                inventory.append("sprite core harness")
                print("Upon placing the core in the harness you feel your vitality increase. ***PlayerHP increased by 100***")
                playerHP = 200
                input('(Press Enter to continue')
                print("////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
                print("\nFollowing the battle you hear that now firmiliar sound of bells echoing across the deck.")
                print("\n\"This is your captain speaking. Good work everyone, initial reports show no lives were lost and injuries were minor.\"")
                print("\"We have again proved our ability to easily outmatch the sea sprites. Be on guard however, this is only the beginning of our voyage across the sea.\"")
                print("The message was followed with a simple click. \"You look confused.\" Mused Broxy. \"Ahh, it's the tones you don't understand. Different messages have different tones at the end to inform us on the crew what is expected of us.\"")
                print("\n\"The simple click is indicative of a call ending. No action required. The three whistles you heard before indicate an emergency situation which we are all trained to respond to.\"")
                print("\n\"It's good to see you are worth your salt in battle. I hear that you too are a HexTinker, no? Perhaps we can work together while we voyage to Essteria.")
                print("\nFrom the skies above you hear a roaring laughter approach. \"Ah, it feels good to battle in the skys above the sea once again!\" BarShoup roared as he flew past the deck of the lotus.")
                print("\n\"He sure seems happy.\" Broxy laughed. \"Although I didn't know BarShoup for long, he is a legend even amongst those who sail upon this ship. Few have voyaged to Essteria to earn there way onto this ship. His journy was a perticularly perilous one.")
                
                
        

#Paths not yet written  
        elif (Race, Class) == ('human', 'mage'):
                print("\nAlong the coast of the Manus sea exists the capital city Oceanus."
                      "\nIts Adorned in colors of ivory accented with bluish green hues, iconic spiraling towers inspire awe to those who look upon them. Casting icredible views"
                      "\nof the ocean and Vulcanus isles from the upper spires. Within one of these spires a group of mages work diligintley on plans for the grand arcane elevators"
                      "\n\n\"You there. what is your name?\" A soft voice echoes")
#Player name input and setting inventory
                inventory = []
                playerName = input ("\n***What is your your name: ")
                print ("\n\"" + playerName + ","" hmph\"." + " exhaled the elderly mage."
                       "\n\n\"You must be new here at the arcanum. " + playerName + "Are you familiar with the purpose of our elevator designs based off the purposes of out city?\""
                       "\n\"I am one of the lead magengineers, Arduna. I'd be happy to update you on our work here.\"")
    
#human mage story selection
                while True:
                        answer1 = input("\n***Would you like to hear the story of the city? (Y/N): ")
                        if answer1.upper() == 'Y':
                                print("\n\"Wonderful! As you may already know our city is split into two tiers.\""
                                      "\n\"The purpose of the upper tier is obvious. It runs and operates like any other major city.\"")
                                print("\n\"The lower tier however, approximately 200 feet off the cliff is the most important part of this city.\""
                                      "\n\"Down there lies the shipyards which haul minerals from the main island back to our city.\""
                                      "\n\"In addition, the ruling elite of our city are very pompous about their nauticals voyaging. Massive ships fill the harbor as well to the North, with the shipyards and mineral deposts to the South.\""
                                      "\n\"As you might image, it takes extrodanary amounts of energy for us to operate lifts carrying all of those minerals and ships parts up and down the cliff. As well as people in the public lift.\""
                                      "\n\"Along with that, comes engineering suited best to weilders of arcane energy as ourselves.\""
                                      "\n\"Albiet most of us can tap into other powers, the arcane energy can interact with matter as energy without damaging it.\""
                                      "\n\"This is the way we work together in order to properly continue operations of the lift."
                                      "\n\"Now, allow me to put you to work within the arcane energy, please follow me...\"")

                                break
            
                        elif answer1.upper() == 'N':
                                break
                        else:
                                print("\n \"I'm sorry young one I don't understand your response.\"")
                

                        print("\nSuddenly, an alarm begins echoing throughout the land.")   
                        print("\n\"The defense siren? They didn't announce a test today. " + playerName + ", I'm going to the overlook to see what is going on. Follow if you would like.\" Spoke Arduna cautiously")
                        print("\nAs the door to the overlook opens the immense beauty of the vulcanaus isles is stark against the twinkling sea. Then suddenly a dark, cloaked figure crawls and leaps atop the platform!")
                        print("\nSensing the malicious intent you must prepare to fight.")
                input('(Press Enter to continue')
                print("////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
    
   #commence first combat phase - player/enemy info
                playerHP = 100
                enemyHP = 25
                EnemyDamage = 10
                EnemyType = 'Flesh'
                playerSkills = {'FL': 15, 'HP' : 15, 'HFS' : 30}
                print("\nNow starts the combat phase, Mages starts with 3 skills Frost Lance (FL - Utilizing frost damage), HeatPulse (HP - Utilizing arcane bursts of heat), or HeatFrostSword(HFS - Infusing a sharp blade of ice with radient heat to empower it)")
                print("\nFrostLance: This ability utilizes magic to form a lance of frost, this trait was inherited through mage blood."
                      "\nThis is a ranged damage ability. This allows for decent damage with a decent chance of avoiding damage. It will deal more damage to enemies susceptible to cold and less to those who are cold adapted")
                print("\nHeatPulse: Channeling arcane energy, This ability fires a pulse of pure heat energy at the opponent."
                      "\nThis is a ranged damage ability. This allows for decent damage with a decent chance of avoiding damage.")
                print("\nHeatFrostSword is a powerful magic utilized by mages. It requires incredible skill to form a blade of ice and empower it with incredible heat energy without melting it."
                      "\nThis is a high damage ability utilizied from low range. This allows for major damage with a low chance of avoiding damage.")
                
                print("\nYour starting HP is ", playerHP)
                print("Enemy HP is %d With a max damage output of %d" % (enemyHP, EnemyDamage))
                #initiate combat
                while enemyHP > 0:
                        while True:
                                combatPhase = input('\n***Select an ability (FL, HP, or HFS): ')
                                if combatPhase.upper() not in ('FL', 'HP', 'HFS'):
                                        print("\nThat ability doesn't exist, please try again.")
                                else:
                                        break    
                        input ("\nCombat is about to begin, type 'roll' to initiate: ")
                        roll = random.randint(1, 10)
                        print ('\n' + playerName + " Rolled:", roll)
                        playerHP, enemyHP = HumanMage.HMFleshCombat (roll, combatPhase, playerHP, enemyHP, playerSkills, playerName, EnemyDamage, EnemyType)
                        if playerHP <= 0:
                                print("You have died, but the God's will not allow it...yet")
                                playerHP += 100
                                print("Forces beyond you understanding have chosen to give you life. playerHP = " + playerHP)   
                print("\nYour enemy has been deafeated.")
                print("\nAs you slowly walk towards the fallen figure you quickly notice mucusy flesh hanging loosly over raw muscle and bone. A dark creature you have never seen before.")
                print("\n\"What in the high heavens is that!\" Arduna cursed.")
                print("\n\"In all my years I have never seen such a vile creature.\" He spat.")
                print("\n\"Stay here and watch the body " + playerName + '\"I will go and retrieve the guards. We must find out what is going on here.')
                print('\nIn a moment of stillness you drink in the peace staring out at the sea. Following the thrill of battle a peace washes over you. Perhaps the body holds any items of value. ')
                print("\n***Upon rummaging through the corpse, you found a strange medalion. Perhaps it holds some value")
                inventory.append('Drak\'Shir Medallion')
                print("Inventory: ", inventory)
                input('(Press Enter to continue)')
                print("////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")   
        elif (Race, Class) == ('battlezone', 'mage'):
                round = 0
                playerHP = 100
                enemyHP = 25
                EnemyDamage = 10
                EnemyType = 'Flesh'
                playerSkills = {'FL': 15, 'HP' : 15, 'HFS' : 30}
                print("\nNow starts the combat phase, Mages starts with 3 skills Frost Lance (FL - Utilizing frost damage), HeatPulse (HP - Utilizing arcane bursts of heat), or HeatFrostSword(HFS - Infusing a sharp blade of ice with radient heat to empower it)")
                print("\nFrostLance: This ability utilizes magic to form a lance of frost, this trait was inherited through mage blood."
                      "\nThis is a ranged damage ability. This allows for decent damage with a decent chance of avoiding damage. It will deal more damage to enemies susceptible to cold and less to those who are cold adapted")
                print("\nHeatPulse: Channeling arcane energy, This ability fires a pulse of pure heat energy at the opponent."
                      "\nThis is a ranged damage ability. This allows for decent damage with a decent chance of avoiding damage.")
                print("\nHeatFrostSword is a powerful magic utilized by mages. It requires incredible skill to form a blade of ice and empower it with incredible heat energy without melting it."
                      "\nThis is a high damage ability utilizied from low range. This allows for major damage with a low chance of avoiding damage.")
                
                print("\nYour starting HP is ", playerHP)
                print("Enemy HP is %d With a max damage output of %d" % (enemyHP, EnemyDamage))
                #initiate combat
                while enemyHP > 0:
                        while True:
                                combatPhase = input('\n***Select an ability (FL, HP, or HFS): ')
                                if combatPhase.upper() not in ('FL', 'HP', 'HFS'):
                                        print("\nThat ability doesn't exist, please try again.")
                                else:
                                        break    
                        input ("\nCombat is about to begin, type 'roll' to initiate: ")
                        roll = random.randint(1, 10)
                        print ('\n' + playerName + " Rolled:", roll)
                        playerHP, enemyHP = HumanMage.HMFleshCombat (roll, combatPhase, playerHP, enemyHP, playerSkills, playerName, EnemyDamage, EnemyType)
                        if playerHP <= 0:
                                print ('You are dead, you got to round ', round)
                round +=1 
        else:
                print("\nThis story has yet to be written, alas, you must select a different fate")
main()