class HumanMage ():
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
    def HMFleshCombat (roll, combatPhase, playerHP, enemyHP, playerSkills, playerName, EnemyDamage, EnemyType):
        #Outter if statement for different interactions based on enemy type and ability used
        if EnemyType == 'Flesh':
            #Heat Pulse, strong against Flesh type
            if combatPhase.upper() == 'HP':  
                if roll == 10:
                    print ("\nThe attack from heat pulse overwhelms and critically strikes your foe, dealing massive damage!")
                    enemyHP -= playerSkills[combatPhase.upper()] * 3
                elif roll == 9:
                    print ("\nThe heat pulse overwhelms and critically strikes your foe, damage increased!")
                    enemyHP -= playerSkills[combatPhase.upper()] * 2.5
                elif roll == 8:
                    print ("\nThe heat pulse overwhelms and strikes your foe dealing extra damage!")
                    enemyHP -= playerSkills[combatPhase.upper()] * 2.0           
                elif roll == 7:
                    print ("\nThe heat pulse overwhelms and struck true!")
                    enemyHP -= playerSkills[combatPhase.upper()] * 1.5           
                elif roll == 6:
                    print ("\nThe enemy managed to partially block the blow, still feeling the heat of the pulse.")
                    enemyHP -= playerSkills[combatPhase.upper()] * 1.0            
                elif roll == 5:
                    print ("\nThe enemy managed to mitigate the impact of the heat pulse, but still sears.")
                    enemyHP -= playerSkills[combatPhase.upper()] * 0.5            
                elif roll == 4:
                    print ("\nThe attack was able to land searing the enemy, but not without a coutner attack from the enemy!")
                    enemyHP -= playerSkills[combatPhase.upper()] * 1.5
                    playerHP -= EnemyDamage * 0.5
                elif roll == 3:
                    print ("\nThe heat pulse barely seared the enemy, but the enemy countered with a solid blow!")
                    enemyHP -= playerSkills[combatPhase.upper()] * 1.0
                    playerHP -= EnemyDamage * 0.75
                elif roll == 2:
                    print ("You managed to clip your foe with heat, but were struck in the process!")
                    enemyHP -= playerSkills[combatPhase.upper()] * 0.75  
                    playerHP -= EnemyDamage * 0.75
                elif roll == 1:
                    print ("\nThe enemy dodged the attack and struck with a powerful counter attack.")
                    enemyHP -= playerSkills[combatPhase.upper()] * 0
                    playerHP -= EnemyDamage
        
        #Frost Lance, normal against Flesh type
            elif combatPhase.upper() == 'FL':  
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
            elif combatPhase.upper() == 'HFS':  
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
        
        
        
        #Sets enemy hp to 0 as opposed to a negative value
            if enemyHP < 0:
                enemyHP = 0
            print("\nThe enemy HP: ", enemyHP)
            print("\n" + playerName + " Hp: ", playerHP)
            return playerHP, enemyHP              
    
   