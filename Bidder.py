import os

def find_winner(bidder_details):
    heighest_bid = 0
    winner = ""
    for bidder in bidder_details:
        bidding_price = bidder_details[bidder]
        if bidding_price > heighest_bid:
            heighest_bid = bidding_price
            winner = bidder
    print(bidder_details)
    print(f"{winner} is the winner with the bid price of {heighest_bid}")

bidder_details = {}
end_of_bid = False

while not end_of_bid:
    name = input("enter the bidder name: ")
    price = int(input("enter the bid price: "))
    bidder_details[name] = price
    more_bidder = input("are there any other bidders:").lower()
    if more_bidder == 'n':
        end_of_bid = True
        find_winner(bidder_details)
    elif more_bidder == "y":
        os.system('cls')