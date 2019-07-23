from _datetime import datetime as dx  # From whatever module, import this specific API and call it as dx in this file

delta = dx.now() - dx(2019, 7, 21)
print(delta.days, delta.seconds)

whenever = dx.strptime("2019-07-22", "%Y-%m-%d")  # Hours is "H"; minutes are "M"
print(whenever)

print(whenever.strftime("%Y"))

print(whenever.year, whenever.day, whenever.hour, whenever.second)
