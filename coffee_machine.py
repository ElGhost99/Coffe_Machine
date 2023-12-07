water = int(input("Write how many ml of water the coffe machine has:\n"))
milk = int(input("Write how many ml of milk the coffe machine has:\n"))
grams = int(input("Write how many grams of coffe beans the coffe machine has:\n"))
cups = int(input("Write how many cups of coffee you will need:\n"))
def check():
    cups_water = water // 200
    cups_milk = milk // 50
    cups_grams = grams // 15
    cups_max = min(cups_water, cups_milk, cups_grams)
    return cups_max

cups_max = check()
if cups ==cups_max:
    print("Yes, I can make that amount of coffee")
elif cups < cups_max:
    more_cups = cups_max - cups
    print(f"Yes, I can make that amount of coffee (and even {more_cups} more than that)")
else:
    print(f"No, I can make only {cups_max} cups of coffee")
