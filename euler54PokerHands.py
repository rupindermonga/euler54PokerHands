'''
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD
Pair of Fives
 	2C 3S 8S 8D TD
Pair of Eights
 	Player 2
2	 	5D 8C 9S JS AC
Highest card Ace
 	2C 5C 7D 8S QH
Highest card Queen
 	Player 1
3	 	2D 9C AS AH AC
Three Aces
 	3D 6D 7D TD QD
Flush with Diamonds
 	Player 2
4	 	4D 6S 9H QH QC
Pair of Queens
Highest card Nine
 	3D 6D 7H QD QS
Pair of Queens
Highest card Seven
 	Player 1
5	 	2H 2D 4C 4D 4S
Full House
With Three Fours
 	3C 3D 3S 9S 9D
Full House
with Three Threes
 	Player 1
The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
'''

'''
def noPair(n):
    result = False
    number_hand = creatingListNumber(n)[0]
    if len(set(number_hand)) == 4:
        result = True
    return result
'''
'''
def aPair(n):
    # n is the list of poker hand
    result = False
    number_hand = creatingListNumber(n)[0]
    if len(set(number_hand)) == 4:
        result = True
    return result

def twoPairs(n):
    # n is the list of poker hand
    result = False
    number_hand = creatingListNumber(n)[0]
    if len(set(number_hand)) == 3 and most_frequent(number_hand) == 2:
        result = True
    return result




def threeKind(n):
    # n is the list of poker hand
    result = False
    number_hand = creatingListNumber(n)[0]
    if len(set(number_hand)) == 3 and most_frequent(number_hand) == 3:
        result = True
    return result

def straight(n):
    result = False
    number_hand = creatingListNumber(n)[0]
    suit_hand = creatingListNumber(n)[1]
    if sorted(number_hand) == list(range(min(number_hand), max(number_hand)+1)) and len(set(suit_hand)) != 1:
        result = True  
    return result

def Flush(n):
    suit_hand = creatingListNumber(n)[1]
    number_hand = creatingListNumber(n)[0]
    result = False
    if len(set(suit_hand)) == 1 and sorted(number_hand) != list(range(min(number_hand), max(number_hand)+1)):
        result = True
    return result

def FullHouse(n):
    result = False
    number_hand = creatingListNumber(n)[0]
    if len(set(number_hand)) == 2 and most_frequent(number_hand) == 3:
        result = True
    return result

def FourKind(n):
    result = False
    number_hand = creatingListNumber(n)[0]
    if len(set(number_hand)) == 2 and most_frequent(number_hand) == 4:
        result = True
    return result

def straightFlush(n):
    result = False
    number_hand = creatingListNumber(n)[0]
    suit_hand = creatingListNumber(n)[1]
    if sorted(number_hand) == list(range(min(number_hand), max(number_hand)+1)) and len(set(suit_hand)) == 1:
        result = True  
    return result

def most_frequent(n): 
    return n.count(max(set(n), key = n.count))
'''


def WhichHand(n):
    value_dict = {'T': 10, 'J':11, 'Q': 12, 'K': 13, 'A': 14}
    return value_dict[n]

def creatingListNumber(n):
    #n is the list of poker hand, creating a list of all numbers of hands and its suits
    number_list = []
    suit_list   = []
    for i in range(5):
        if n[i][0].isdigit():
            number_list.append(int(n[i][0]))
        else:
            number_list.append(WhichHand(n[i][0]))
        suit_list.append(n[i][1])
    return number_list, suit_list
    
def HandResult(n):
    number_hand = creatingListNumber(n)[0]
    suit_hand = creatingListNumber(n)[1]
    set_number_hand = set(number_hand)
    set_suit_hand = set(suit_hand)
    len_set_suit_hand = len(set_suit_hand)
    len_set_number_hand = len(set_number_hand)
    max_number_repeat_hand = max(set_number_hand, key = number_hand.count)
    min_number_repeat_hand = min(set_number_hand, key = number_hand.count)
    most_frequent_nu_hand = number_hand.count(max(set_number_hand, key = number_hand.count))
    max_number = max(number_hand)
    min_number = min(number_hand)
    list_range_number = list(range(min_number, max_number+1))
    sort_number = sorted(number_hand)
    switcher = {
        (len_set_number_hand == 4): [1, max_number_repeat_hand], # One Pair
        (len_set_number_hand == 3 and most_frequent_nu_hand == 2): [2, max(sorted(set_number_hand, reverse=True), key = number_hand.count),max(sorted(set_number_hand), key = number_hand.count), min_number_repeat_hand], #"Two Pairs"
        (len_set_number_hand == 3 and most_frequent_nu_hand == 3): [3, max_number_repeat_hand], #"Three Kind",
        (sort_number == list_range_number and len_set_suit_hand != 1): [4, max_number, sort_number[3], sort_number[2], sort_number[1], sort_number[0]], #"Straight",
        (len_set_suit_hand == 1 and sort_number != list_range_number): [5, max_number, sort_number[3], sort_number[2], sort_number[1], sort_number[0]], #"Flush",
        (len_set_number_hand == 2 and most_frequent_nu_hand == 3): [6, max_number_repeat_hand], #"Full House",
        (len_set_number_hand == 2 and most_frequent_nu_hand == 4): [7, max_number_repeat_hand, min_number_repeat_hand], #"Four Kind",
        (sort_number == list_range_number and len_set_suit_hand == 1): [8, max_number, sort_number[3], sort_number[2], sort_number[1], sort_number[0]] # "Straight Flush",
    }
    func = switcher.get(True,  [0, max_number, sort_number[3], sort_number[2], sort_number[1], sort_number[0]]) #"High Card",
    return func


def CountingHands(filename):
    f = open(filename, "r")
    count = 0
    for eachLine in f:
        list_line = list(eachLine.strip('\n').split(' '))
        player1_hand = list_line[:5]
        player2_hand = list_line[5:]
        player1_hand_result = HandResult(player1_hand)
        player2_hand_result = HandResult(player2_hand)
        for (n1,n2) in zip(player1_hand_result, player2_hand_result):
            if n1 > n2:
                count += 1
                break
            elif n1 < n2:
                break
    return count
        
final = CountingHands("p054_poker.txt")
print(final)