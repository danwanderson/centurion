#!/usr/bin/env python3

import yaml
import os
import re


class Weapon(yaml.YAMLObject):
    yaml_tag = u'Weapon'
    yaml_loader = yaml.SafeLoader

    def __init__(self, name, damage, range, power, mass, cost):
        self.name = name
        self.damage = damage
        self.range = range
        self.power = power
        self.mass = mass
        self.cost = cost

    def __repr__(self):
        return "%s(name=%r, damage=%r, range=%r, power=%r, mass=%r, \
            cost=%r)" % (
            self.__class__.__name__, self.name, self.damage, self.range,
            self.power, self.mass, self.cost,
        )


# need to make this safer/work better if file is called
# from a weird path
weapon_data_dir = '../data/weapons'
dir_list = os.listdir(weapon_data_dir)
weapon_data = dict()

for files in dir_list:
    if '.yml' in files:
        # read file and add to dictonary
        file_stream = open(weapon_data_dir + '/' + files, 'r')
        weapon = yaml.safe_load(file_stream)
        weapon_data[weapon['name']] = weapon

for weapon in weapon_data:
    print(weapon_data[weapon])

