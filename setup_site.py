import configparser
import argparse
import shutil

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('config', type=str, help='Config section name')
parser.add_argument('library', type=str, help='Library name')
parser.add_argument('library_dir', type=str, help='Library directory path')
parser.add_argument('include_dir', type=str, help='Include directory path')
args = parser.parse_args()

# write the site.cfg file
config = configparser.ConfigParser()
config[args.config] = {
    'library': args.library,
    'library_dir': args.library_dir,
    'include_dir': args.include_dir
}
shutil.copyfile('site.cfg.example', 'site.cfg')
with open('site.cfg', 'a') as configfile:
    config.write(configfile)
