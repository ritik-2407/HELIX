import subprocess
import shlex

def execute_command(command : str):
    try:
        args = shlex.split(command)

        #temporary placeholder for custom commands 
        if args[0] in {"ss" , "github" , "leetcode"}:
            print(f"[custom command detected] -> {args[0]}")
            return

        subprocess.run(
            args,
            shell=False
        )

    except FileNotFoundError:
        print(f"command not found: {args[0]}")
    except Exception as e:
        print(f"error: {e}")