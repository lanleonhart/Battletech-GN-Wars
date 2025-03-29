def calculate_c_bill_cost(c_bill_cost_factor, mech_tonnage):
    # Calculate C-Bill Cost for Installation
    c_bill_cost_value = c_bill_cost_factor * mech_tonnage * mech_tonnage
    
    return c_bill_cost_value

# Take user inputs
mech_tech_rating = int(input("Enter Mech Tech Rating (integer): "))
mech_tonnage = int(input("Enter Mech Tonnage (integer): "))
tech_cost_factor = float(input("Enter Tech Cost Factor (double): "))

# Calculate Installation Time
installation_time = tech_cost_factor * (mech_tonnage / mech_tech_rating)

# Display the Installation Time
print(f"Installation Time: {installation_time} days")

# Get the C-Bill Cost Factor from the user
c_bill_cost_factor = float(input("---------------------------\nEnter C-Bill Cost Factor: "))

# Calculate C-Bill Cost based on Mech Tonnage and C-Bill Cost Factor
result_c_bill_cost = calculate_c_bill_cost(c_bill_cost_factor, mech_tonnage)

# Display the C-Bill Cost
print(f"Installation Cost: {result_c_bill_cost:,.0f} C-Bills")
