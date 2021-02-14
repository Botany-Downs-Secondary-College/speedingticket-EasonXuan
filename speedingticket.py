warrants = ["Eason", "Kiran", "Jass"]
fines = 0


def checkWarrants(name):
    for driver in warrants:
        if driver == name:
            print(driver.upper(),"IS WANTED FOR ARREST")



def calculateFine(fines):
    while True:
        try:
            spd_limit = int(input("Enter speed limit: "))
            vehicle_speed = int(input("Enter vehicle speed: "))
            difference = vehicle_speed - spd_limit
            fines = difference * 10

            if difference > 0:
                print("You are over the speed limit! Your fine is ${}".format(fines))
                break
            elif difference <= 0:
                print("You have not gone past the speed limit! You are safe!")
                break
            else:
                print("please enter valid numbers")
        except ValueError:
            print("Please enter valid numbers")

while True:
    try:
        name = input("Enter the name of the dirver: ")
        name = name.title().strip()

        checkWarrants(name)
        calculateFine(fines)

        replay = input("Would you like to enter another driver? (Y/N): ")

        if replay == "Y":
            print("==============================")
        elif replay == "N":
            break
        else:
            print("please enter (Y/N)")
    except ValueError:
        print("please enter valid answers")


