# Roll tables are NOT 0 indexed!
# Range is not inclusive of the end, hence what seems to be overlap in indices

# Fill up given roll_table from start index to end index (inclusive)
# with the given value.
def inc_range_fill(start, end, roll_table, val):
	for i in range(start, end + 1):
		roll_table[i] = val

# Fill table for the size of the settlement (in terms of type)
size_roll_table = {}
size_roll_table[1] = 'Farm'
inc_range_fill(2, 3, size_roll_table, 'Hamlet')
inc_range_fill(4, 5, size_roll_table, 'Village')
inc_range_fill(6, 7, size_roll_table, 'Town')
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
inc_range_fill(1,3, elf_roll_table, 'Elves')

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
inc_range_fill(1, 3, purpose_roll_table, ('Road/River convergence', 1, 0))
inc_range_fill(4, 6, purpose_roll_table, ('Natural Resources', 2, 0))
inc_range_fill(7, 8, purpose_roll_table, ('Mining Settlement', 1, 1))
inc_range_fill(9, 10, purpose_roll_table, ('Military/Strategic point', 0, 0))

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
inc_range_fill(1, 4, trade_resource_roll_table, 'Grazing Land')


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

features_roll_table = {
	1: 'Arms',
	2: 'Books',
	3: 'Brewing',
	4: 'Centre of Learning',
	5: 'Crumbling ramparts/palisade',
	6: 'Eerie ruin nearby',
	7: 'Famous for annual feast or festival',
	8: 'Famous/notorious inn',
	9: 'Foodstuffs',
	10: 'Glass or pottery crafters',
	11: 'Goats',
	12: 'Government',
	13: 'Home of famous artist, actor, or author',
	14: 'Horse breeding',
	15: 'Illicit services',
	16: 'Imortant argricultural producer',
	17: 'Imposing bridge or other construction',
	18: 'Impressive shrine, statue, or memorial',
	19: 'Impressive temple to major deity',
	20: 'Inhabitants ostracized by outsiders',
	21: 'Known as lawless place',
	22: 'Large dwarven community (2d10%)',
	23: 'Large library',
	24: 'Large producer of charcoal',
	25: 'Natural fort',
	26: 'Logging, timber, and sawing',
	27: 'Lush park, gardens, or commons',
	28: 'Major road/river warden station',
	29: 'Mentioned in famous song, saga, or poem',
	30: 'Mighty watch tower or beacon',
	31: 'Military strongoiint (double garrison)',
	32: 'Mining (metal or mineral)',
	33: 'Notorious for corrupt officials',
	34: 'On the decline',
	35: 'Partially in ruins',
	36: 'Preserves',
	37: 'Recently under attack',
	38: 'Rumored site of unnatural events',
	39: 'Recently prospering',
	40: 'Geographically isolated',
	41: 'Historical importance',
	42: 'Sheep',
	43: 'Significant center of trade',
	44: 'Significant fortifications',
	45: 'Major prison/labor camp site',
	46: 'Recent unrest',
	47: 'Sizable Halfling Community (2d10%)',
	48: 'Greedy Tradesmen',
	49: 'Trapping',
	50: 'Wine'
}


