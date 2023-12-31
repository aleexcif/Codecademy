# Ground Shipping
def shipping_cost_ground(weight):

  if weight <= 2:
    price_per_pound = 1.50
  elif weight <= 6:
    price_per_pound = 3.00
  elif weight <= 10:
    price_per_pound = 4.00
  else:
    price_per_pound = 4.75

  return 20 + (price_per_pound * weight)

print(shipping_cost_ground(8.4))

# Premium Ground Shipping
shipping_cost_premium = 125.00

print(shipping_cost_premium)

# Drone Shipping
def shipping_cost_drone(weight):

  if weight <= 2:
    price_per_pound = 4.50
  elif weight <= 6:
    price_per_pound = 9.00
  elif weight <= 10:
    price_per_pound = 12.00
  else:
    price_per_pound = 14.25

  return price_per_pound * weight

print(shipping_cost_drone(1.50))

# Cheapest Shipping Method
def print_cheapest_shipping_method(weight):
  
  ground = shipping_cost_ground(weight)
  premium = shipping_cost_premium
  drone = shipping_cost_drone(weight)

  if ground < premium and ground < drone:
    method = "standard ground"
    cost = ground
  elif premium < ground and premium < drone:
    method = "premium ground"
    cost = premium
  else:
    method = "drone"
    cost = drone

  print(
    "The cheapest option available is $%.2f with %s shipping."
    % (cost, method)
    )

# Test Cheapest Shipping Method
print_cheapest_shipping_method(4.8)
print_cheapest_shipping_method(41.5)
