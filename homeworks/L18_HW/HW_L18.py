# Task 1
import argparse


def main():
    parser = argparse.ArgumentParser('sum of 2 numbers')
    parser.add_argument('number_1', type=int, help="number1")
    parser.add_argument('number_2', type=int, help="number2")

    args = parser.parse_args()
    answer = args.number_1 + args.number_2
    print(f'{args.number_1} + {args.number_2} = {answer}')


if __name__ == "__main__":
    main()
else:
    pass


#  Task 2 Написати скрипт який прмймає назву файлу і рахує скільки слів знаходиться в ньому.

def number_words():
    parser = argparse.ArgumentParser('Number of words in your file')
    parser.add_argument(dest='filename', action='store', type=str)
    args = parser.parse_args()
    print(len(args.filename.read()))


if __name__ == '__main__':
    number_words()
