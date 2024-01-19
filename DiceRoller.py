import random

#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
#● ┌ ─ ┐ │ └ ┘


dice_design={
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│ ●       │",
        "│     ●   │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│         │",
        "│  ● ● ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ ●   ●   │",
        "│ ●   ●   │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ ●  ●  ● │" 
        "│ ●     ● │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ● ● ●  │",
        "│  ● ● ●  │",
        "└─────────┘")
}

dice = []
total = 0
num_of_dice = int(input("how many dice?:"))

for x in range(num_of_dice):
    dice.append(random.randint(1, 6))

for line in range(4):
    for x in dice:
        print(dice_design.get(x)[line], end="")
    print()

for x in dice:
    total += x
print(f"total: {total}")