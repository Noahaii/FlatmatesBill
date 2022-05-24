from flat import Flatmate, Bill
from reports import PDF


def main():
    amount = float(input('What is the bill amount: '))
    period = input('What is the bill period E.g. December 2021: ')
    the_bill = Bill(amount, period)
    number_of_flatmates = int(input('How many flatmates are paying this period: '))
    flatmate_members = []

    name = input('Enter name of a flatmate paying this period: ')
    days = int(input(f'how many days has {name} spent in the house: '))
    flatmate = Flatmate(name=name, days_in_house=days)
    flatmate_members.append(flatmate)
    days_sum = flatmate_members[0].days_in_house
    n = 1
    while n < number_of_flatmates:
        name = input('Enter name of another flatmate paying this period: ')
        days = int(input(f'how many days has {name} spent in the house: '))
        flatmate = Flatmate(name=name, days_in_house=days)
        flatmate_members.append(flatmate)
        days_sum += flatmate_members[n].days_in_house
        n += 1

    for i in range(0, number_of_flatmates):
        this_flat_bill = flatmate_members[i].pays(the_bill.amount, days_sum)
        print(f"{flatmate_members[i].name} pays {this_flat_bill}")

    the_pdf = PDF('bill_report.pdf')
    the_pdf.generate(the_bill, flatmate_members, number_of_flatmates, days_sum)


if __name__ == "__main__":
    main()