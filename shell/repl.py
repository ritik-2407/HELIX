import sys
from shell.executor import execute_command, state
from shell.ui import show_banner, get_prompt

def start_repl():
    show_banner()

    while True:
        try:
            raw = input(get_prompt(state)).strip()

            if not raw:
                continue

            if raw in ("exit", "quit"):
                print("Exiting Helix...")
                break

            execute_command(raw)

        except KeyboardInterrupt:
            # Ctrl+C → new line, shell survives
            print()
            continue

        except EOFError:
            # Ctrl+D
            print("\nExiting Helix...")
            break
