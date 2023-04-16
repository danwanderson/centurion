#!/usr/bin/env python3

import sys
sys.path.append('..')

from lib.weapon_data import read_weapon_data, dump_weapon_data # noqa E402
from lib.engine_data import read_engine_data, dump_engine_data # noqa E402
from lib.shield_data import read_shield_data, dump_shield_data # noqa E402


def main(*argv, **kwargs):
    """ Main function """
    # Read databases
    weapon_data = read_weapon_data()
    dump_weapon_data(weapon_data)
    engine_data = read_engine_data()
    dump_engine_data(engine_data)
    shield_data = read_shield_data()
    dump_shield_data(shield_data)

    # Read vehicle database
    #vehicle_data = vehicle_data.read_vehicle_data()

    # Print menu
    #print_menu()

    # Read user input
    while True:
        user_input = input("> ")
        if user_input == "q":
            break
        else:
            print("Unknown command: " + user_input)

# main function
# read databases (weapon_data, engram_data, shield_data)
# Read vehicle database
# print menu

if __name__ == "__main__":
    main()