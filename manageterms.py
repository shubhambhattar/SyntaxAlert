#!/usr/bin/env python3
import argparse, os.path
from utils.data_handlers import open_typo_file, save_typo_data

# Parse argument
parser = argparse.ArgumentParser(description='add new terms!')

parser.add_argument('-wrong', dest="wrong", type=str, required=True)
parser.add_argument('-right', dest="right", type=str, required=True)
parser.add_argument('-lang', dest="lang", type=str, required=True)
args = parser.parse_args()

script_path = os.path.dirname(os.path.realpath(__file__))
lang_path = script_path + '/words/' + args.lang + '.json'

typo_data = open_typo_file(lang_path)
typo_data[args.right].add(args.wrong)

save_typo_data(lang_path, typo_data)
