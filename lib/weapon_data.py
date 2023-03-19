#!/usr/bin/env python3

import yaml
import os
from natsort import natsorted


class Weapon(yaml.YAMLObject):
    yaml_tag = u'!Weapon'
    yaml_loader = yaml.SafeLoader

    def __init__(self, name, type, damage, range, power, mass, cost, ammo_type):
        self.name = name
        self.type = type
        self.damage = damage
        self.range = range
        self.power = power
        self.mass = mass
        self.cost = cost
        self.ammo_type = ammo_type

    def __repr__(self):
        return "%s(name=%r, type=%r, damage=%r, range=%r, power=%r, mass=%r, cost=%r, ammo_type=%r)" % (
            self.__class__.__name__, self.name, self.type, self.damage, self.range,
            self.power, self.mass, self.cost, self.ammo_type,
        )

    @classmethod
    def get_name(self):
        return self.name



# return the type of a weapon
def get_weapon_type(weapon):
    return weapon.type

# return the name of a weapon
def get_weapon_name(weapon):
    return weapon.name

def dump_weapon_data(weapon_data):
    # get a unique list of weapon types
    weapon_types = []
    for weapon in sorted(weapon_data, key=get_weapon_type):
        if weapon.type not in weapon_types:
            weapon_types.append(weapon.type)

    # For each weapon type, generate a sorted list and print it
    for type in weapon_types:
        items=[]
        for weapon in weapon_data:
            if type in weapon.type:
                items.append(weapon)
        for weapon in natsorted(items, key=get_weapon_name):
            print(weapon)

# Get path of current file
lib_path = os.path.dirname(__file__)
# Add relative path to the data directory
weapon_data_dir = lib_path + '/../data/weapons'
# Set up a dictionary to store the data
weapon_data = []

# get a list of the files in the directory
with os.scandir(weapon_data_dir) as dir_list:
    for file in dir_list:
        # make sure it's a non-empty yml file
        if file.name.endswith('.yml') and file.is_file() and file.stat().st_size != 0:
            # read file and add to dictonary
            file_stream = open(weapon_data_dir + '/' + file.name, 'r')
            weapon = yaml.safe_load(file_stream)
            if weapon.name in weapon_data:
                print("WARNING: duplicate input detected: " + weapon.name)
            weapon_data.append(weapon)

dump_weapon_data(weapon_data)
