auction_dict = {}
more_bidders = True

while more_bidders:
  name = input("What is your name? ")
  num = float(input("What is your bidding price? $"))
  auction_dict[name] = num
# While more_bidders is True, add the name-num pair inputs to the auction_dict dictionary

  bid_again = input("Bid again? Yes or No ").lower()
  if bid_again == "no":
    more_bidders = False
# If the user enters "no", the program will end and the following code will execute
    
    print(auction_dict)
# Print the dictionary for the user to see

    largest_value = max(auction_dict.values())
# Get the maximum value (highest bid) from the dictionary values

    for key, value in auction_dict.items():
      if value == largest_value:
        key_with_largest_value = key
# Get the key name associated with the highest value from the dictionary

        print(f"The winner of the auction is {key_with_largest_value} with a bid of ${largest_value}")
# Print the winner of the auction with the highest bid (key_with_largest_value & largest_value)