import csv

def csv_to_vcf(input_csv, output_vcf):

    with open(input_csv, newline='', encoding='utf-8-sig') as csvfile, \
         open(output_vcf, "w", encoding="utf-8") as out:

        reader = csv.DictReader(csvfile)
        reader.fieldnames = [f.strip() for f in reader.fieldnames]

        # Schrijf header
        out.write("##fileformat=VCFv4.2\n")
        out.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n")

        count = 0
        for row in reader:
            chrom = row["Chrom"].strip()
            pos = row["Pos"].strip()
            ref = row["REF"].strip()
            alt = row["ALT"].strip()

            out.write(f"{chrom}\t{pos}\t.\t{ref}\t{alt}\t60\t.\t.\n")
            count += 1

    print(f"VCF gemaakt: {output_vcf} met {count} varianten.")


# --- HIER definieer je jouw input en output ---
csv_to_vcf("ChangesOPENP.csv", "ChangesOPENP.vcf")