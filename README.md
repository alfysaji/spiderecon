# Spiderecon

> *"Learning is the exploit that never gets patched."*

Spiderecon is a fast, modular Open-Source Intelligence (OSINT) and web reconnaissance tool. It combines multithreaded directory fuzzing, domain registration analysis, and historical data breach checking into a single, interactive command-line interface.

## Features
* **Directory Enumeration:** High-speed, multithreaded directory brute-forcing to discover hidden web paths.
* **WHOIS & Domain Info:** Retrieves registrar details, creation/expiration dates, and name servers for target domains.
* **Data Breach Check:** Queries public databases to see if a domain has been compromised in historical data leaks.

## Prerequisites
* Python 3
* A Linux environment (e.g., Kali Linux)

## Installation Guide
Run the following commands in your terminal to download and install the tool globally on your system:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/alfysaji/spiderecon.git](https://github.com/alfysaji/spiderecon.git)Navigate into the directory:
   Navigate into the directory:

Bash
cd spiderecon
Make the installer executable:

Bash
chmod +x install.sh
Run the automated install script:

Bash
sudo ./install.sh
Usage
Once installed, the installer handles the virtual environment and dependencies automatically. You can launch the interactive menu from any directory in your terminal by simply typing:

Bash
spiderecon ''' 
