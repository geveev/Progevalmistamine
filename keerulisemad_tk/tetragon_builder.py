"""KT seest tühi nelinurk -- GeVeev"""


def tetragon_builder(height: int, length: int):
    """ write a function that generates a tetragon with an empty
    interior using asterisks (*) and spaces ( ).The tetragon will have a specified
    height and length, and it should haveasterisks on the first and last rows, as well
    as the first and last columns,with empty space inside. height and length is always positive integers.
    :param height:
    :param length:
    :return tetragon:
    """

    result = ''
    for i in range(height):
        if i == 0 or i == height - 1:
            result += '*' * length + '\n'
        else:
            result += '*' + ' ' * (length - 2) + '*' + '\n'

    return result[0:-1]
