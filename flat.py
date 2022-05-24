class Bill:
    """
    a class that holds data for a bill.
    attributes include amount and period
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """"
    object to represent someone living in the flat
    and pays their share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, all_flatmates_sum_of_days):
        weight = float(self.days_in_house / all_flatmates_sum_of_days)
        return bill * weight
