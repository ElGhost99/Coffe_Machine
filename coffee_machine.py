
def machine_has(water, milk, beans, cups_disposable,money):
    print("The coffe machine has:")
    print(f"{water} ml of water")
    print(f"{milk} ml of milk")
    print(f"{beans} g of coffee beans")
    print(f"{cups_disposable} disposable cups ")
    print(f"${money} of money")


def buy(water, milk, beans, cups_disposable, money):
    coffee = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n"))
    cups_disposable -= 1
    if coffee == 1:
        water -= 250
        beans -= 16
        money += 4
        pass
    elif coffee == 2:
        water -= 350
        milk -= 75
        beans -= 20
        money += 7
        pass
    else:
        water -= 200
        milk -= 100
        beans -= 12
        money += 6
        pass
    return water, milk, beans, cups_disposable, money


def check():
    cups_water = water // 200
    cups_milk = milk // 50
    cups_grams = grams // 15
    cups_max = min(cups_water, cups_milk, cups_grams)
    return cups_max

def fill(water, milk, beans, cups_disposable):
    water += int(input("Write how many ml of water you want to add:\n"))
    milk += int(input("Write how many ml of milk you want to add:\n"))
    beans += int(input("Write how many grams of coffee beans you want to add:\n"))
    cups_disposable += int(input("Write how many disposable cups you want to add:\n"))
    return water, milk, beans, cups_disposable

def take(money):
    print(f"I gave you ${money}")
    money = 0
    return money

def main():
    water = 400
    milk = 540
    beans = 120
    cups_disposable = 9
    money = 550

    machine_has(water, milk, beans, cups_disposable, money)

    action = input("Write action (buy, fill, take)\n")
    if action == "buy":
        water, milk, beans, cups_disposable, money = buy(water, milk, beans, cups_disposable, money)
    elif action == "fill":
        water, milk, beans, cups_disposable = fill(water, milk, beans, cups_disposable)
    else:
        money = take(money)
    machine_has(water, milk, beans, cups_disposable,money)


main()