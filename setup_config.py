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
    'library': args.library,
    'library_dir': args.library_dir,
    'include_dir': args.include_dir
}
with open('site.cfg', 'a') as configfile:
    config.write(configfile)
