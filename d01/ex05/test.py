from the_bank import Bank, Account

try:
    a = Account("graziela", a=20)
    b = Bank()
    b.add(a)
except ValueError as err:
    print(err)
