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
def is_pair(cards):
    """returns the value of the pair if found, else None"""
    count = {}
    for card in cards:
        count[card.value] = count.get(card.value, 0) + 1
    for value, freq in count.items():
        if freq == 2:
            return ([value] * 2, count)
    return (None, count)

def is_three(cards):
    """returns the value of the three of a kind if found, else None"""
    count = {}
    for card in cards:
        count[card.value] = count.get(card.value, 0) + 1
    for value, freq in count.items():
        if freq == 3:
            return ([value] * 3, count)
    return (None, count)

def is_four(cards):
    """returns the value of the four of a kind if found, else None"""
    count = {}
    for card in cards:
        count[card.value] = count.get(card.value, 0) + 1
    for value, freq in count.items():
        if freq == 4:
            return [value] * 4
    return (None, count)
def rank_hand(c1, c2, river):
    slots = sorted([c1, c2] + river, key=lambda x: x.value)
    full_house_check = set(([i for i in is_pair(slots)[1].keys() if is_pair(slots)[1][i]==2])).union(set(([j for j in is_three(slots)[1].keys() if is_three(slots)[1][j] == 3])))
    if (len(full_house_check) == 2):
        return "full house", full_house_check
    elif (res := is_four(slots)[0]):
        return "four of a kind", res
    elif (res := is_three(slots)[0]):
        return "three of a kind", res
    elif (res := is_pair(slots)[0]):
        return "pair", res
    return "nothing", []


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
    
c1 = card(13, "hearts", "King")
c2 = card(13, "spades", "King")

river = [
    card(13, "diamonds", "King"),  # Third King (Three of a Kind)
    card(1, "clubs", "Ace"),       # First Ace (Pair)
    card(1, "spades", "Ace")       # Second Ace (Completes Full House)
]
   
rank, res = rank_hand(c1, c2, river)
print(f'You had a {rank} which was {res}')


    






    