first_name_element = {
	1: 'All',
	2: 'Als',
	3: 'Alt',
	4: 'Ammer',
	5: 'Arn',
	6: 'Aschen',
	7: 'Ascher',
	8: 'Bens',
	9: 'Birn',
	10: 'Blanken',
	11: 'Blau',
	12: 'Blut',
	13: 'Bogen',
	14: 'Borken',
	15: 'Braun',
	16: 'Buche',
	17: 'Diep',
	18: 'Dunkel',
	19: 'Eis',
	20: 'Ell',
	21: 'Eschen',
	22: 'Fried',
	23: 'Fursten',
	24: 'Gels',
	25: 'Gelb',
	26: 'Giessen',
	27: 'Grab',
	28: 'Graten',
	29: 'Grau',
	30: 'Gros',
	31: 'Gruft',
	32: 'Grun',
	33: 'Gunz',
	34: 'Hagel',
	35: 'Hall',
	36: 'Hart',
	37: 'Hauzen',
	38: 'Hech',
	39: 'Herbst',
	40: 'Herz',
	41: 'Hohen',
	42: 'Holz',
	43: 'Ilmen',
	44: 'Kall',
	45: 'Klage',
	46: 'Klein',
	47: 'Lauffen',
	48: 'Lauter',
	49: 'Lipp',
	50: 'Main',
	51: 'Marien',
	52: 'Merse',
	53: 'Mess',
	54: 'Moos',
	55: 'Naum',
	56: 'Nenn',
	57: 'Nieder',
	58: 'Nord',
	59: 'Ober',
	60: 'Ost',
	61: 'Oster',
	62: 'Otters',
	63: 'Pfaffen',
	64: 'Pfarr',
	65: 'Pfeffen',
	66: 'Rain',
	67: 'Riesen',
	68: 'Saal',
	69: 'Salz',
	70: 'Schaf',
	71: 'Schone',
	72: 'Schroben',
	73: 'Schwab',
	74: 'Schwan',
	75: 'Schwarz',
	76: 'Semmen',
	77: 'Sim',
	78: 'Sommer',
	79: 'Sonder',
	80: 'Speeger',
	81: 'Thurin',
	82: 'Tier',
	83: 'Tranen',
	84: 'Trost',
	85: 'Upfen',
	86: 'Vater',
	87: 'Vecker',
	88: 'Wall',
	89: 'Waren',
	90: 'Wein',
	91: 'Weiss',
	92: 'West',
	93: 'Winter',
	94: '[charname]',
	95: 'Starn',
	96: 'Stein',
	97: 'Sud',
	98: 'Tauber',
	99: 'Taufel'
}

second_name_element = {}
inc_range_fill(1, 3, second_name_element, 'acker')
inc_range_fill(4, 6, second_name_element, 'bach')
inc_range_fill(7, 9, second_name_element, 'berg')
inc_range_fill(10, 12, second_name_element, 'brucke')
inc_range_fill(13, 15, second_name_element, 'brunnen')
inc_range_fill(16, 18, second_name_element, 'burg')
inc_range_fill(19, 21, second_name_element, 'chen')
inc_range_fill(22, 24, second_name_element, 'dorf')
inc_range_fill(25, 27, second_name_element, 'feld')
inc_range_fill(28, 30, second_name_element, 'fort')
inc_range_fill(31, 33, second_name_element, 'galgen')
inc_range_fill(34, 36, second_name_element, 'haus')
inc_range_fill(37, 39, second_name_element, 'hausen')
inc_range_fill(40, 42, second_name_element, 'helde')
inc_range_fill(43, 45, second_name_element, 'helm')
inc_range_fill(46, 48, second_name_element, 'hof')
inc_range_fill(49, 51, second_name_element, 'holz')
inc_range_fill(52, 54, second_name_element, 'horst')
inc_range_fill(55, 57, second_name_element, 'hugel')
inc_range_fill(58, 60, second_name_element, 'hut')
inc_range_fill(61, 63, second_name_element, 'hutte')
inc_range_fill(64, 66, second_name_element, 'leben')
inc_range_fill(67, 69, second_name_element, 'munde')
inc_range_fill(70, 72, second_name_element, 'schweig')
inc_range_fill(73, 75, second_name_element, 'stadt')
inc_range_fill(76, 78, second_name_element, 'statte')
inc_range_fill(79, 81, second_name_element, 'stein')
inc_range_fill(82, 84, second_name_element, 'tur')
inc_range_fill(85, 87, second_name_element, 'wald')
inc_range_fill(88, 90, second_name_element, 'wasser')
inc_range_fill(91, 92, second_name_element, 'alte')
inc_range_fill(93, 94, second_name_element, 'bad')
inc_range_fill(95, 96, second_name_element, 'grosse')
inc_range_fill(97, 98, second_name_element, 'hellige')
inc_range_fill(99, 100, second_name_element, 'neue')