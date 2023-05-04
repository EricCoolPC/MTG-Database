class Card:
    def __init__(self,name,manaCost,cmc,types,cardText,flavorText,powerToughness,expansion,rarity):
        self.name = name
        self.manaCost = manaCost
        self.cmc = cmc
        self.types = types
        self.cardText = cardText
        self. flavorText = flavorText
        self.powerToughness = powerToughness
        self.expansion = expansion
        self.rarity = rarity

    def Print_Stuff (self) :
        print (self.name)
        print (self.flavorText)