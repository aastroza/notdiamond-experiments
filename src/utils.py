import re

def extract_response(s):
    digits = re.findall(r'\d+', s)
    for d in digits:
        if d == '0' or d == '1':
            return int(d)
    
    return -1