#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv


def parse_vcf(filename):
    variants = {}
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue  # sla metadata over
            parts = line.strip().split('\t')
            chrom, pos, _, ref, alt = parts[:5]
            variants[(chrom, pos)] = (ref, alt)
    return variants


def compare_vcfs(output_csv="vcf_comparison.csv"):
    
    # --- Jouw vaste paden ---
    vcf1_path = "/home/sarah/Internship_CMB_VIB/vcf_files/aln_NCBIv2_vs_newCBS.vcf"
    vcf2_path = "/home/sarah/Internship_CMB_VIB/vcf_files/aln_NCBIv2_vs_OPENPichia.vcf"

    vcf1 = parse_vcf(vcf1_path)
    vcf2 = parse_vcf(vcf2_path)

    all_positions = set(vcf1.keys()) | set(vcf2.keys())

    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["CHROM", "POS", "REF_A", "ALT_A", "REF_B", "ALT_B", "STATUS"])

        for chrom, pos in sorted(all_positions, key=lambda x: (x[0], int(x[1]))):
            a = vcf1.get((chrom, pos))
            b = vcf2.get((chrom, pos))

            if a and b:
                if a == b:
                    status = "Same_variant"
                else:
                    status = "Differ_in_variant"
                writer.writerow([chrom, pos, a[0], a[1], b[0], b[1], status])
            elif a:
                writer.writerow([chrom, pos, a[0], a[1], "-", "-", "Only in file vcf1"])
            else:
                writer.writerow([chrom, pos, "-", "-", b[0], b[1], "Only in file vcf2"])

    print(f"✅ Comparison ended. Results saved in: {output_csv}")
    print(f"   File 1: {vcf1_path}")
    print(f"   File 2: {vcf2_path}")


if __name__ == "__main__":
    compare_vcfs()

