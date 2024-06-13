from car import Car as c, ElectricCar as ec
# import car

my_mustang = c('ford','mustang',2024)
print(my_mustang.get_descriptive_name())
my_leaf = ec('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())