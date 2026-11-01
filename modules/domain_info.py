import whois

def get_whois(domain):
    try:
        # Perform the lookup
        domain_info = whois.whois(domain)
        
        print("\n--- WHOIS Information ---")
        print(f"Registrar: {domain_info.registrar}")
        print(f"Creation Date: {domain_info.creation_date}")
        print(f"Expiration Date: {domain_info.expiration_date}")
        print(f"Name Servers: {domain_info.name_servers}")
        
    except Exception as e:
        print(f"Error retrieving WHOIS data: {e}")
