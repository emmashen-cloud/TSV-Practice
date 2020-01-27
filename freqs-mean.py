import csv

with open("freqs.tsv") as infile:
    reader = csv.reader(infile, delimiter="\t")
    with open("freqs-means.tsv", "w") as outfile:
        writer = csv.writer(outfile, delimiter="\t")
        for l in reader:
            # Calculate the mean for each line by dividing the sum 
            # by the length; if a column is a "", its value is a 0
            line_sum = sum((float(x) if x else 0) for x in l[1:])
            mean = line_sum / len(l[1:]) if line_sum else 0
            l.append(mean)
            writer.writerow(l)
