import argparse

def get_args():
    parser = argparse.ArgumentParser(
        description='빈도수 계산',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('dna', metavar='DNA', help='Input DNA Sequence')

    return parser.parse_args()

def main():
    args = get_args()
    print(args.dna)

if __name__ == '__main__':
    main()