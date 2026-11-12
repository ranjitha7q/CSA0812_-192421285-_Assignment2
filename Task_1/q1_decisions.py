"""Q1: Electricity subsidy eligibility and the danger of overlapping if statements."""

households = [
    {"name": "H1", "units": 100, "ration": True, "senior80": False},
    {"name": "H2", "units": 100, "ration": False, "senior80": False},
    {"name": "H3", "units": 101, "ration": True, "senior80": False},
    {"name": "H4", "units": 200, "ration": False, "senior80": False},
    {"name": "H5", "units": 201, "ration": False, "senior80": False},
    {"name": "H6", "units": 250, "ration": False, "senior80": True},
    {"name": "H7", "units": 150, "ration": False, "senior80": False},
    {"name": "H8", "units": 180, "ration": True, "senior80": True},
]

def separate_ifs_buggy(units, ration_card, senior_over_80):
    """Demonstrates a common bug: the partial condition misses its lower boundary."""
    decisions = []
    if units <= 100:
        decisions.append("FULL subsidy")
    if units <= 200 and ration_card:  # BUG: should also require units >= 101
        decisions.append("PARTIAL subsidy")
    if units > 200 and not senior_over_80:
        decisions.append("NO subsidy")
    if units > 200 and senior_over_80:
        decisions.append("SPECIAL eligibility review")
    if not decisions:
        decisions.append("NO subsidy")
    return decisions

def separate_ifs_correct(units, ration_card, senior_over_80):
    """Correct independent-if implementation with mutually exclusive ranges."""
    decisions = []
    if units <= 100:
        decisions.append("FULL subsidy")
    if 101 <= units <= 200:
        if ration_card:
            decisions.append("PARTIAL subsidy")
        else:
            decisions.append("NO subsidy")
    if units > 200:
        decisions.append("SPECIAL eligibility review" if senior_over_80 else "NO subsidy")
    return decisions

def chained_decision(units, ration_card, senior_over_80):
    if units <= 100:
        return "FULL subsidy"
    elif units <= 200:
        return "PARTIAL subsidy" if ration_card else "NO subsidy"
    else:
        return "SPECIAL eligibility review" if senior_over_80 else "NO subsidy"

if __name__ == "__main__":
    print("Q1 - Electricity Subsidy Eligibility")
    print("H | Units | Ration | Senior>80 | Buggy separate if | Correct separate if | if-elif-else")
    for h in households:
        args = (h["units"], h["ration"], h["senior80"])
        a = ", ".join(separate_ifs_buggy(*args))
        b = ", ".join(separate_ifs_correct(*args))
        c = chained_decision(*args)
        print(f'{h["name"]} | {h["units"]} | {h["ration"]} | {h["senior80"]} | {a} | {b} | {c}')
