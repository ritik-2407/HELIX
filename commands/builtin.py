import os


def cd(args, state):
    if len(args) == 1:
        target = os.path.expanduser("~")
    else:
        target = args[1]

    new_path = os.path.abspath(
        os.path.join(state.cwd, target)
    )

    if not os.path.isdir(new_path):
        print(f"cd: no such directory: {target}")
        return

    state.cwd = new_path


def pwd(args, state):
    print(state.cwd)


BUILTIN_COMMANDS = {
    "cd": cd,
    "pwd": pwd,
}
