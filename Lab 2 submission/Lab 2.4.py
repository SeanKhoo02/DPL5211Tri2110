# Student ID: 1201201336
# Student Name: Khoo Chong Qin

banana = 1.50
grapes = 5.60


print("Invoice for Fruits Purchase")
print("---------------------------------")
print("\n")
Q1 = int(input("Enter the quantity (comb) of banana bought: "))
Q2 = int(input("Enter the amount (kg) of grapes bought: "))

total_b= Q1*1.50
total_g= Q2*5.60

total = total_b + total_g
print("\n")
print("Item \t\t Qty \t Price  \tTotal")
print("Banana (combs)" "\t", Q1, "\t", banana, "\t\t""RM {:.2f}".format(total_b))
print("Grapes (kg)" "\t", Q2, "\t", grapes, "\t\t""RM {:.2f}".format(total_g))

print("Total: RM ", total)