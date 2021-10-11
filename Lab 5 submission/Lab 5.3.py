print("=================================")
print(" \t     MENU")
menu = int(input("Please enter your choice [1 or 2]: "))


def cm_to_meter(centimeter):
        meter = centimeter / 100
        return meter

def meter_to_cm(meter):
    centimeter = meter * 100
    return centimeter

def get_cm():
    cm = float(input("Please enter a value for centimeter :"))
    m = cm_to_meter(cm)
    print(" {:.2f} cm is {:.2f} meter ".format(cm, m))

def get_m():
    m = float(input("Please enter a value for meter :"))
    cm = meter_to_cm(m)
    print(" {:.2f} cm is {:.2f} meter".format(cm, m))

if(menu == 1):
    get_cm()

elif(menu ==2):
   get_m()
else:
    print("Invalid choice")
