"""
MRX - MARCH 2026.
"""
import requests

URL = "http://url-of-the.chall/vjfYkHzyZGJ4A7cPNutFeM/flag"

def main():
    r = requests.get(URL)
    print(r.text)

if __name__ == "__main__":
    main()
