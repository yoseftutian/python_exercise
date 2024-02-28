def validate_party_char(char):
    valid_chars = {'A', 'B', 'L', 'Y'}
    if char not in valid_chars:
        raise ValueError("Invalid party_char. must be 'A', 'B', 'L', or 'Y'")
    return char


class Petek:
    def __init__(self, party_char, party_name):
        self._party_char = validate_party_char(party_char)
        self._party_name = party_name

    # getter and setter for party_char
    @property
    def party_char(self):
        return self._party_char

    @party_char.setter
    def party_char(self, value):
        self._party_char = validate_party_char(value)

    # getter and setter for party_name
    @property
    def party_name(self):
        return self._party_name

    @party_name.setter
    def party_name(self, value):
        self._party_name = value


# a class for the ballot box ("Kalpi box")
class BallotBox:
    # G1
    def __init__(self, ballot_number):
        self.ballot_number = ballot_number
        self.peteks = [None] * 100  # init. 100 cells
        self.petek_count = 0

    def get_ballot_number(self):
        return self.ballot_number

    def set_ballot_number(self, ballot_number):
        self.ballot_number = ballot_number

    # G3 -> adding a "Petek"
    def add_petek(self, petek):
        if self.petek_count < len(self.peteks):  # max. 100 places(!)
            self.peteks[self.petek_count] = petek
            self.petek_count += 1
        else:
            print("Ballot box is full.")

    # new party_char list
    # higher scope because we need it outside the method
    party_char_counts = [0, 0, 0, 0]  # the party list with counts for each party

    # counting the "party chars"
    def count_party_chars(self):
        # count for 'A', 'B', 'L', 'Y'
        for i in range(len(self.peteks)):
            petek = self.peteks[i]
            if petek is not None:  # otherwise, the program might crash
                party_char = petek.party_char
                # Use match-case instead
                if party_char == 'A':
                    self.party_char_counts[0] += 1
                elif party_char == 'B':
                    self.party_char_counts[1] += 1
                elif party_char == 'L':
                    self.party_char_counts[2] += 1
                elif party_char == 'Y':
                    self.party_char_counts[3] += 1

    # this one is meant for printing the char_counts list
    def get_party_char_counts(self):
        return self.party_char_counts


# for the BallotBox (get a ballot variable, and count the parties in it)
def count_party_chars_in_ballot_box(ballot_box):
    ballot_box.count_party_chars()


# Testing this
class Main:
    box = BallotBox(123)
    box.add_petek(Petek('A', "Party A"))
    box.add_petek(Petek('B', "Party B"))
    box.add_petek(Petek('A', "Party A"))
    count_party_chars_in_ballot_box(box)

    party_char_counts = box.get_party_char_counts()
    print(f"Party char counts: A={party_char_counts[0]}, B={party_char_counts[1]},"
          f" L={party_char_counts[2]}, Y={party_char_counts[3]}")
