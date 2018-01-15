#Initialize Variables
deck = ["1","2","3","4","5","6","7","8","9","10","J","Q","K","A"]
choice = 0
player = []
dealer = []

#Total function
def total(person):
    total = 0
    hasAce = 0
    i = 0

    #Add value of each card
    while i<len(person):
        #If card is a number card
        try:
            total += int(person[i])
        #If card is a face card
        except:
            #If card is an ace
            if person[i] == "A":
                hasAce = 1
            #If card isnt an ace
            else:    
                total += 11
            
        i += 1   
 
    #If the plaer has an ace
    if hasAce == 1:
        #Add 1 or...
        if (total+10) > 21:
            total += 1
        #Add 10 if able
        else:
            total += 10

    return total

#Show Cards Function
def printStatus(player, dealer):
    #Show Dealer's total and cards
    print("Dealer's total is: " + str(total(dealer)) + ": ")
    i = 0
    while i<len(dealer):
        if i == (len(dealer)-1):
            print(dealer[i])
        else:
            print(dealer[i], end=", ")
        i += 1

    #Show Player's total and cards
    print("Player's total is: " + str(total(player)) + ": ")
    i = 0
    while i<len(player):
        print(player[i], end="")
        i += 1
        if i < len(player):
            print(", ", end="")
    return 0

#Shuffle Deck
import random
random.shuffle(deck)

#Dealing (Dealer 1 card, Player 2 cards)
print("Dealer draws first card.")
dealer.append(deck[0])
del deck[0]
print("Player receives two card.\n")
player.append(deck[0])
del deck[0]
player.append(deck[0])
del deck[0]
printStatus(player, dealer)

#Player Decision Loop
while choice != "S" and choice != "s":
    choice = input("\n\nDo you want to (H)it, (S)tay, or (Q)uit?\n")
    
    if choice == "H" or choice == "h":
        if len(deck) != 0:
            player.append(deck[0])
            del deck[0]
        printStatus(player, dealer)

        if total(player) > 21:
            print("\n\nPlayer bust!")
            input('Press ENTER to exit')
            exit()
        
    elif choice == "Q" or choice == "q":
        exit()

#Dealer draws rest of cards
while int(total(dealer)) < 17:
    dealer.append(deck[0])
    del deck[0]

#Final totals
printStatus(player, dealer)
print("\n")

#Check winner
if total(dealer) > 21:
    print("Dealer bust!")
elif total(dealer) > total(player):
    print("Dealer wins!")
elif total(dealer) < total(player):
    print("You win!")
else:
    print("Tie!")

input('Press ENTER to exit')
