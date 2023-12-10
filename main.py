import random
from decimal import Decimal
# Function to generate a random security object
def generate_security():
    security_name = f"Security_{random.randint(1, 200)}"
    duration = round(random.uniform(1.0, 10.0), 2)
    ytm = round(random.uniform(0.01, 0.10), 2)
    index_number = random.randint(1, 10)
    weight = Decimal('0.00')  # Initialize weight to 0
    return {
        "security_name": security_name,
        "duration": duration,
        "ytm": ytm,
        "index_number": index_number,
        "weight": weight
    }
# Create an array of 200 security objects
securities = [generate_security() for _ in range(200)]
# Randomly select securities and assign weights
selected_securities = []
total_weight = Decimal('0.00')
while total_weight < Decimal('100.00') and securities:
    security = random.choice(securities)
    max_weight = min(Decimal('2.50'), Decimal('100.00') - total_weight)
    weight = round(random.uniform(0, float(max_weight)), 2)
    security["weight"] = Decimal(str(weight))
    selected_securities.append(security)
    total_weight += Decimal(str(weight))
    securities.remove(security)
# Print the selected securities and their weights
for security in selected_securities:
    print(f"Security Name: {security['security_name']}, Weight: {security['weight']}")
print(f"Total Weight: {total_weight:.2f}")


def calculate_metrics(selected_securities):
    investment_horizon = Decimal('0.00')
    ability_to_absorb_loss = Decimal('0.00')
    target_yield = Decimal('0.00')
    for security in selected_securities:
        weight = Decimal(security["weight"])
        duration = Decimal(security["duration"])
        index_number = Decimal(security["index_number"])
        ytm = Decimal(security["ytm"])
        investment_horizon += weight * duration
        ability_to_absorb_loss += weight * index_number
        target_yield += weight * ytm
    return investment_horizon, ability_to_absorb_loss, target_yield

# Call the function to calculate the metrics
investment_horizon, ability_to_absorb_loss, target_yield = calculate_metrics(selected_securities)
print(f"Investment Horizon: {investment_horizon:.2f}")
print(f"Ability to Absorb Loss: {ability_to_absorb_loss:.2f}")
print(f"Target Yield: {target_yield:.2f}")
