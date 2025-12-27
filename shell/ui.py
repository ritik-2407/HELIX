# ================== THEME ==================

GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

# ================== UI ==================

def show_banner():
    print(GREEN)
    print("╔══════════════════════════╗")
    print("║        HELIX ⚡          ║")
    print("║   Custom Python Shell   ║")
    print("╚══════════════════════════╝")
    print(RESET)

GREEN = "\033[92m"
RESET = "\033[0m"

def get_prompt(state):
    return f"{GREEN}helix{RESET} > "

