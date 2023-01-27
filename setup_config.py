import configparser
import argparse

# read the arguments from the command line
parser = argparse.ArgumentParser()
parser.add_argument('config', type=str)
parser.add_argument('libraries', type=str)
parser.add_argument('library_dirs', type=str)
parser.add_argument('include_dirs', type=str)
args = parser.parse_args()

# write the config file
config = configparser.ConfigParser()
config[args.config] = {
    'libraries': args.libraries,
    'library_dirs': args.library_dirs,
    'include_dirs': args.include_dirs
}
with open('site.cfg', 'a') as configfile:
    config.write(configfile)
