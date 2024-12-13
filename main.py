from gui import *
import pandas as pd
import os


# Sets up initial csv file for processing. Done on start of application.
def setup() -> None:
    """
    Creates the CSV file where votes are saved
    """
    df = pd.DataFrame({'ID': [], 'Vote': []})
    df.to_csv('votes.csv', index=False)


# Runs the application
def main() -> None:
    """
    Initialize the tkinter app
    """
    window = Tk()
    window.title('Voting')
    window.geometry('400x600')
    window.resizable(False, False)

    Gui(window)
    window.mainloop()


if __name__ == '__main__':
    setup()
    main()