pay_per_hour = float(input("enter pay per hour"))
total_hours = int(input("enter total hours"))
if total_hours <= 40:
    pay = total_hours * pay_per_hour
else:
    over_time = total_hours -40
    ot_pay = over_time * 1.5 * pay_per_hour
    normal_pay = pay_per_hour
    pay =
print()