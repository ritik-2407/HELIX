from shell.executor import execute_command

def start_repl():
    print("Hello this is the test")
    print("type exit to quit")

    while True:
        try:
            raw = input("> ").strip()
            if not raw:
                continue
            if raw == "exit":
                break

            execute_command(raw)
                
        except KeyboardInterrupt:
            print("\nexit")
            break