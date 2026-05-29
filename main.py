"""
Caesar Cipher CLI Interface
---------------------------
An interactive command-line interface (CLI) for the Caesar Cipher utility.
Features menu-driven navigation, colored terminal logging, input validation,
and cross-platform ANSI color initialization.
"""

import sys
import os
from caesar_cipher import encrypt, decrypt

# ANSI color escape sequences for a professional CLI aesthetic
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"


def initialize_terminal():
    """
    Initializes terminal for ANSI color codes.
    Specifically enables virtual terminal processing on Windows platforms.
    """
    if os.name == "nt":
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            # ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
        except Exception:
            # Fallback: run empty command to trigger color processing in some shells
            os.system("")


def print_banner():
    """Prints a professional, styled ASCII art banner for the application."""
    banner = f"""
{CYAN}{BOLD}======================================================================
     ____                  ___              ____ _       __               
    / __ \\_________  _____/ (_)___ ___  __ / ___(_)___  / /_  ___  _____  
   / /_/ / ___/ __ \\/ __  / / __  / / / / / /   / / __ \\/ __ \\/ _ \\/ ___/  
  / ____/ /  / /_/ / /_/ / / /_/ / /_/ / / /___/ / /_/ / / / /  __/ /      
 /_/   /_/   \\____/\\____/_/\\__, /\\__, /  \\____/_/ .___/_/ /_/\\___/_/       
                          /____//____/         /_/                         
                  - CYBERSECURITY INTERNSHIP TASK-01 -
                      Caesar Cipher Cryptotool
======================================================================{RESET}
"""
    print(banner)


def get_shift_value() -> int:
    """
    Prompts the user for a shift value and validates that it is a valid integer.
    Repeats the prompt until a valid integer is provided.

    :return: The validated integer shift value.
    """
    while True:
        try:
            user_input = input(f"{YELLOW}{BOLD}Enter shift value (integer key): {RESET}").strip()
            if not user_input:
                print(f"{RED}[Error] Shift value cannot be empty. Please enter an integer.{RESET}\n")
                continue
            return int(user_input)
        except ValueError:
            print(f"{RED}[Error] '{user_input}' is not a valid integer. Please enter an integer key.{RESET}\n")


def execute_action(choice: str):
    """
    Executes the cryptographic action based on the user's choice.

    :param choice: String value '1' (Encrypt) or '2' (Decrypt).
    """
    mode_name = "Encryption" if choice == "1" else "Decryption"
    print(f"\n{MAGENTA}{BOLD}--- {mode_name} Mode ---{RESET}")
    
    # Prompt user for the message to be processed
    message = input(f"{YELLOW}Enter the message to {mode_name.lower()}:\n{RESET}").strip()
    
    if not message:
        print(f"{RED}[Error] The input message cannot be empty.{RESET}")
        return
        
    shift = get_shift_value()
    
    # Perform encryption or decryption
    if choice == "1":
        result = encrypt(message, shift)
        print(f"\n{GREEN}{BOLD}Plaintext: {RESET} {message}")
        print(f"{GREEN}{BOLD}Shift Key: {RESET} {shift}")
        print(f"{GREEN}{BOLD}Ciphertext:{RESET} {result}")
    else:
        result = decrypt(message, shift)
        print(f"\n{GREEN}{BOLD}Ciphertext:{RESET} {message}")
        print(f"{GREEN}{BOLD}Shift Key: {RESET} {shift}")
        print(f"{GREEN}{BOLD}Plaintext: {RESET} {result}")
        
    print(f"{CYAN}======================================================================{RESET}")


def main():
    """Main loop driving the menu-driven command line interface."""
    initialize_terminal()
    print_banner()

    while True:
        print(f"\n{BOLD}Select an Option from the Menu:{RESET}")
        print(f"  [{GREEN}1{RESET}] {BOLD}Encrypt{RESET} a message")
        print(f"  [{GREEN}2{RESET}] {BOLD}Decrypt{RESET} a message")
        print(f"  [{RED}3{RESET}] {BOLD}Exit{RESET} program")
        
        choice = input(f"\n{YELLOW}{BOLD}Choose (1-3): {RESET}").strip()

        if choice in ("1", "2"):
            execute_action(choice)
        elif choice == "3":
            print(f"\n{CYAN}{BOLD}Thank you for using the Caesar Cipher tool! Secure coding!{RESET}")
            sys.exit(0)
        else:
            print(f"{RED}[Error] Invalid selection '{choice}'. Please select option 1, 2, or 3.{RESET}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{RED}[Interrupted] Program terminated by user. Exiting...{RESET}")
        sys.exit(0)