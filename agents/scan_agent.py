def run_scan(name, email):
    # Placeholder logic – to be replaced with real scraping/search API
    results = [
        {'type': 'Data Broker', 'source': 'Spokeo', 'link': f'https://www.spokeo.com/{name.replace(" ", "-")}'},
        {'type': 'Leak Check', 'source': 'HaveIBeenPwned', 'link': f'https://haveibeenpwned.com/unifiedsearch/{email}'},
    ]
    return results
