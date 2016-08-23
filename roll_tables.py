# Roll tables are NOT 0 indexed!
# Range is not inclusive of the end, hence what seems to be overlap in indices

# Fill table for the size of the settlement (in terms of type)
size_roll_table = {}
size_roll_table[1] = 'Farm'
for i in range(2,4):
	size_roll_table[i] = 'Hamlet'
for i in range(4,7):
	size_roll_table[i] = 'Village'
for i in range(6,8):
	size_roll_table[i] = 'Town'
size_roll_table[8] = 'City'

# fill table for the racial composition of the settlement
race_roll_table = {
	1: 'All',
	2: '2-Mix',
	3: 'Humans',
	4: 'Humans',
	5: 'Elves',
	6: 'Elves',
	7: 'Dwarves',
	8: 'Dwarves',
	9: 'Orcs',
	10: 'Orcs',
	11: 'Halflings',
	12: 'Halflings',
	13: 'Tieflings',
	14: 'Tieflings',
	15: 'Gnomes',
	16: 'Gnomes',
	17: '3-Mix',
	18: '4-Mix'
}

# fill table for elf type
elf_roll_table = {
	4: 'Half-Elves',
	5: 'Half-Elves',
	6: 'Drow'
}
for i in range(1,4):
	elf_roll_table[i] = 'Elves'

# Fill table for orc type
orc_roll_table = {
	1: 'Orcs',
	2: 'Orcs',
	3: 'Half-Orcs'
}

# Fill table for settlement location	
location_roll_table = {
	1: 'Alerik',
	2: 'Nayadin',
	3: 'Saya',
	4: 'Mered',
	5: 'Skryt',
	6: 'Lladro',
	7: 'Rohm',
	8: 'Dal\'Vhen',
	9: 'W Ardon\'Ya',
	10: 'N Ardon\'Ya',
	11: 'E Ardon\'Ya'
}

# Fill table for purposes
# Example:
# Natural Resources, 2 trade resources, 0 metal resources
purpose_roll_table = {}	
for i in range (1,4):
	purpose_roll_table[i] = ('Road/River convergence', 1, 0)
for i in range (4,7):
	purpose_roll_table[i] = ('Natural Resource', 2, 0)
for i in range (7,9):
	purpose_roll_table[i] = ('Mining Settlement', 1, 1)
for i in range (9,11):
	purpose_roll_table[i] = ('Military/Strategic Value', 0, 0)


# Fill metal resource table
metal_roll_table = {
	1: 'Copper',
	2: 'Copper',
	3: 'Tin',
	4: 'Tin',
	5: 'Iron',
	6: 'Iron',
	7: 'Silver',
	8: 'Gold',
	9: 'Exotic metal',
	10: 'Special metal'
}

trade_resource_roll_table = {
	5: 'Flour Farms',
	6: 'Flour Farms',
	7: 'Grain Farms',
	8: 'Grain Farms',
	9: 'Natural Oils or Fuels',
	10: 'Rare Animals'
}
for i in range(1,5):
	trade_resource_roll_table[i] = 'Grazing Land'


# Population formula
# (num_sides, mult. mod, add. mod)
# For example: (10, 10, 5) would result in
#	a population of (rand(1,10)*10)+5
population_roll_table = {
	'Farm': (20, 1, 0),
	'Hamlet': (10, 10, 0),
	'Village': (10, 100, 0),
	'Town': (10, 1000, 0),
	'City': (10, 500, 10000)
}

gods_roll_table = {
	1: 'None',
	2: 'Shirin',
	3: 'Teva',
	4: 'Turambar',
	5: 'Nirnaeth',
	6: 'Or\'Noor',
	7: 'Lilne',
	8: 'Yolva',
	9: 'Calliope',
	10: 'Dimm',
	11: 'Simple God',
	12: 'Nehar',
	13: 'Calpurnia',
	14: 'Iryna',
	15: 'The Watcher',
	16: 'Murmur',
	17: '2-Mix',
	18: '3-Mix'
}