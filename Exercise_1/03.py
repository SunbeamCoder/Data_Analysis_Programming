# DangQuocToan_20051051_51
kWh = int(input("Enter kWh: "))
if kWh <= 100:
    unit_price = kWh * 2000
else:
    unit_price = kWh * 2100
print(f"bill  = {unit_price}")