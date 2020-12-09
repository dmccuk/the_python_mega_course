import glob
from pathlib import Path

def get_quote(feel):
    feel = feel.lower()
    print(feel)
    available_feelings = glob.glob("quotes/*txt")
    print(available_feelings)
    available_feelings = [Path(filename).stem for filename in available_feelings]
    print(available_feelings)
        
    if feel in available_feelings:
        print(feel)
        with open(f"quotes/{feel}.txt", encoding="utf-8") as file:
            quotes = file.readlines()
        print(quotes)

print(get_quote("happy"))