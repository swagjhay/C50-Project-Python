from cs50 import get_string

def luhn_checksum(card_number):
    digits = [int(d) for d in card_number]
    checksum = 0

    for i in range(len(digits) - 2, -1, -2):
        doubled = digits[i] * 2
        if doubled > 9:
            doubled -= 9
        digits[i] = doubled
    return sum(digits) % 10 == 0
card = get_string("Number: ")

if not card.isdigit():
    print("INVALID")
elif not luhn_checksum(card):
    print("INVALID")
else:

    if len(card) == 15 and (card.startswith("34") or card.startswith("37")):
        print("AMEX")
    elif len(card) == 16 and card[:2] in ["51", "52", "53", "54","55"]:
        print("MASTERCARD")
    elif len(card) in [13,16] and card.startswith("4"):
        print("VISA")
    else:
        print("INVALID")
