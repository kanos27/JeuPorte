
class Personnage():
  # initiation avec mise en place de vie, ataque et peut-être inventaire
  def __init__(self, vie, atk):
    self.vie = vie
    self.atk = atk
    
  
  # fonction donnant les infos importantes sur le personnage demandé
  def __str__(self):
    return "" + str(self.vie) + "|" + str(self.atk)
    
  
  # fonction permetant d'obtenir la vie du personnage
  def getVie(self):
    return self.vie
  
  
  # fonction permetant d'obtenir l'attaque du personnage
  def getAtk(self):
    return self.atk
  
  
  # fonction d'attaque enlevant à la vie d'un personnage l'attaque d'un attaquant
  
  
  # fonction soignant le personnage grâce à sa vie et à la valeur du soin
  def healing(self, valHeal):
   self.vie = getVie() + valHeal
