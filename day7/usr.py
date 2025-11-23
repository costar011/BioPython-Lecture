import argparse

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        print("0으로 나눌 수 없습니다.")
        return
    else:
        return a / b

#############

def get_args():
    # 파서 생성
    parser = argparse.ArgumentParser(description="계산기")
    # 필수 인자
    parser.add_argument('a', type=float, help='첫 번째 인수')
    parser.add_argument('b', type=float, help='두 번째 인수')
    # 선택 인자
    parser.add_argument('-o', '--operation',
                        dest='op',
                        choices=['add', 'sub', 'mul', 'div'],
                        default='add',
                        help='연산 선택 (add, sub, mul, div)')
    parser.add_argument('-v', '--verbose', action='store_true', help='결과 상세히 출력')
    
    args = parser.parse_args()
    
    return args

def main():
    args = get_args()
    if args.op == 'add':
        result = add(args.a, args.b)
    elif args.op == 'sub':
        result = sub(args.a, args.b)
    elif args.op == 'mul':
        result = mul(args.a, args.b)
    elif args.op == 'div':
        result = div(args.a, args.b)
    
    if args.verbose:
        print(f"계산: {args.a} {args.op} {args.b} = {result}")
    else:
        print(result)

if __name__ == '__main__':
    main()
