from collections import Counter
import random
import timeit

def iter_count(dna):
    cnt_a, cnt_c, cnt_g, cnt_t = 0, 0, 0, 0

    for base in dna:
        if base == "A":
            cnt_a += 1
        elif base == "C":
            cnt_c += 1
        elif base == "G":
            cnt_g += 1
        elif base == "T":
            cnt_t += 1
    return (cnt_a, cnt_c, cnt_g, cnt_t)

def dict_count(dna):
    counts = {}
    for base in dna:
        counts[base] = counts.setdefault(base, 0)
        counts[base] += 1
    return counts

def counter_count(dna):
    return dict(Counter(dna))

def string_count(dna):
    a = dna.count("A")
    c = dna.count("C")
    g = dna.count("G")
    t = dna.count("T")

    return (a, c, g, t)

def generate_dna(length):
    bases = ["A", "C", "G", "T"]

    return "".join(random.choice(bases) for _ in range(length))

def main():
    dna_sequence = generate_dna(length=100000000)

    #timeit 설정
    number_of_runs = 10
    repeat_count = 3

    print(f"순차 실행 반복 테스트 조건 : 함수당 {number_of_runs}, 최소값 {repeat_count} 측정")

    method_list = {
        "1. iter_count": iter_count,
        "2. Dictionary": dict_count,
        "3. str.count()": string_count,
        "4. collections.Counter": counter_count
    }

    results = {}

    for name, func in method_list.items():
        timing_globals = {"func":func, "dna_sequence":dna_sequence}

        # 측정 시작
        timer = timeit.repeat(
            stmt = "func(dna_sequence)",
            globals = timing_globals,
            repeat = repeat_count,
            number = number_of_runs
        )

        time_best = min(timer)
        results[name] = time_best

        print(f"측정 완료: {name:<30} -> {time_best:.6f}초")
    
    print("최종 성능 순위(총 누적시간 기준)")
    sorted_results = sorted(results.items(), key=lambda item: item[1])

    for rank, (name, total_time) in enumerate(sorted_results, 1):
        ratio = total_time / sorted_results[0][1]
        print(f"{rank}.{name:<35} : {total_time:.6f} 초({ratio:.2f}배 느림)")

if __name__ == "__main__":
    main()