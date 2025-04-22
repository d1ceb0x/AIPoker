import random
print("Welcome to poker")

cardCache = set() #set up a cache for cards
class card: #simple class for a card
    def __init__(self, value, suite, face):
        self.value = value
        self.suite = suite
        self.face = face

    def __eq__(self, other):
        return self.value == other.value and self.suite == other.suite #comparison function
    def __hash__(self):
        return hash((self.value, self.suite)) ##hashing function

def generate_card(): #function for generating cards

    suits = ['hearts', 'spades', 'diamonds', 'clubs']
    values = ['Ace'] + [str(i) for i in range(2, 11)] + ['Jack', 'Queen', 'King']

    
    card_index = random.randint(0, 51)
    suite = suits[card_index // 13]  #assigning suites
    value = values[card_index % 13]  ##assigning values
    return card(card_index % 13 + 1, suite, value)


def add_card(card):
    if card not in cardCache:  
        cardCache.add(card)  # directly modifies the global set
    


c1 = generate_card()
add_card(c1) # add the first card
c2 = generate_card()
add_card(c2)#Keep regenrating until c2 is unique

#simple UI
print("====================================")
print("Your cards: \n")
print(f"Card 1: {c1.face} of {c1.suite}")
print(f"Card 1: {c2.face} of {c2.suite}")
print("====================================")



 





    