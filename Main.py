from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///flashcard.db?check_same_thread=False")  # I will use flashcard.db for SQLA
#  connection = inspect(engine)  # Unnecessary unless you are accessing an existing table (ex. get_table_names)
Base = declarative_base()  # Allows us to connect the class and database
Session = sessionmaker(bind=engine)  # Session allows us to modify the table
session = Session()


class flashcard(Base):
    __tablename__ = "flashcard"

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)


Base.metadata.create_all(engine)  # Creates the table we made above with flashcard class

while True:
    print("\n1. Add flashcards")
    print("2. Practice flashcards")
    print("3. Exit")
    choice = str(input())

    if choice == "1":
        while True:
            print("\n1. Add a new flashcard")
            print("2. Exit")
            choice = str(input())
            if choice == "1":
                question_ = ""
                answer_ = ""
                while len(question_) == 0:
                    question_ = str(input("\nQuestion: ")).strip()
                while len(answer_) == 0:
                    answer_ = str(input("Answer: ")).strip()
                flashcard_ = flashcard(question=question_, answer=answer_)  # Creates flashcard instance for SQLA
                session.add(flashcard_)  # Adds flashcard to session queue (which modifies the table
                session.commit()  # Like conn.commit or with conn but for SQLA
            elif choice == "2":
                break
            else:
                print(f"{choice} is not an option")

    elif choice == "2":
        flashcard_list = session.query(flashcard).all()
        if len(flashcard_list) == 0:
            print("There is no flashcard to practice!")
        else:
            for flashcard in flashcard_list:
                print("\nQuestion: {}".format(flashcard.question))
                selection = str(input("Please press \"y\" to see the answer or press \"n\" to skip: "))
                if selection == "y":
                    print("\nAnswer: {}".format(flashcard.answer))
                else:
                    continue

    elif choice == "3":
        print("Bye!")
        break
    else:
        print(f"{choice} is not an option")
