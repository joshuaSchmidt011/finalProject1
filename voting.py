import pandas as pd
from main import setup


def cast_vote(id: str, vote: int) -> bool:
    """
     Cast a vote for a given ID. If the ID has already voted, the vote is not counted again.

    Parameters:
        id (str): The unique identifier of the voter.
        vote (int): The vote choice, should be 1, 2, or 3. This is provided by the tkinter ui radio buttons

    Returns:
        bool: True if the vote was successfully cast, False if the ID has already voted.
    """
    voting_df = pd.read_csv(r'votes.csv')
    values = voting_df['ID'].tolist()
    values = [str(value) for value in values]
    check = id in values
    print(values, check)

    if check:
        print('id has already voted')
        return False
    else:
        print('id has not voted')
        voting_df.loc[len(voting_df)] = [id, vote]
        voting_df.to_csv('votes.csv', index=False)
        return True


def count_votes() -> tuple[int, int]:
    """
    Counts votes and finds victor

    Returns:
        tuple[int, int]: A tuple containing the option number with the most votes and the total vote count.
    """
    voting_df = pd.read_csv(r'votes.csv')
    values = voting_df['Vote'].tolist()
    opt_1 = values.count(1)
    opt_2 = values.count(2)
    opt_3 = values.count(3)
    vote_list = [opt_1, opt_2, opt_3]
    most_votes = vote_list.index(max(vote_list))
    most_votes += 1
    setup()
    return most_votes, max(vote_list)

