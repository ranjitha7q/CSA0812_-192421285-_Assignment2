"""Q2: OTP verification using while and for loops."""

CORRECT_OTP = "482913"
CORRECT_SECURITY_ANSWER = "blue"

def verify_with_while(entries, security_answer=None):
    attempts = 0
    max_attempts = 3
    extra_used = False
    for entry in entries:
        if entry.strip() == "":
            print("Blank entry ignored; attempt not counted.")
            continue
        if entry.strip() == CORRECT_OTP:
            print("OTP verified successfully.")
            return True
        attempts += 1
        print(f"Wrong OTP. Attempts used: {attempts}/{max_attempts}")
        if attempts == max_attempts:
            if security_answer and security_answer.lower() == CORRECT_SECURITY_ANSWER and not extra_used:
                max_attempts += 2
                extra_used = True
                print("Security answer correct. Two extra attempts granted.")
            else:
                print("Account locked for 30 minutes.")
                return False
    print("Input sequence ended before successful verification.")
    return False

def verify_with_for(entries, security_answer=None):
    attempts = 0
    extra_attempts = 2 if security_answer and security_answer.lower() == CORRECT_SECURITY_ANSWER else 0
    total_attempts = 3 + extra_attempts
    for entry in entries:
        if entry.strip() == "":
            print("Blank entry ignored; attempt not counted.")
            continue
        if entry.strip() == CORRECT_OTP:
            print("OTP verified successfully.")
            return True
        attempts += 1
        print(f"Wrong OTP. Attempts used: {attempts}/{total_attempts}")
        if attempts >= total_attempts:
            print("Account locked for 30 minutes.")
            break
    else:
        print("All supplied entries were processed; no successful OTP.")
    return False

if __name__ == "__main__":
    print("WHILE LOOP DEMO")
    verify_with_while(["", "111111", "222222", "333333"])
    print("\\nFOR LOOP DEMO WITH SECURITY QUESTION")
    verify_with_for(["111111", "", "222222", "333333", "482913"], "blue")
    print("\\nSuccessful attempt demo")
    verify_with_while(["", "482913"])
