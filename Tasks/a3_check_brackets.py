def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    if len(brackets_row) % 2 != 0:
        return False

    open = "("
    close = ")"
    if len(brackets_row) == 0:
        return True

    if brackets_row[0] == close or brackets_row[-1] == open:
        return False

    list_open_brackets = []
    list_close_brackets = []

    for simbol in brackets_row:
        if simbol == open:
            list_open_brackets.append(simbol)
        elif simbol == close:
            list_close_brackets.append(simbol)

    if len(list_open_brackets) == len(list_close_brackets):
        return True
    else:
        return False


def main():
    print(check_brackets("()()(()())"))
    print(check_brackets(")("))
    print(check_brackets(""))


if __name__ == '__main__':
    main()
