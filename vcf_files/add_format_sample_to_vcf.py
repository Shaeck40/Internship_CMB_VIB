import sys

# Check if the user provided input and output filenames
if len(sys.argv) != 3:
    print(f"Usage: python {sys.argv[0]} <input_vcf> <output_vcf>")
    sys.exit(1)

input_vcf = sys.argv[1]
output_vcf = sys.argv[2]

with open(input_vcf, "r") as fin, open(output_vcf, "w") as fout:
    for line in fin:
        if line.startswith("##"):
            fout.write(line)
            continue

        if line.startswith("#CHROM"):
            # Add FORMAT meta
            fout.write('##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">\n')
            # Add FORMAT and sample columns
            header = line.strip().split("\t")
            header += ["FORMAT", "CBS"]
            fout.write("\t".join(header) + "\n")
            continue

        # Add FORMAT and sample values to data lines
        fields = line.strip().split("\t")
        fields += ["GT", "1/1"]
        fout.write("\t".join(fields) + "\n")

print(f"Processed {input_vcf} -> {output_vcf}")
