import requests

def check_domain(domain):
    # HIBP public endpoint for checking breaches associated with a specific domain
    api_url = f"https://haveibeenpwned.com/api/v3/breaches?domain={domain}"
    
    headers = {
        "User-Agent": "Spiderecon-OSINT-Tool"
    }
    
    print(f"\n[*] Querying public records for breaches associated with {domain}...")
    
    try:
        response = requests.get(api_url, headers=headers, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            if data:
                print(f"[!] WARNING: {len(data)} breach(es) found for {domain}:\n")
                for breach in data:
                    print(f"--- {breach.get('Title')} ---")
                    print(f"Breach Date:      {breach.get('BreachDate')}")
                    print(f"Records Leaked:   {breach.get('PwnCount'):,}")
                    print(f"Compromised Data: {', '.join(breach.get('DataClasses', []))}\n")
            else:
                # The API returned an empty list, meaning no breaches match this domain
                print(f"[+] Good news: No known breaches found for {domain}.")
                
        elif response.status_code == 404:
            print(f"[+] Good news: No known breaches found for {domain}.")
            
        else:
            print(f"[-] API Error: The server returned status code {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"[-] Error connecting to Breach API: {e}")
