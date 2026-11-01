import requests
import sys
import concurrent.futures

def check_url(target_url, headers):
    """Worker function that handles a single HTTP request."""
    try:
        response = requests.get(target_url, headers=headers, timeout=3, allow_redirects=False)
        if response.status_code == 200:
            return f"[+] Found (200): {target_url}"
        elif response.status_code == 403:
            return f"[-] Forbidden (403): {target_url}"
        elif response.status_code in [301, 302]:
            return f"[~] Redirect ({response.status_code}): {target_url} -> {response.headers.get('Location')}"
    except requests.exceptions.RequestException:
        pass
    return None

def enumerate(url, wordlist_path):
    if not url.endswith('/'):
        url += '/'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    try:
        # Read all lines into memory first so we can distribute them to threads
        with open(wordlist_path, 'r') as file:
            lines = [line.strip() for line in file.readlines()]
            
        total_words = len(lines)
        print(f"\n[*] Loaded {total_words} words. Starting fast multithreaded scan...\n")
        
        completed = 0
        
        # Launch 20 concurrent threads (adjust max_workers to go faster or slower)
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            # Submit all tasks to the thread pool
            futures = {executor.submit(check_url, f"{url}{word}", headers): word for word in lines}
            
            # Process results as soon as each thread finishes
            for future in concurrent.futures.as_completed(futures):
                completed += 1
                
                # Update progress bar
                sys.stdout.write(f"\rProgress: [{completed}/{total_words}] requests sent...".ljust(60))
                sys.stdout.flush()
                
                # If the worker function returned a hit, clear the line and print it
                result = future.result()
                if result:
                    sys.stdout.write("\r" + " " * 60 + "\r")
                    print(result)
                    
        print("\n\n[*] Enumeration complete.")
                    
    except FileNotFoundError:
        print(f"\n[-] Error: Wordlist not found at {wordlist_path}")
