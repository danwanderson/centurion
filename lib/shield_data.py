#!/usr/bin/env python3

import yaml
import os
from natsort import natsorted


class Shield(yaml.YAMLObject):
    yaml_tag = u'!Shield'
    yaml_loader = yaml.SafeLoader

    def __init__(self, flicker_rate, power, mass, cost):
        self.flicker_rate = flicker_rate
        self.power = power
        self.mass = mass
        self.cost = cost

    def __repr__(self):
        return "%s(flicker_rate=%r, power=%r, mass=%r, cost=%r)" % (
            self.__class__.__name__, self.flicker_rate,
            self.power, self.mass, self.cost
        )

    @classmethod
    def get_name(self):
        return self.name


# return the flicker_rate of a shield
def get_shield_flicker_rate(shield):
    return shield.flicker_rate


def dump_shield_data(shield_data):
    for shield in natsorted(shield_data, key=get_shield_flicker_rate):
        print(shield)


def read_shield_data():
    # Get path of current file
    lib_path = os.path.dirname(__file__)
    # Add relative path to the data directory
    shield_data_dir = lib_path + '/../data/shields'
    # Set up a dictionary to store the data
    shield_data = []

    # get a list of the files in the directory
    with os.scandir(shield_data_dir) as dir_list:
        for file in dir_list:
            # make sure it's a non-empty yml file
            if file.name.endswith('.yml') and file.is_file() and file.stat().st_size != 0:
                # read file and add to dictonary
                file_stream = open(shield_data_dir + '/' + file.name, 'r')
                shields = yaml.safe_load_all(file_stream)
                #if shield.flicker_rate in shield_data:
                #    print("WARNING: duplicate input detected: " + shield.flicker_rate)
                for shield in shields:
                    shield_data.append(shield)
    return shield_data

#dump_shield_data(shield_data)
