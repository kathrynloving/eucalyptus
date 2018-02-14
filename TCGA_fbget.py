import fbget, csv
clinical_data = fbget.clinical("TGCT").split("\n")
csv_writer = csv.writer(open("TCGA_TGCT_clinical_data.csv", 'w'))
for row in clinical_data:
    row_to_list = row.split("\t")
    csv_writer.writerow(row_to_list)

