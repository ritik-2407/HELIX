#!/usr/bin/env python



# ================== IMPORTS ==================

import subprocess
import shlex
import os
import sys

from commands.builtin import BUILTIN_COMMANDS
from commands.custom import CUSTOM_COMMANDS
from commands.aliases import ALIASES

# ================== STATE ==================

class ShellState:
    # Holds shell state (currently only cwd)
    def __init__(self):
        self.cwd = os.getcwd()

state = ShellState()



# ================== ROUTER ==================

def dispatch_command(args, state):
    cmd = args[0]

    # Built-in commands
    if cmd in BUILTIN_COMMANDS:
        BUILTIN_COMMANDS[cmd](args, state)
        return

    # Custom commands
    if cmd in CUSTOM_COMMANDS:
        CUSTOM_COMMANDS[cmd](args, state)
        return

    # OS-level commands
    subprocess.run(
        args,
        cwd=state.cwd,
        shell=False
    )

# ================== ALIASES ==================

def expand_alias(command: str) -> str:
    parts = shlex.split(command)
    if not parts:
        return command

    cmd = parts[0]
    if cmd not in ALIASES:
        return command

    expanded = ALIASES[cmd]
    rest = parts[1:]

    return " ".join([expanded] + rest)

# ================== EXECUTOR ==================

def execute_command(command: str):
    try:
        command = expand_alias(command)
        args = shlex.split(command)
        if not args:
            return

        dispatch_command(args, state)

    except FileNotFoundError:
        print(f"{RED}command not found:{RESET} {args[0]}")
    except KeyboardInterrupt:
        print()
    except Exception as e:
        print(f"{RED}error:{RESET} {e}")

# ================== MAIN LOOP ==================

def main():
    show_banner()

    while True:
        try:
            command = input(get_prompt(state))
            execute_command(command)
        except EOFError:
            print("\nExiting Helix...")
            break

# ================== ENTRY ==================

if __name__ == "__main__":
    main()
