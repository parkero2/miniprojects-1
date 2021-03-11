initial_value = 50 # The starting value of a giftcard
items_brought = ["Christmas cape bunde", "1,000 O-Bux", "Epic-tier gift", "VIP rank"]
amount_spent = 35 # How much was spent

print("You spent ${} of your ${} giftcard, leaving ${} remaining. You brought the following items:\n1x {}, \n1x {}, \n1x {}, \n1x {}".format(amount_spent, initial_value, initial_value - amount_spent, items_brought[0], items_brought[1], items_brought[2], items_brought[3])) # Print what the inital balance was, amount spent on what items and how much is remaining