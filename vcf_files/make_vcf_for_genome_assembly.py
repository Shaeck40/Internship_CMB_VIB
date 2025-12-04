import csv

def create_vcf(input_csv, original_vcf, output_vcf):
    """
    Maak een nieuw VCF op basis van:
    - input_csv: CSV met kolommen Chrom, Pos
    - original_vcf: VCF met QNAME en QSTART in INFO
    - output_vcf: nieuw VCF-bestand
    """

    # Laad originele VCF entries op basis van CHROM/POS
    vcf_data = {}
    with open(original_vcf, encoding='utf-8') as v:
        for line in v:
            if line.startswith('#'):
                continue
            parts = line.strip().split('\t')
            if len(parts) < 8:
                continue
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

    # Lees CSV en schrijf nieuwe VCF
    with open(input_csv, newline='', encoding='utf-8-sig') as csvfile, open(output_vcf, 'w', encoding='utf-8') as out:
        reader = csv.DictReader(csvfile, delimiter=',')
        reader.fieldnames = [name.strip() for name in reader.fieldnames]

        # VCF-header
        out.write("##fileformat=VCFv4.2\n")
        out.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n")

        count = 0
        for row in reader:
            chrom = str(row.get('Chrom')).strip()
            pos = str(row.get('Pos')).strip()

            key = (chrom, pos)
            if key not in vcf_data:
                continue

            entry = vcf_data[key]
            new_chrom = entry['qname']
            new_pos = entry['qstart']
            new_ref = entry['alt']
            new_alt = entry['ref']

            out.write(f"{new_chrom}\t{new_pos}\t.\t{new_ref}\t{new_alt}\t60\t.\t.\n")
            count += 1

    print(f"Nieuwe VCF gemaakt: {output_vcf} met {count} varianten.")


if __name__ == "__main__":
    create_vcf("ChangesCBS.csv", "aln_NCBIv2_vs_newCBS.vcf", "ChangesCBS.vcf")
