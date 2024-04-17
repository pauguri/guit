#!/usr/bin/env python3

import subprocess
import argparse

# Llistat de traduccions (TODO: externalitzar a un csv)
command_mapping = {
    "afegeix": "add",
    "arxiva": "archive",
    "branca": "branch",
    "contempla": "checkout",
    "neteja": "clean",
    "clona": "clone",
    "compromet": "commit",
    "descriu": "describe",
    "compara": "diff",
    "cerca": "fetch",
    "inicia": "init",
    "informa": "log",
    "fusiona": "merge",
    "mou": "mv",
    "estira": "pull",
    "empeny": "push",
    "reposa": "rebase",
    "reinicia": "reset",
    "restaura": "restore",
    "recula": "revert",
    "mostra": "show",
    "desa": "stash",
    "estat": "status",
    "canvia": "switch",
    "etiqueta": "tag",
    "configura": "config",
    "remot": "remote",
}

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