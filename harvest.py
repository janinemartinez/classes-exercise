############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, name, first_harvest, color, is_seedless, is_bestseller):
        """Initialize a melon."""
        print('initializing MelonType')
        self.name = name
        self.color = color
        self.code = code
        self.first_harvest = first_harvest
        self.pairings = []
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)
        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code
        # Fill in the rest


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    musk = MelonType('musk', 'Muskmelon', 1998, 'green',
                     True, True)
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('cas', 'casaba', 2003, 'orange', False, False)

    cas.add_pairing('strawberries')
    cas.add_pairing('mint')
    all_melon_types.append(cas)


    cren = MelonType('cren', 'Crenshaw', 1996, 'green', False, False)
    musk.add_pairing('proscuitto')
    all_melon_types.append(cren)

    yell_mel = MelonType('yw', 'Yellow Watermelon', 2013, 'yellow', False, True)
    yell_mel.add_pairing('ice cream')
    all_melon_types.append(yell_mel)


    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon in melon_types:
    	print(f'{melon.name} Pairs With:', ', '.join(melon.pairings))


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    melons = {}
    for melon in melon_types:
    	melons[melon.code] = melon
    return melons

############
# Part 2   #
############

class Melon(object):
	def __init__(melon_type, shape_rating, color_rating, harvested_from, harvested_by)
    """A melon in a melon harvest."""

    self.melon_type = code
    self.shape_rating = shape_rating
    self.color_rating = color_rating
    self.harvested_from = harvested_from
    self.harvested_by = harvested_by
    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melon_objects = []

    mel_1 = Melon('yw', 8, 7, 'Field 2', 'Sheila')
    melon_objects.append(mel_1)

    mel_2 = Melon('yw', 3, 4, 'Field 2', 'Sheila')
    melon_objects.append(mel_2)

    mel_3 = Melon('yw', 9, 8, 'Field 3', 'Sheila')
    melon_objects.append(mel_3)

    mel_4 = Melon('cas', 10, 6, 'Field 35', 'Sheila')
    melon_objects.append(mel_4)

    mel_5 = Melon('cren', 8, 9, 'Field 35', 'Michael')
    melon_objects.append(mel_5)

    mel_6 = Melon('cren', 8, 2, 'Field 35,', 'Michael')
    melon_objects.append(mel_6)

    mel_7 = Melon('cren', 2, 3, 'Field 4', 'Michael')
    melon_objects.append(mel_7)

    mel_8 = Melon('musk', 6, 7, 'Field 4', 'Michael')
    melon_objects.append(mel_8)

    mel_9 = Melon('yw', 7, 10, 'Field', 'Sheila')
    melon_objects.append(mel_9)
    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    for melon_object in melons:
    	if melon_object.shape_rating > 5, and melon_object.color_rating > 5, and melon_object.harvested_from != 'Field 3':
    		print(f'Harvested by {melon_object.harvested_by} from {harvested_from} (CAN BE SOLD)')
    	else:
    		print(f'Harvested by {melon_object.harvested_by} from {harvested_from} (NOT SELLABLE)')
    # Fill in the rest 



