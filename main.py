from agents.scan_agent import run_scan

if __name__ == '__main__':
    name = input('Enter your name: ')
    email = input('Enter your email: ')
    results = run_scan(name, email)
    print('\nScan Results:')
    for result in results:
        print(result)
