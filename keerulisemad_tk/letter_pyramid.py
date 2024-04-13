"""KT tähtede püramiid -- geveev"""


def letter_pyramid(letters):
    """
    Generate a triangle pattern using letters from the input string. Letters must have spaces between and
    last row can be incomplete if there are not enough letters.

    For example:
    letters("tere õhtust") ==
    "   t\n"
    "  e r\n"
    " e õ h\n"
    "t u s t"


    letters("tere hommikust") ==
    "    t\n"
    "   e r\n"
    "  e h o\n"
    " m m i k\n"
    "u s t"

    letters("12512") ==
    "  1\n"
    " 2 5\n"
    "1 2"

    :param letters:
    :return pyramid of letters:
    """

    letters = letters.replace(" ", "")
    triangle = ""
    n = len(letters)
    index = 0
    row_length = 1
    rows = []

    # Kõik read
    while index < n:
        end_index = min(index + row_length, n)
        rows.append(letters[index:end_index])
        index += row_length
        row_length += 1

    total_rows = len(rows)

    # Püramiidi ehitaja
    for i, row in enumerate(rows):
        leading_spaces = total_rows - 1 - i
        line = " " * leading_spaces + " ".join(row)
        triangle += line + "\n"

    return triangle.rstrip()
