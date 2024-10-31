import argparse
import string

CHARS = string.ascii_letters + string.digits


def is_word(text: str):
    for char in text:
        if char in CHARS:
            return True
    return False


def get_word_count_and_characters(text: str) -> [int, int]:
    char_count = len(text.replace('\n', ''))
    text = " ".join(text.split())
    text = text.split()
    word_count = 0
    for word in text:
        # Character count
        if is_word(word):
            word_count += 1

    return word_count, char_count


def parse_args():
    parser = argparse.ArgumentParser(
        description='gather file name to count words'
    )
    parser.add_argument('file', metavar='str', type=argparse.FileType('r'), help='Filename to count words')

    return parser.parse_args()


def main():
    args = parse_args()
    if args.file:
        file = args.file
        with file as file_handler:
            word_count, char_count = get_word_count_and_characters(file_handler.read())
            print(f'File: {file.name}\n'
                  f'Words: {word_count}\n'
                  f'Character Count: {char_count}\n')


if __name__ == '__main__':
    main()
