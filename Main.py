import sqlite3

conn = sqlite3.connect("cards.db")
curr = conn.cursor()

with conn:
    conn.execute("""CREATE TABLE IF NOT EXISTS cards (
        term TEXT,
        definition TEXT
    );""")

while True:
<<<<<<< HEAD
    print("\n1. Add flashcards")
=======
    print("1. Add flashcards")
>>>>>>> 26c2eb721d36ed5fb79dc01063d9ecc6535dfca4
    print("2. Practice flashcards")
    print("3. Exit")
    choice = str(input())

    if choice == "1":
        while True:
            print("\n1. Add a new flashcard")
            print("2. Exit")
            choice = str(input())
            if choice == "1":
                question = ""
                answer = ""
                while len(question) == 0:
                    question = str(input("\nQuestion: ")).strip()
                while len(answer) == 0:
                    answer = str(input("Answer: ")).strip()
                with conn:
                    conn.execute("INSERT INTO cards VALUES (?, ?)", (question, answer))
            elif choice == "2":
                break
            else:
                print(f"{choice} is not an option")

    elif choice == "2":
        with conn:
            cards = conn.execute("SELECT * FROM cards").fetchall()
<<<<<<< HEAD
            if len(cards) == 0:
                print("\nThere is no flashcard to practice!")
=======
            if cards is None:
                print("There is no flashcard to practice!")
>>>>>>> 26c2eb721d36ed5fb79dc01063d9ecc6535dfca4
            else:
                for card in cards:
                    print("\nQuestion: {}".format(card[0]))
                    selection = str(input("Please press \"y\" to see the answer or press \"n\" to skip: "))
                    if selection == "y":
                        print("\nAnswer: {}".format(card[1]))
                    else:
                        continue

    elif choice == "3":
        print("Bye!")
        break
    else:
        print(f"{choice} is not an option")
