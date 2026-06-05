import random

quotes = {
    "motivation": [
        "Push yourself, because no one else is going to do it for you.",
        "Don’t stop until you’re proud.",
        "Success starts with self-discipline.",
        "Small progress is still progress.",
        "Dream it. Wish it. Do it."
    ],

    "life": [
        "Life is what happens when you're busy making other plans.",
        "Happiness depends upon ourselves.",
        "Turn your wounds into wisdom.",
        "Every moment is a fresh beginning.",
        "Live the life you imagine."
    ],

    "success": [
        "Success is not final, failure is not fatal.",
        "Opportunities don’t happen, you create them.",
        "Work hard in silence, let success make the noise.",
        "Don’t watch the clock; do what it does. Keep going.",
        "Success usually comes to those who are too busy to be looking for it."
    ]
}

def generate_quote(category):
    return random.choice(quotes[category])


def main():
    print("=== QUOTE GENERATOR ===")

    while True:
        print("\nCategories:")
        print("1. Motivation")
        print("2. Life")
        print("3. Success")

        choice = input(">> ")

        if choice == "1":
            category = "motivation"
        elif choice == "2":
            category = "life"
        elif choice == "3":
            category = "success"
        else:
            print("Invalid choice!")
            continue

        quote = generate_quote(category)

        print("\n--- Quote ---")
        print(f"\"{quote}\"")

        # Save option
        save = input("\nSave? (y/n): ")
        if save.lower() == 'y':
            with open("quotes.txt", "a") as f:
                f.write(quote + "\n")
            print("Saved!")

        again = input("\nAgain? (y/n): ")
        if again.lower() != 'y':
            break


if __name__ == "__main__":
    main()