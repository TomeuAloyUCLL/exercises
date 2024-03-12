# Write your code here
import re

def is_valid_time(string):
    return re.fullmatch(r'([01]\d|[2][0-3]):([0-5]\d):([0-5]\d)(.[\d]{3})?', string)