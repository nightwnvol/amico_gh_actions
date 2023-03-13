import configparser
import argparse

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('config', type=str)
parser.add_argument('library', type=str)
parser.add_argument('library_dir', type=str)
parser.add_argument('include_dir', type=str)
args = parser.parse_args()

# write the site.cfg file
config = configparser.ConfigParser()
config[args.config] = {
    'library': args.libraries,
    'library_dir': args.library_dirs,
    'include_dir': args.include_dirs
}
with open('site.cfg', 'a') as configfile:
    config.write(configfile)
