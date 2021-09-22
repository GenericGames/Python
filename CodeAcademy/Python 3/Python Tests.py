weight = 4.8
cost_ground = 0
cost_ground_premium = 125.00
cost_drone = 0
cheapest_shipping = ""

## Ground Shipping

if weight <= 2.0:
    cost_ground = weight * 1.5 + 20.00
elif weight > 2.0 and weight <= 6.0:
    cost_ground = weight * 3.0 + 20.00
elif weight > 6.0 and weight <= 10.0:
    cost_ground = weight * 4.0 + 20.00
elif weight > 10.0:
    cost_ground = weight * 4.75 + 20.00
else:
    print("error")

print("Ground shipping cost: $" + str(cost_ground))

# Ground shipping premium

print("Ground shipping premium cost: $" + str(cost_ground_premium))

# Drone Shipping

if weight <= 2.0:
    cost_drone = weight * 4.5
elif weight > 2.0 and weight <= 6.0:
    cost_drone = weight * 9.0
elif weight > 6.0 and weight <= 10.0:
    cost_drone = weight * 12.0
elif weight > 10.0:
    cost_drone = weight * 14.25
else:
    print("error")

print("Drone shipping cost: $" + str(cost_drone))

# Cheapest shipping

if cost_ground_premium < cost_ground and cost_ground_premium < cost_drone:
    cheapest_shipping = "Ground premium"
elif cost_ground < cost_drone:
    cheapest_shipping = "Ground"
else:
    cheapest_shipping = "Drone"
print(cheapest_shipping + " is the cheapest shipping method.")
