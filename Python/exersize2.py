def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sqft = sqft_walls + sqft_ceiling
    gallons_needed = total_sqft / sqft_per_gallon
    cost = cost_per_gallon * gallons_needed
    return cost
# Given values for the room
sqft_walls = 432
sqft_ceiling = 144
sqft_per_gallon = 400
cost_per_gallon = 15

# Use the get_cost function to calculate the cost of one coat of paint for the room
project_cost_one_coat = get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon)

# Number of coats to apply
num_coats = 8

# Calculate the project cost for applying one coat eight times
total_project_cost = project_cost_one_coat * num_coats