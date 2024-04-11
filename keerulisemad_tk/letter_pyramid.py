"""KT tähtede püramiid -- geveev"""


def letter_triangle(letters):
    """
    Generate a triangle pattern using letters from the input string. Letters must have spaces between and
    last row can be incomplete if there are not enough letters.

    For example:
    letters("tere õhtust") ==
                    "         t \n"
                    "        e r \n"
                    "       e õ h \n"
                    "      t u s t"


    letters("tere hommikust") ==
                    "            T \n"
                    "           e r \n"
                    "          e H o \n"
                    "         m m i k \n"
                    "        u s t"

    :param letters:
    :return pyramid of letters:
    """

    letters = letters.replace(" ", "")
    triangle = ""
    n = len(letters)
    index = 0
    row_length = 1
    while index < n:
        triangle += " " * (n - row_length)
        for _ in range(row_length):
            if index < n:
                triangle += letters[index] + " "
                index += 1
        triangle += "\n"
        row_length += 1
    return triangle
