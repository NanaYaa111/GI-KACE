#1. Makola Market Sales System
inventory = {
    "Tomatoes": {"stock": 150, "price_per_unit": 5.0},
    "Onions": {"stock": 80, "price_per_unit": 3.5},
    "Garden Eggs": {"stock": 200, "price_per_unit": 1.0}
}

print("Welcome to Makola Market!")

while True:
    item = input("Enter item to buy (Tomatoes, Onions, Garden Eggs) or 'exit': ")

    if item == "exit":
        print("Closing sales. Total transactions completed.")
        break

    if item in inventory:
        quantity = int(input("Enter quantity to buy: "))

        if quantity > inventory[item]["stock"]:
            print("Sorry, only", inventory[item]["stock"], "units of", item, "remaining.")
        else:
            cost = quantity * inventory[item]["price_per_unit"]
            inventory[item]["stock"] = inventory[item]["stock"] - quantity
            print("Sale successful! Cost: GHS", cost, ". Now", inventory[item]["stock"], "units of", item, "left.")
    else:
        print("Item not found in stock. Check spelling.")


#2. Ghana Water Company (GWCL) Bill Calculator
service_charge = 15

consumption = float(input("Enter water consumption in cubic meters: "))

if consumption <= 15:
    consumption_cost = consumption * 0.90
elif consumption <= 30:
    consumption_cost = (15 * 0.90) + ((consumption - 15) * 1.20)
else:
    consumption_cost = (15 * 0.90) + (15 * 1.20) + ((consumption - 30) * 1.80)

total_bill = service_charge + consumption_cost

print("Consumption:", consumption, "m3")
print("Service Charge: GHS", round(service_charge, 2))
print("Consumption Cost: GHS", round(consumption_cost, 2))
print("Total Bill: GHS", round(total_bill, 2))


#3. Traffic Speed Analyzer for Road Safety
recorded_speeds = [95, 110, 100, 85, 125, 90, 105, 115, 70, 130, 99, 101, 88]
SPEED_LIMIT = 100
speeding_violations = []

for speed in recorded_speeds:
    if speed > SPEED_LIMIT:
        print("WARNING: Vehicle recorded at", speed, "km/h. Exceeded limit of", SPEED_LIMIT, "km/h.")
        speeding_violations.append(speed)

total_vehicles = len(recorded_speeds)
total_violations = len(speeding_violations)
percentage_speeding = round((total_violations / total_vehicles) * 100, 2)

total_speed = 0
for speed in recorded_speeds:
    total_speed += speed
average_speed = round(total_speed / total_vehicles, 2)

print("Traffic Speed Analysis Summary ")
print("Total vehicles recorded:", total_vehicles)
print("Total speeding violations:", total_violations)
print("Percentage of vehicles speeding:", percentage_speeding, "%")
print("Average speed of vehicles:", average_speed, "km/h")
focused_segment = recorded_speeds[2:8] 
print("Speeds for focused inspection segment (3rd to 8th vehicle):", focused_segment)

