import time
import argparse


def timer(amount: int, name: str = ''):
    start_time = time.time()
    current_time = 0
    try:
        while current_time <= amount:
            elapsed_time = time.time() - start_time
            mins, secs = divmod(elapsed_time, 60)
            hours, mins = divmod(mins, 60)

            # Format the time in HH:MM:SS or MM:SS
            time_format = f"{int(hours):02d}:{int(mins):02d}:{int(secs):02d}" if hours else f"{int(mins):02d}:{int(secs):02d}"
            output = f"{name} - {time_format}"
            print(f"\r{output}", end='')

            time.sleep(1)
            current_time += 1
    except KeyboardInterrupt:
        pass
    print()


def t_time(string: str):
    if 's' in string:
        return float(string[:string.find('s')])
    elif 'm' in string:
        return float(string[:string.find('m')]) * 60
    elif 'h' in string:
        return float(string[:string.find('h')]) * 60 * 60
    elif 'd' in string:
        return float(string[:string.find('d')]) * 60 * 60 * 24
    elif string.isdigit():
        return float(string)
    else:
        raise argparse.ArgumentTypeError('Please enter a number or time type.')


def parse_args():
    parser = argparse.ArgumentParser(description='Simple Timer')
    parser.add_argument('time', type=t_time, default=60, const=1, nargs='?',
                        help='Amount of time to count (defaults to 10)')
    parser.add_argument('-n', '--name', type=str, default='Timer')

    return parser.parse_args()


def main():
    args = parse_args()
    timer(int(args.time), args.name)


if __name__ == '__main__':
    main()
