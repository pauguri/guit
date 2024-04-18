#!/usr/bin/env python3

import subprocess
import argparse

# Importar llistat de traduccions
with open("traduccio.csv", "r") as file:
    command_mapping = dict(line.strip().split(",") for line in file)

def main():
    parser = argparse.ArgumentParser(description="Git en català")
    parser.add_argument("command", choices=command_mapping.keys(), help="Escull una comanda de Git en català")
    parser.add_argument("args", nargs=argparse.REMAINDER, help="Arguments addicionals de Git")
    args = parser.parse_args()

    git_command = command_mapping[args.command]
    git_command_with_args = ["git", git_command] + args.args
    subprocess.run(git_command_with_args)

if __name__ == "__main__":
    main()