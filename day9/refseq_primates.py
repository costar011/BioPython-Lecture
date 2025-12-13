#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
from Bio import Entrez, SeqIO, AlignIO, Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
import os
import subprocess

# 1. 설정
Entrez.email = "your_email@example.com"  
filename_fasta = "refseq_primates.fasta"
filename_aln = "refseq_primates.aln"

# 최신 표준 RefSeq ID
refseq_species = {
    "Human": "NC_012920",
    "Chimpanzee": "NC_001643",
    "Bonobo": "NC_001644",
    "Gorilla": "NC_001645",
    "Rhesus_Macaque": "NC_005943"
}

def run_refseq_analysis():
    print("--- [RefSeq 분석 시작] ---")

    # 2. 다운로드
    sequences = []
    print(f"1. NCBI 다운로드 중 ({len(refseq_species)}종)...")
    try:
        for name, acc_id in refseq_species.items():
            with Entrez.efetch(db="nucleotide", id=acc_id, rettype="fasta", retmode="text") as handle:
                record = SeqIO.read(handle, "fasta")
                record.id = name
                record.description = f"{name}|{acc_id}"
                sequences.append(record)
        SeqIO.write(sequences, filename_fasta, "fasta")
    except Exception as e:
        print(f"다운로드 오류: {e}")
        return

    # 3. 정렬 (ClustalW)
    print("2. 서열 정렬(Alignment) 수행 중...")
    cmd = ["clustalw", "-INFILE=" + filename_fasta, "-OUTFILE=" + filename_aln, "-OUTPUT=CLUSTAL"]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"정렬 오류: {e}")
        return

    # 4. 분석 및 시각화
    print("3. 계통수 및 거리 행렬 계산...")
    try:
        alignment = AlignIO.read(filename_aln, "clustal")
    except:
        print("정렬 파일을 읽을 수 없습니다.")
        return

    calculator = DistanceCalculator('identity')
    dm = calculator.get_distance(alignment)
    constructor = DistanceTreeConstructor()
    tree = constructor.nj(dm)

    # Root 설정
    for clade in tree.get_terminals():
        if clade.name == "Rhesus_Macaque":
            tree.root_with_outgroup(clade)
            break

    # 그래프 그리기
    fig, ax = plt.subplots(figsize=(12, 6))
    Phylo.draw(tree, axes=ax, do_show=False, branch_labels=lambda c: round(c.branch_length, 4) if c.branch_length else None)
    ax.set_title("Phylogenetic Tree (RefSeq Standard)", fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.show()

    # 유전적 유사도 행렬 출력
    print("\n[RefSeq 유전적 유사도 (Identity %)]")
    names = [s.id for s in alignment]
    matrix_data = [[(1 - dm[i, j]) * 100 for j in range(len(names))] for i in range(len(names))]
    df = pd.DataFrame(matrix_data, index=names, columns=names)
    pd.options.display.float_format = '{:.2f}%'.format
    print(df)  

if __name__ == '__main__':
    run_refseq_analysis()