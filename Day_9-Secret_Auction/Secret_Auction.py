from art import logo

auction_bids = {}
print(logo)
print("Welcome to the secret auction program")
keep_bidding = True

while keep_bidding:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    auction_bids[name] = bid
    proceed = input("Are there any other bidders? Type 'yes' or 'no.\n").lower()

    if proceed == 'yes':
        keep_bidding = True
    else:
        keep_bidding = False

    print("\n" * 50)

# Comparison can be made simpler with the 'max' function.
## highest_bidder = max(auction_bids, key=auction_bids.get)
## highest_bid = auction_bids[highest_bidder]
highest_bidder = ""
highest_bid = 0
for name in auction_bids:
    if auction_bids[name] > highest_bid:
        highest_bid = auction_bids[name]
        highest_bidder = name

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
