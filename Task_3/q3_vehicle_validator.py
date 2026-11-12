"""Q3: Vehicle registration number normalisation and validation.
Accepted compact pattern: 2 state letters + 2 district digits +
1 or 2 series letters + 4 registration digits.
No regular expressions are used.
"""

def normalise(text):
    cleaned = text.strip().replace(" ", "").replace("-", "")
    return cleaned.upper()

def is_valid(reg):
    if len(reg) not in (9, 10):
        return False
    if not (reg[0:2].isalpha() and reg[2:4].isdigit()):
        return False
    if len(reg) == 9:
        return reg[4:5].isalpha() and reg[5:9].isdigit()
    return reg[4:6].isalpha() and reg[6:10].isdigit()

def format_registration(reg):
    if not is_valid(reg):
        raise ValueError("Cannot format an invalid registration number")
    series_end = 5 if len(reg) == 9 else 6
    return f"{reg[0:2]} {reg[2:4]} {reg[4:series_end]} {reg[series_end:]}"

if __name__ == "__main__":
    raw_values = [
        "tn 09 ab 1234",
        "TN-09-AB-1234",
        "TN09AB1234",
        "KA-01-M-0007",
        "TN 22 1234 AB",
        "A1-09-AB-1234",
    ]
    for raw in raw_values:
        reg = normalise(raw)
        status = "valid" if is_valid(reg) else "INVALID"
        formatted = format_registration(reg) if is_valid(reg) else "not formatted"
        print(f"{raw} -> {reg} {status}; receipt: {formatted}")
    sample = "TN09AB1234"
    print("Last four characters:", sample[-4:])
    print("Slice sample[-4:-1]:", sample[-4:-1])
