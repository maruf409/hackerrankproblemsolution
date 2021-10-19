def solve(meal_cost, tip_percent, tax_percent):
    tips = ((meal_cost)/100) * tip_percent
    tax = (tip_percent-(tax_percent/10)) / tip_percent
    totall = meal_cost + tips + tax
    #x = round(totall)
    print(int(totall))

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)