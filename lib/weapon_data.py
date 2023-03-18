#!/usr/bin/env python3

import yaml


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


stream = open('../data/weapons/3_6_laser.yml', 'r')
laser = yaml.safe_load(stream)
print(laser)
print(laser['name'])
print(laser['power'])
