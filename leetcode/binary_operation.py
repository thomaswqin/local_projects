import string


def main():
    pwd = input("Enter your new passwords.\n")
    print(f"your password is {pwd}")
    return

def set_0(input: int, pos: int) -> int:
    """
    SET the pos-th position of the input integer as zero
    AND 0, will always set that digit to 0.
    But need to keep other position unchanged (AND 1 or Or 0).
    Returns: int
    """
    # use "~" operator, to invert every single bit.
    result = ~(1 << pos) & input
    return result

def set_1(input: int, pos: int) -> int:
    """
    Set pos-th position of input integer as 1
    OR 1, will always set that digit to 1.
    Need to keep other positions unchanged (AND 1 or OR 0)
    """
    result = input | (1 << pos)
    return result

def set_digit(input:int, target: int, pos:int) -> int:
    if target == 0:
        return set_0(input, pos)
    elif target == 1:
        return set_1(input, pos)
    else:
        raise ValueError(f"Input target digit={target} is not 0 or 1")

if __name__ == "__main__":
    main()  # cmd + P to see parameters, fn+F1 to see documentation

