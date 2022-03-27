from flat import Flatmate, Bill


def main():
    amount = int(input('What is the bill amount: '))
    month = input('What is the bill period: ')
    the_bill = Bill(amount, month)
    number_of_flatmates = int(input('How many flatmates are paying this period: '))
    flatmate_members = []
    name = input('Enter name of a flatmate paying this period: ')
    days = int(input(f'how many days has {name} spent in the house: '))
    flatmate = Flatmate(name=name, days_in_house=days)
    flatmate_members.append(flatmate)
    n = 1
    while n < number_of_flatmates:
        name = input('Enter name of another flatmate paying this period: ')
        days = int(input(f'how many days has {name} spent in the house: '))
        flatmate = Flatmate(name=name, days_in_house=days)
        flatmate_members.append(flatmate)
        n += 1

    for i in range(len(flatmate_members)):
        print(f'{flatmate_members[i].name}: {flatmate_members[i].days_in_house}')


if __name__ == "__main__":
    main()
