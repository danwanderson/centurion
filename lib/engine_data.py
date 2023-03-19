#!/usr/bin/env python3

import yaml
import os
from natsort import natsorted


class Engine(yaml.YAMLObject):
    yaml_tag = u'!Engine'
    yaml_loader = yaml.SafeLoader

    def __init__(self, rating, mass, cost):
        self.rating = rating
        self.mass = mass
        self.cost = cost

    def __repr__(self):
        return "%s(rating=%r, mass=%r, cost=%r)" % (
            self.__class__.__name__, self.rating,
            self.mass, self.cost
        )

    @classmethod
    def get_name(self):
        return self.name



# return the rating of a engine
def get_engine_rating(engine):
    return engine.rating

def dump_engine_data(engine_data):
    for engine in natsorted(engine_data, key=get_engine_rating):
        print(engine)

# Get path of current file
lib_path = os.path.dirname(__file__)
# Add relative path to the data directory
engine_data_dir = lib_path + '/../data/engines'
# Set up a dictionary to store the data
engine_data = []

# get a list of the files in the directory
with os.scandir(engine_data_dir) as dir_list:
    for file in dir_list:
        # make sure it's a non-empty yml file
        if file.name.endswith('.yml') and file.is_file() and file.stat().st_size != 0:
            # read file and add to dictonary
            file_stream = open(engine_data_dir + '/' + file.name, 'r')
            engines = yaml.safe_load_all(file_stream)
            #if engine.rating in engine_data:
            #    print("WARNING: duplicate input detected: " + engine.rating)
            for engine in engines:
                engine_data.append(engine)

dump_engine_data(engine_data)
