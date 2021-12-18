def possible_cards(base, number):
    i = 0
    while i <= number:
        yield base + i
        i += 1

def possible_pins(base, number):
    i = 0
    while i <= number:
        yield base + i
        i += 1

card_gen = possible_cards(4000000000000000, 9999999999)
pin_gen = possible_pins(0000, 9999)

while True: #TODO think about correct loop
    card = next(card_gen)
    while True:
        pin = next(pin_gen)
        print(f"Card number: {card}")
        print(f"Pin: {pin}")


