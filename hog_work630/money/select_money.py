
import money


def select_money():
    if money.saved_money == 2000:
        print(f"发工资了，工资是{money.saved_money}")
    else:
        print(f"没有发工资,工资是{money.saved_money}")
