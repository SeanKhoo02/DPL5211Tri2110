W = 0.15

print("Natural Mineral Water Dispenser")
print("-------------------------------------")
liters = int(input("\nEnter amount of liters: "))

payment=liters*W

print("\nPrice per litre   = RM ", W)
print("Number of liters = ", liters)
print("Total: RM {:.2f} ".format(payment))



