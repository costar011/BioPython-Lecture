#!/usr/bin/env python3

# @title Horai (1995) 인류 기원 분석
import matplotlib.pyplot as plt
import pandas as pd
from Bio import Entrez, SeqIO, AlignIO, Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
import os
import subprocess

# 1. 설정
Entrez.email = "your_email@example.com"  # 본인 이메일 입력으로 변경

human_origin_dict = {
    "African (Ugandan)": "D38112",    # 논문의 핵심 뿌리
    "Japanese (Asian)": "D38116",     # 아시아 대표
    "European (Standard)": "NC_012920", # 수정된 표준
    "Chimpanzee (Outgroup)": "D38113" # 외집단
}

filenames = {"fasta": "human_origin.fasta", "aln": "human_origin.aln"}

def run_human_origin_analysis_fixed():
    print("--- [인류 기원(Out of Africa) 분석 시작] ---")
    
    # 2. 다운로드
    print(f"1. NCBI 데이터 다운로드 중...")
    sequences = []
    try:
        for name, acc_id in human_origin_dict.items():
            with Entrez.efetch(db="nucleotide", id=acc_id, rettype="fasta", retmode="text") as handle:
                record = SeqIO.read(handle, "fasta")
                record.id = name
                record.description = acc_id
                sequences.append(record)
        SeqIO.write(sequences, filenames["fasta"], "fasta")
    except Exception as e:
        print(f"[Error] 다운로드 실패: {e}")
        return

    # 3. 정렬
    # ClustalW는 시스템에 설치되어 있어야 합니다

    print("2. ClustalW 정렬 수행 중...")
    cmd = ["clustalw", "-INFILE=" + filenames["fasta"], "-OUTFILE=" + filenames["aln"], "-OUTPUT=CLUSTAL"]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"[Error] 정렬 실패: {e}")
        return

    # 4. 분석 및 시각화 (수정된 부분)
    print("3. 계통수 및 유전적 거리 계산...")
    try:
        alignment = AlignIO.read(filenames["aln"], "clustal")
    except:
        print("정렬 파일을 읽을 수 없습니다.")
        return

    calculator = DistanceCalculator('identity')
    dm = calculator.get_distance(alignment)
    
    constructor = DistanceTreeConstructor()
    tree = constructor.nj(dm)

    # 1. 먼저 침팬지 노드를 찾습니다.
    outgroup_node = None
    for clade in tree.find_clades():
        if "Chimpanzee" in clade.name:
            outgroup_node = clade
            break
            
    # 2. 찾은 노드로 뿌리를 설정합니다.
    if outgroup_node:
        tree.root_with_outgroup(outgroup_node)
        print("   -> Root 설정 완료: Chimpanzee")
    else:
        print("   -> [Warning] 외집단(Chimpanzee)을 찾을 수 없습니다.")

    # 그래프 그리기
    fig, ax = plt.subplots(figsize=(12, 8))
    Phylo.draw(tree, axes=ax, do_show=False, branch_labels=lambda c: round(c.branch_length, 4) if c.branch_length else None)
    
    ax.set_title("Phylogenetic Tree of Human Origins (Horai et al., 1995)", fontsize=16, fontweight='bold')
    ax.set_xlabel("Evolutionary Distance")
    
    plt.tight_layout()
    plt.show()

    # 유전적 거리 행렬 출력
    print("\n[유전적 거리 행렬 (Identity %)]")
    names = [s.id for s in alignment]
    matrix_data = [[(1 - dm[i, j]) * 100 for j in range(len(names))] for i in range(len(names))]
    
    df = pd.DataFrame(matrix_data, index=names, columns=names)
    pd.options.display.float_format = '{:.2f}%'.format
    print(df)
    
    print("\n[ASCII Tree Structure]")
    Phylo.draw_ascii(tree)

if __name__ == "__main__":
    run_human_origin_analysis_fixed()