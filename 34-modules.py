# Main App

import converters

from converters import kg_to_lbs

my_weight = converters.lbs_to_kg(210)

your_weight = kg_to_lbs(94.5)

print(my_weight)
print(your_weight)



# Exercise

import utils

my_list = [3, 15, 12, 6, 1, 10]
maximum = utils.find_max(my_list)

print(f"Largest number: {maximum}")
