# Student ID: 1201201336
# Student Name: Khoo Chong Qin

kilo = float(input("Please enter the value of kilogram : "))
gram = kilo * 1000
print("For ", kilo, " kilogram is equivaldent to ", round(gram, 2), " gram")

#other method
print("For {:.2f} kilogram is equivalent to {:.2f} gram".format(kilo, gram))