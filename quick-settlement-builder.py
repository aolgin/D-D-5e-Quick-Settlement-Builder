import random
import sys
import roll_tables as tables

MAX_FEATURES = 4

class Settlement:
	# Filled constructor
	def __init__(self, name="", size="", features=[], population=0, location="", 
		purpose="", resources=[], races=[], gods=[]):
		self.name = name
		self.size = size
		self.features = features
		self.location = location
		self.population = population
		self.purpose = purpose
		self.resources = resources
		self.races = races
		self.gods = gods

	# Roll the dice! Get a random number between start and num_sides (inclusive)
	def roll(self, num_sides, start=1, debug=False):
		return random.randint(start, num_sides)

	def roll_name(self, debug=False):
		first = tables.first_name_element[self.roll(len(tables.first_name_element))]
		second = tables.second_name_element[self.roll(len(tables.second_name_element))]
		name = first + second
		if debug:
			print('Name: ' + name)
		return name

	# handle logic for rolling for X number of features
	def roll_features(self, debug=False):
		num_features = self.roll(MAX_FEATURES)
		features = [] 
		i = 1
		while i <= num_features:
			k = self.roll(len(tables.features_roll_table))
			if tables.features_roll_table[k] not in features:
				features.append(tables.features_roll_table[k])
				i += 1

		if debug:
			print('Features: ' + str(features))
		return features

	def roll_resources(self, purpose, debug=False):
		num_trade_resources = purpose[1]
		num_metal_resources = purpose[2]
		resource_list = []
		if num_trade_resources > 0:
			i = 1
			while i <= num_trade_resources:
				trade_roll = self.roll(len(tables.trade_resource_roll_table))
				resource = tables.trade_resource_roll_table[trade_roll]
				if resource not in resource_list:
					resource_list.append(resource)
					i += 1
		if num_metal_resources > 0:
			metal_roll = self.roll(len(tables.metal_roll_table))
			resource_list.append(tables.metal_roll_table[metal_roll])
		if debug:
			print('Resources: ' + str(resource_list))
		return resource_list

	def roll_races(self, debug=False):
		race_roll = self.roll(len(tables.race_roll_table))
		main_race = tables.race_roll_table[race_roll]
		if debug:
			print('Main Race: ' + main_race)
		race_list = []
		if main_race == 'Elves':
			race_list.append(tables.elf_roll_table[self.roll(len(tables.elf_roll_table))])
		elif main_race == 'Orcs':
			race_list.append(tables.orc_roll_table[self.roll(len(tables.orc_roll_table))])
		elif "Mix" in main_race:
			i = int(main_race[0])
			roll_range_start = 3
			roll_range_end = len(tables.race_roll_table) - 2
			k = 1
			while k <= i:
				new_race = tables.race_roll_table[self.roll(roll_range_end, roll_range_start)]
				if new_race == 'Elves':
					new_race = tables.elf_roll_table[self.roll(len(tables.elf_roll_table))]
				elif new_race == 'Orcs':
					new_race = tables.orc_roll_table[self.roll(len(tables.orc_roll_table))]
				
				if new_race not in race_list:
					race_list.append(new_race)
					k += 1
		else:
			race_list.append(main_race)

		if debug:
			print('Races: ' + str(race_list))
		return race_list

	def roll_gods(self, debug=False):
		gods_roll = self.roll(len(tables.gods_roll_table))
		main_god = tables.gods_roll_table[gods_roll]
		if debug:
			print('Main God: ' + main_god)
		god_list = []
		if "Mix" in main_god:
			i = int(main_god[0])
			roll_range_start = 2
			roll_range_end = len(tables.gods_roll_table) - 2
			k = 1
			while k <= i:
				new_god = tables.gods_roll_table[self.roll(roll_range_end, roll_range_start)]
				if new_god not in god_list:
					god_list.append(new_god)
					k += 1
		else:
			god_list.append(main_god)

		if debug:
			print('Gods: ' + str(god_list))
		return god_list

	def printArray(self, arr):
		x = len(arr)
		y = len(arr) - 1
		result = ""
		if x == 1:
			result += arr[0]
		else:
			for i in range(x):
				if i == y:
					result += "and {}".format(arr[i])
				else:
					result += "{}, ".format(arr[i])
		return result

	# convert the object to a nicely formatted string
	def toPrettyString(self):
		sentence = '{} is a {} of about {} people, located in {}. '.format(self.name, self.size, self.population, self.location) 
		sentence += 'Its residents are comprised of {}. The main god(s) worshipped here is/are {}. '.format(self.printArray(self.races), self.printArray(self.gods))
		sentence += 'It was built as a {}, with resources such as {}. It has a some notable features, such as {}'.format(self.purpose, self.printArray(self.resources), self.printArray(self.features))
		return sentence

	def toCSVString(self):
		return 'nothing for now'

	# Generate a settlement and fill it in
	def generate_settlement(self, debug=False):
		name = self.roll_name(debug)
		features = self.roll_features(debug)
		races = self.roll_races(debug)
		gods = self.roll_gods(debug)
		
		size = tables.size_roll_table[self.roll(len(tables.size_roll_table))]
		if debug:
			print('size: ' + size)
		
		population_tuple = tables.population_roll_table[size]
		population = (self.roll(population_tuple[0]) * population_tuple[1]) + population_tuple[2]
		if debug:
			print('Population: ' + str(population))
		
		location = tables.location_roll_table[self.roll(len(tables.location_roll_table))]
		if debug:
			print('Location: ' + location)

		purpose_roll = tables.purpose_roll_table[self.roll(len(tables.purpose_roll_table))]
		purpose = purpose_roll[0]
		if debug:
			print('Purpose: ' + purpose)
		resources = self.roll_resources(purpose_roll, debug)

		self.name = name
		self.features = features
		self.races = races
		self.gods = gods
		self.population = population
		self.location = location
		self.purpose = purpose
		self.resources = resources
		self.size = size
		return self
		#return self.__init__(name, size, features, population, location, purpose, resources, races, gods)

def __main__():
	nargs = len(sys.argv)

	if nargs > 2:
		print("Error: There should not be any arguments passed via CLI")
		return 1

	if nargs == 1:
		debug = False
	elif nargs == 2:
		if sys.argv[1] == 'True':
			debug = True
		elif sys.argv[1] == 'False':
			debug = False

	# Create instance of settlement class for generator use
	settlement_instance = Settlement()

	# Ask for input (currently pseudo code)
	print('How many settlements would you like to generate?: ')
	num_settlements = int(raw_input())

	# Create basic gui
	
	# Output to csv

	# Generator loop


	if num_settlements <= 0:
		print("Error: Please input a non-zero number!")
		return 1
	else:
		# 'range' is not inclusive of the end
		for i in range(0, num_settlements):
			print('--------NEW SETTLEMENT---------')
			s = settlement_instance.generate_settlement(debug)
			print(s.toPrettyString())
	return 0


__main__()
