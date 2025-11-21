parser.add_argument("name", help='사용자 이름')
parser.add_argument('--age', type=int, default=20, help='사용자 이름')
parser.add_argument('-y', '--yes', action='store_true', help='확인 플래그')

args = parser.parse_args()

print(f"Hello, {args.name}")
print(f"Age is set to: {args.age}")

if args.yes:
    print("Confirmed")