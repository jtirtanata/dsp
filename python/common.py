import re

def fetch_title(full_title):
    match = re.fullmatch(r'([A-Z][\w-]*(\s+[A-Z][\w-]*)*)\s+(\w){2}\s+(Biostatistics)', full_title)
    return match.group(1)
