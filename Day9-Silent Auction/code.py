from art import logo

print(logo)

bids={}
bidding_end=False

def highest_bidder(bids):
    highest_bid=0
    winner=""
    for bid in bids:
        new_bid=bids[bid]
        if new_bid>highest_bid:
            highest_bid=new_bid
            winner=highest_bid
    print(f"The highest price is from {winner}")

while not bidding_end:
    print("Welcome to the secret auction")
    name=input("What is your name?")
    price=int(input("What is your auction? "))
    bids[name]=price
    should_continue=input("Do you want to continue?yes or no: ").lower()
    if should_continue=="no":
        bidding_end=True
        highest_bidder(bids)

 