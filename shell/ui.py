import time
import os
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.live import Live
from rich.table import Table

console = Console()

# ================== THEME ==================
HEX_GREEN = "#00FF41" 
HEX_CYAN = "#00FFFF"

def boot_sequence():
    """Simulates a system breach sequence."""
    tasks = [
        "BYPASSING KERNEL...",
        "INJECTING SHELLCODE...",
        "DECRYPTING RSA-4096...",
        "ESTABLISHING TUNNEL..."
    ]
    
    # Using 'Progress' instead of 'Tracked'
    with Live(auto_refresh=True) as live:
        for task in tasks:
            time.sleep(0.3)
            grid = Table.grid(expand=True)
            grid.add_row(f"[bold {HEX_GREEN}][⚡][/] {task}")
            live.update(Panel(grid, border_style=HEX_GREEN))
    console.clear()

def show_banner():
    # ASCII Art with a neon glow effect
    banner_text = (
        " ██░ ██ ▓█████  ██▓     ██▓ ▒██   ██▒\n"
        "▓██░ ██▒▓█   ▀ ▓██▒    ▓██▒ ▒▒ █ █ ▒░\n"
        "▒██▀▀██░▒███   ▒██░    ▒██▒ ░  █   ░ \n"
        "░▓█ ░ ██ ▒▓█  ▄ ▒██░    ░██░  █ █ █  \n"
        "░▓█▒░ ██▓░▒████▒░██████▒░██░▒██▒ ▒██▒\n"
        " ▒ ░░ ▒░░░ ▒░ ░░ ▒░▓  ░░▓  ▒ ▒░ ░ ░ \n"
    )
    
    panel = Panel(
        Text(banner_text, style=f"bold {HEX_GREEN}"),
        title=f"[bold white]SYSTEM ACCESS GRANTED[/]",
        subtitle=f"[{HEX_CYAN}]SECURE LINE: 127.0.0.1[/]",
        border_style=HEX_GREEN,
        padding=(1, 4)
    )
    console.print(panel)

def get_prompt(state):
    t = time.strftime("%H:%M:%S")

    # Use shell state, NOT os.getcwd()
    path = state.cwd.replace(os.path.expanduser("~"), "~")
    
    # Modern angled prompt
    return f"\n[bold black on {HEX_GREEN}] {t} [/][bold {HEX_GREEN} on #1a1a1a][/] [bold cyan]{path}[/] \n[bold {HEX_GREEN}]>>[/] "