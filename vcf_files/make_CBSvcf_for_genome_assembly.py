import csv

def excel_to_vcf(input_csv, original_vcf, output_vcf):
    """
    Convert CSV plus original VCF into remapped VCF.
    """

    # Laad originele VCF entries op basis van CHROM/POS
    vcf_data = {}
    with open(original_vcf) as v:
        for line in v:
            if line.startswith('#'):
                continue
            parts = line.strip().split('\t')
            chrom, pos, _, ref, alt, _, _, info = parts[:8]

            # Parse INFO naar dictionary
            info_dict = dict(p.split('=') for p in info.split(';') if '=' in p)

            qname = info_dict.get('QNAME')
            qstart = info_dict.get('QSTART')

            vcf_data[(chrom, pos)] = {
                'ref': ref,
                'alt': alt,
                'qname': qname,
                'qstart': qstart
            }

    # Schrijf nieuwe VCF
    with open(input_csv, newline="") as csvfile, open(output_vcf, "w") as out:
        reader = csv.DictReader(csvfile, delimiter=',')

        out.write("##fileformat=VCFv4.2\n")
        out.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n")

        for row in reader:
            chrom = str(row.get('Chrom'))
            pos = str(row.get('Pos'))

            key = (chrom, pos)
            if key not in vcf_data:
                continue

            entry = vcf_data[key]

            new_chrom = entry['qname']
            new_pos = entry['qstart']
            new_ref = entry['alt']
            new_alt = entry['ref']

            out.write(f"{new_chrom}\t{new_pos}\t.\t{new_ref}\t{new_alt}\t60\t.\t.\n")


if __name__ == "__main__":
    excel_to_vcf("ChangesCBS.csv", "output.vcf", "ChangesCBS.vcf")