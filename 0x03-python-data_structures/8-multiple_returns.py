#!/usr/bin/python3


def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string and its first character.

    Args:
    - sentence: Input string.

    Returns:
    - A tuple (length, first_char).
    """
    length = len(sentence)
    first_char = sentence[0] if length > 0 else None
    return length, first_char


if __name__ == "__main__":
    sentence = "At school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))
