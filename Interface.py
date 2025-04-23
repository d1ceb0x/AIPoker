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


def add_unique_card():
    new_card = generate_card()
    while new_card in cardCache:  # Regenerate if duplicate
        new_card = generate_card()
    cardCache.add(new_card)
    return new_card

#The river mechanics
def generate_river(iter, river=[]):
    if iter == 0:
        river = []
        r1 = add_unique_card()
        r2 = add_unique_card()
        r3 = add_unique_card()
        river.append(r1)
        river.append(r2)
        river.append(r3)
    if iter == 1:
        r4 = add_unique_card()
        river.append(r4)

    if iter == 2:
        r5 = add_unique_card()
        river.append(r5)
    return river

    

def print_river(river):
    print("====================================")
    print("The river:")
    for i in range(len(river)):
        print(f'\nCard {i+1}: {river[i].face} of {river[i].suite}')
    print("====================================")
c1 = add_unique_card() # add the first card
c2 = add_unique_card()#Keep regenrating until c2 is unique

#simple UI
print("====================================")
print("Your cards: \n")
print(f"Card 1: {c1.face} of {c1.suite}")
print(f"Card 1: {c2.face} of {c2.suite}")
print("====================================")

river = generate_river(0)
print_river(river)

iter = 1
user = input("Push or fold? ")

while user.lower() == "push" and iter <= 2:
    generate_river(iter, river)
    print_river(river)
    iter += 1
    user = input("Push or fold? ")

else:
    if len(river) <5: print("\nYou folded! Here is the full river")
    if len(river) == 3:
        generate_river(1, river)
        generate_river(2, river)
        print_river(river)

    if len(river) == 4:
        generate_river(2, river)
        print_river(river)
    
    



    






    