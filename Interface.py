import random
print("Welcome to poker")


class card: #simple class for a card
    def __init__(self, value, suite, nomen):
        self.value = value
        self.suite = suite
        self.nomen = nomen

    def __eq__(self, other):
        return self.value == other.value and self.suite == other.suite

def generate_card(): #function for generating cards

    suits = ['hearts', 'spades', 'diamonds', 'clubs']
    values = ['Ace'] + [str(i) for i in range(2, 11)] + ['Jack', 'Queen', 'King']

    
    card_index = random.randint(0, 51)
    suite = suits[card_index // 13]  
    value = values[card_index % 13]  
    return card(card_index % 13 + 1, suite, value)


    
    
cardCache = set() # set up a cache for cards
c1 = generate_card()
cardCache.add(c1) # add the first card
c2 = generate_card()
while c1.__eq__(c2):
    c2 = generate_card() #Keep regenrating until c2 is unique
cardCache.add(c2)
print("====================================")
print("Your cards: \n")
print(f"Card 1: {c1.nomen} of {c1.suite}")
print(f"Card 1: {c2.nomen} of {c2.suite}")
print("====================================")



 





    