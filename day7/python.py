import argparse

parser = argparse.ArgumentParser(description='argparse 기초 예제')
parser.add_argument('name', help='사용자 이름')
parser.add_argument('--age', type=int, default=20, help='사용자 나이')
parser.add_argument('-y', '--yes', action='store_true', help='확인 플래그')
parser.add_argument('-f', '--format', default='json', choices=['json', 'xml', 'csv'], help='출력 형식 선택')

args = parser.parse_args()

print(f"Hello, {args.name}!")
print(f"Age is set to: {args.age}")

if args.yes:
    print("Confirmed!")
