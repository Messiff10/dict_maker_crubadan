import os
import csv

language = "en_US"
kaggle_dir = "/Users/grace/data/kaggle"
kaggle_file_name = os.path.join(kaggle_dir, "twcs.csv")
output_dir = "/Users/grace/data/word/csv_from_spark/1/"
output_file_name = output_dir + language + "_twitter_kaggle_.txt"

res = []
with open(kaggle_file_name, 'r', encoding='utf-8') as kaggle_file:
    reader = csv.DictReader(kaggle_file)
    res = [row['text']+"\n" for row in reader]


with open(output_file_name, 'w', encoding='utf-8') as output_file:
    print("writing", output_file_name, "...")
    output_file.writelines(res)

print("len of", output_file_name, "is", str(len(res)))
print("Finished!")
