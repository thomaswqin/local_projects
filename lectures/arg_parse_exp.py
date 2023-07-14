import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--first", type=str,
                        default="sample first str",
                        help="The first argument to the function")
    parser.add_argument("-s", "--second", type=int,
                        default=999,
                        help="The first argument to the function")
    parser.add_argument("-t", "--third",
                        action="store_true",
                        help="The first argument to the function")
    args = parser.parse_args()
    first_arg = args.first
    second_arg = args.second
    third_arg = args.third  # if not passed in, will be false by default

    print(f"Value {first_arg}, type is {type(first_arg)}")
    print(f"Value {second_arg}, type is {type(second_arg)}")
    print(f"Value {third_arg}, type is {type(third_arg)}")


if __name__ == "__main__":
    main()
