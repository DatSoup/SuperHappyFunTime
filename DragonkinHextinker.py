class DragonkinHextinker ():
    '''
    def __init__(self, roll, combatPhase, playerHP, enemyHP, playerSkills, playerName, EnemyDamage):
        self.roll = roll
        self.combatPhase = combatPhase
        self.playerHP = playerHP
        self.enemyHP = enemyHP
        self.playerSkills = playerSkills
        self.playerName = playerName
        self.EnemyDamage = EnemyDamage
        '''
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
    
    
    #Use of cosmic vein
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
    
    def DHLotusFight (roll, combatPhase, playerHP, enemyHP, playerSkills, playerName, EnemyDamage): ###UPDATE this combat for uniqueness.
        #Dragon breath combat
        if combatPhase.upper() == 'DB':  
            if roll == 10:
                print ("\nThe attack from dragon breath critically strikes Gord'esh, dealing massive damage!")
                enemyHP -= playerSkills[combatPhase.upper()] * 2
            elif roll == 9:
                print ("\nThe dragons breath critically strikes Gord'esh, damage increased!")
                enemyHP -= playerSkills[combatPhase.upper()] * 1.5
            elif roll == 8:
                print ("\nThe dragon breath strikes Gord'esh dealing extra damage!")
                enemyHP -= playerSkills[combatPhase.upper()] * 1.25           
            elif roll == 7:
                print ("\nThe dragon breath struck true!")
                enemyHP -= playerSkills[combatPhase.upper()]            
            elif roll == 6:
                print ("\nGord'esh managed to partially block the blow.")
                enemyHP -= playerSkills[combatPhase.upper()] * 0.75            
            elif roll == 5:
                print ("\nGord'esh managed to mitigate the impact of the dragon breath.")
                enemyHP -= playerSkills[combatPhase.upper()] * 0.5            
            elif roll == 4:
                print ("\nThe attack was able to land, but not without a coutner attack from Gord'esh!")
                enemyHP -= playerSkills[combatPhase.upper()] * 1
                playerHP -= EnemyDamage * 0.5
            elif roll == 3:
                print ("\nThe dragon breath barely struck, but Gord'esh countered with a solid blow!")
                enemyHP -= playerSkills[combatPhase.upper()] * 0.75
                playerHP -= EnemyDamage * 0.75
            elif roll == 2:
                print ("You managed to clip Gord'esh, but were struck in the process!")
                enemyHP -= playerSkills[combatPhase.upper()] * 0.5  
                playerHP -= EnemyDamage * 0.75
            elif roll == 1:
                print ("\nGord'esh dodged the attack and struck with a powerful counter attack.")
                enemyHP -= playerSkills[combatPhase.upper()] * 0
                playerHP -= EnemyDamage
    
    #HexPulseGun combat
        elif combatPhase.upper() == 'HPG':  
            if roll == 10:
                print ("\nThe attack from the HexPulseGun critically strikes Gord'esh, dealing massive damage!")
                enemyHP -= playerSkills[combatPhase.upper()] * 2
            elif roll == 9:
                print ("\nThe HexPulse critically strikes Gord'esh, damage increased!")
                enemyHP -= playerSkills[combatPhase.upper()] * 1.5
            elif roll == 8:
                print ("\nThe HexPulse critically strikes Gord'esh, dealing extra damage!")
                enemyHP -= playerSkills[combatPhase.upper()] * 1.25           
            elif roll == 7:
                print ("\nThe HexPulse struck true!")
                enemyHP -= playerSkills[combatPhase.upper()]            
            elif roll == 6:
                print ("\nGord'esh managed to partially block the pulse.")
                enemyHP -= playerSkills[combatPhase.upper()] * 0.75            
            elif roll == 5:
                print ("\nGord'esh managed to block the majority of the HexPulse.")
                enemyHP -= playerSkills[combatPhase.upper()] * 0.5            
            elif roll == 4:
                print ("\nThe Pulse was able to land, but not without a ranged coutner attack from Gord'esh!")
                enemyHP -= playerSkills[combatPhase.upper()] * 1
                playerHP -= EnemyDamage * 0.5
            elif roll == 3:
                print ("\nThe Pulse barely struck, but Gord'esh countered with an aimed shot!")
                enemyHP -= playerSkills[combatPhase.upper()] * 0.75
                playerHP -= EnemyDamage * 0.75
            elif roll == 2:
                print ("\nYou managed to clip Gord'esh, but were struck in the process!")
                enemyHP -= playerSkills[combatPhase.upper()] * 0.5   
                playerHP -= EnemyDamage * 0.75
            elif roll == 1:
                print ("\nGord'esh dodged the attack and struck with precise ranged attack.")
                enemyHP -= playerSkills[combatPhase.upper()] * 0
                playerHP -= EnemyDamage
    
    #DragonGlassHexBlade combat
        elif combatPhase.upper() == 'DGHB':  
            if roll == 10:
                print ("\nThe attack from the DragonGlassHexBlade critically strikes Gord'esh, dealing massive damage!")
                enemyHP -= playerSkills[combatPhase.upper()] * 2
            elif roll == 9:
                print ("\nThe DragonGlassHexBlade strikes Gord'esh, damage increased!")
                enemyHP -= playerSkills[combatPhase.upper()] * 1.5
            elif roll == 8:
                print ("\nThe dragon DragonGlassHexBlade critically lands upon Gord'esh dealing extra damage!")
                enemyHP -= playerSkills[combatPhase.upper()] * 1.25           
            elif roll == 7:
                print ("\nThe DragonGlassHexBlade struck true!")
                enemyHP -= playerSkills[combatPhase.upper()]            
            elif roll == 6:
                print ("\nGord'esh managed to partially block the blade.")
                enemyHP -= playerSkills[combatPhase.upper()] * 0.75            
            elif roll == 5:
                print ("\nGord'esh managed to mitigate the impact of the HexBlade.")
                enemyHP -= playerSkills[combatPhase.upper()] * 0.5            
            elif roll == 4:
                print ("\nThe attack was able to land, but not without a coutner attack from Gord'esh!")
                enemyHP -= playerSkills[combatPhase.upper()] * 1
                playerHP -= EnemyDamage * 0.5
            elif roll == 3:
                print ("\nThe DragonGlassHexBlade barely struck, but Gord'esh countered with a solid blow!")
                enemyHP -= playerSkills[combatPhase.upper()] * 0.75
                playerHP -= EnemyDamage * 0.75
            elif roll == 2:
                print ("\nYou managed to clip Gord'esh, but were struck in the process!")
                enemyHP -= playerSkills[combatPhase.upper()] * 0.5
                playerHP -= EnemyDamage * 0.75
            elif roll == 1:
                print ("\nGord'esh dodged the attack and struck with a powerful counter attack.")
                enemyHP -= playerSkills[combatPhase.upper()] * 0
                playerHP -= EnemyDamage
    
    
    #Use of cosmic vein
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
                print ("\nGord'esh notices you tapping into the cosmic enery. Causing you to take some damage in return.")
                playerHP -= playerSkills[combatPhase.upper()] * 0.75
                playerHP -= EnemyDamage * 0.5
            elif roll == 3:
                print ("\nGord'esh notices you tapping into the cosmic enery. Landing a partial blow")
                playerHP += playerSkills[combatPhase.upper()] * 0.75
                playerHP -= EnemyDamage * 0.75
            elif roll == 2:
                print ("\nGord'esh strikes you while tapping into the cosmic energy ")
                playerHP += playerSkills[combatPhase.upper()] * 0.5
                playerHP -= EnemyDamage * 0.75
            elif roll == 1:
                print ("\nYou sense no cosmic energy as Gord'esh lands a powerful strike.")
                playerHP += playerSkills[combatPhase.upper()] * 0
                playerHP -= EnemyDamage * 1.00                
    
    #Sets enemy hp to 0 as opposed to a negative value
        if enemyHP < 0:
            enemyHP = 1
        elif playerHP < 0:
            playerHP = 1
        print("\nThe enemy HP: ", enemyHP)
        print("\n" + playerName + " Hp: ", playerHP)
        return playerHP, enemyHP            