# Write your code here
import re

def scrape_email_addresses(string):
    return re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+', string)