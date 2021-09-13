const = 0.15

print("Natural Mineral Water Dispenser")
print("-------------------------------------")
liters = int(input("\nEnter amount of liters: "))

payment=liters*const

print("\nPrice per litre   = RM ", const)
print("Number of liters = ", liters)
print("Total: RM {:.2f} ".format(payment))



