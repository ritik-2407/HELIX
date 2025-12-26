import subprocess
import shlex
import os

class ShellState:
                                    #this part just holds the state or  contains current working direcotry(cwd)
    def __init__(self):
        self.cwd = os.getcwd()      #just abject which holds the current working direcotry

state = ShellState()


def execute_command(command : str):
    try:
        args = shlex.split(command)
        cmd = args[0]

        if cmd == 'cd':
            change_directory(args)
            return 

        subprocess.run(
            args,
            cwd=state.cwd,          #whenever subprocess runs a command , run in this cwd , this is to ensure that after cd in the future , the command runs in that direcotry not this one
            shell=False
        )

    except FileNotFoundError:
        print(f"command not found: {args[0]}")
    except Exception as e:
        print(f"error: {e}")


def change_directory(args):
    if len(args) == 1:
        target = os.path.expanduser("~")
    else:
        target = args[1]

    new_path = os.path.abspath(os.path.join(state.cwd, target))

    if not os.path.isdir(new_path):
        print(f"cd: no such directory: {target}")
        return

    state.cwd = new_path