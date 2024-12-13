from tkinter import *
import voting


class Gui:
    def __init__(self, window):
        """
            Builds the UI from tkinker for the voting

            Attributes:
                window (Tk): The main Tkinter window.
                    frame_vote (Frame): Frame containing voter input elements.
                        label_vote (Label): Label prompting for votes.
                        label_vote_id (Label): Label for voter ID.
                        entry_vote_id (Entry): Entry box for voter ID.
                    radio_1 (IntVar): Variable to store the selected voting option.
                    frame_vote_1, frame_vote_2, frame_vote_3 (Frame): Frames containing radio buttons.
                        radio_opt_1, radio_opt_2, radio_opt_3 (Radiobutton): Radio buttons for voting options.
                    frame_button_vote (Frame): Frame for the "Cast Vote" button.
                    button_compute (Button): Button to cast a vote.
                    frame_result (Frame): Frame to display voting results.
                    label_result (Label): Label displaying results or messages.
                    frame_button (Frame): Frame for the "Finalize Voting" button.
                    button_compute (Button): Button to finalize voting and calculate results.
            """
        self.window = window

        # Voting Block
        self.frame_vote = Frame(self.window)
        self.label_vote = Label(self.frame_vote, text='Vote Now!\t')
        self.label_vote_id = Label(self.frame_vote, text='Voter ID: \t')
        self.entry_vote_id = Entry(self.frame_vote)

        self.entry_vote_id.pack(side='right')
        self.label_vote_id.pack(side='right')
        self.label_vote.pack(side='left', padx=5)
        self.frame_vote.pack(anchor='w', pady=10)

        # Radio Buttons
        self.radio_1 = IntVar()
        self.radio_1.set(0)
        self.frame_vote_1 = Frame(self.window)
        self.radio_opt_1 = Radiobutton(self.frame_vote_1, text='Bianca', variable=self.radio_1, value=1)

        self.frame_vote_2 = Frame(self.window)
        self.radio_opt_2 = Radiobutton(self.frame_vote_2, text='Edward', variable=self.radio_1, value=2)

        self.frame_vote_3 = Frame(self.window)
        self.radio_opt_3 = Radiobutton(self.frame_vote_3, text='Felicia', variable=self.radio_1, value=3)

        self.radio_opt_1.pack(side='left')
        self.radio_opt_2.pack(side='left')
        self.radio_opt_3.pack(side='left')
        self.frame_vote_1.pack(anchor='w', padx=5)
        self.frame_vote_2.pack(anchor='w', padx=5)
        self.frame_vote_3.pack(anchor='w', padx=5)

        # Vote button
        self.frame_button_vote = Frame(self.window)
        self.label_empty1 = Label(self.frame_button_vote, text='\t\t\t')
        self.button_compute = Button(self.frame_button_vote, text='Cast Vote', command=self.vote)
        self.label_empty1.pack(side='left')
        self.button_compute.pack(side='right', padx=60)
        self.frame_button_vote.pack()

        # Results label
        self.frame_result = Frame(self.window)
        self.label_result = Label(self.frame_result)
        self.label_result.pack(pady=10)
        self.frame_result.pack()

        # Compute button
        self.frame_button = Frame(self.window)
        self.button_compute = Button(self.frame_button, text='Finalize Voting', command=self.finalize_vote)
        self.button_compute.pack(pady=50)
        self.frame_button.pack()

    def vote(self) -> None:
        """
        Handles the vote casting, Validates IDs and display messages.
        :return:
        """
        id = str(self.entry_vote_id.get())
        vote = self.radio_1.get()

        if vote == 0:
            self.label_result.config(text='Please select a voting option.')
        else:
            if vote == 1:
                vote_name = 'Bianca'
            elif vote == 2:
                vote_name = 'Edward'
            elif vote == 3:
                vote_name = 'Felicia'

            if id == '':
                self.label_result.config(text='Please input a valid ID')
            else:
                valid = voting.cast_vote(id, vote)
                if valid:
                    self.label_result.config(text=f'You voted for {vote_name}')
                else:
                    self.label_result.config(text=f'{id}: This ID has already voted')
        self.radio_1.set(0)
        self.entry_vote_id.delete(0, END)

    def finalize_vote(self) -> None:
        """
         Calculate and display the results of voting.
        """
        result = voting.count_votes()
        winner = result[0]
        count = result[1]
        if winner == 1:
            self.label_result.config(text=f'Bianca has won the election with {count} votes!')
        elif winner == 2:
            self.label_result.config(text=f'Edward has won the election with {count} votes!')
        elif winner == 3:
            self.label_result.config(text=f'Felicia has won the election with {count} votes!')
