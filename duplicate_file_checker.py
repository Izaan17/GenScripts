import argparse
import hashlib
import os.path


def hash_file(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        buf = file.read()
        hasher.update(buf)

    return hasher.hexdigest()


def process_files(files, hashes):
    # Shared logic for processing files and detecting duplicates
    for file_path in files:
        file_hash = hash_file(file_path)
        if file_hash in hashes:
            print(f'[{file_hash}]')
            print(file_path)
            print(hashes[file_hash])
            print()
        hashes[file_hash] = file_path


def gather_files(directory, is_recursive):
    if is_recursive:
        # Recursively gather files using os.walk
        for root, _, files in os.walk(directory):
            for file in files:
                yield os.path.join(root, file)  # Return each file's full path
    else:
        # Non-recursively gather files from the top-level directory
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                yield file_path  # Return each file's full path


# Type for argparse to know if it's a directory
def t_directory(string: str):
    if os.path.isdir(string):
        return string

    raise argparse.ArgumentTypeError(f"{string} is not a valid directory.")


def parse_args():
    parser = argparse.ArgumentParser(
        description='File handler'
    )
    parser.add_argument('directory', type=t_directory, default=os.getcwd(), nargs='?', const=1,
                        help='Directory to scan')
    parser.add_argument('-r', '--recursive', action='store_true',
                        help='Checks all folders in the directory recursively')

    return parser.parse_args()


def main():
    args = parse_args()
    is_recursive: bool = args.recursive
    directory: str = args.directory
    hashes: dict = {}

    files = gather_files(directory, is_recursive)

    try:
        process_files(files, hashes)
    except Exception as error:
        print(f'[error] {error}')
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
