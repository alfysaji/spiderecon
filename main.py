import sys
from modules import directory, domain_info, breach_check

def main():
    while True:
        print("\n" + "="*40)
        print("           SPIDERECON TOOL")
        print("="*40)
        print("1. Directory Enumeration (Fast Scan)")
        print("2. WHOIS & Domain Info")
        print("3. Data Breach Check")
        print("4. Exit")
        print("="*40)
        
        choice = input("\nSelect an option (1-4): ").strip()
        
        if choice == '1':
            url = input("[?] Enter target URL (e.g., https://example.com): ").strip()
            wordlist = input("[?] Enter wordlist path (e.g., /usr/share/wordlists/dirb/common.txt): ").strip()
            directory.enumerate(url, wordlist)
            
        elif choice == '2':
            domain = input("[?] Enter target domain (e.g., example.com): ").strip()
            domain_info.get_whois(domain)
            
        elif choice == '3':
            domain = input("[?] Enter website domain to check (e.g., adobe.com): ").strip()
            breach_check.check_domain(domain)
            
        elif choice == '4':
            print("[*] Exiting Spiderecon. Goodbye!")
            sys.exit(0)
            
        else:
            print("[-] Invalid choice, please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Handles the user pressing Ctrl+C cleanly
        print("\n[*] Exiting Spiderecon...")
        sys.exit(0)
