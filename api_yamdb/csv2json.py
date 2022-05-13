import csv
import json
import os

from api_yamdb.settings import BASE_DIR

path_csv_files = os.path.join(BASE_DIR, 'static\\data\\')
path_fixtures_files = os.path.join(BASE_DIR, 'reviews\\fixtures\\')
os.mkdir(path_fixtures_files)
csv_files = os.listdir(path_csv_files)
file_model_dict = {
    "category.csv": "reviews.Category",
    "comments.csv": "reviews.Comment",
    "genre.csv": "reviews.Genre",
    "genre_title.csv": "reviews.GenreTitle",
    "review.csv": "reviews.Review",
    "titles.csv": "reviews.Title",
    "users.csv": "users.User",
}

if len(csv_files) > 0:
    for file in csv_files:
        in_file = path_csv_files + file
        out_file = path_fixtures_files + file + ".json"

        print(f"Converting {in_file} from CSV to JSON as {out_file}")

        f = open(in_file, 'r', encoding='UTF-8')
        fo = open(out_file, 'w', encoding='UTF-8')

        reader = csv.reader(f)

        header_row = []
        entries = []

        for row in reader:
            if not header_row:
                header_row = row
                continue

            pk = row[0]
            model = file_model_dict[file]
            fields = {}
            for i in range(len(row) - 1):
                active_field = row[i + 1]

                if active_field.isdigit():
                    try:
                        new_number = int(active_field)
                    except ValueError:
                        new_number = float(active_field)
                    fields[header_row[i + 1]] = new_number
                else:
                    fields[header_row[i + 1]] = active_field.strip()

            row_dict = {}
            row_dict["pk"] = int(pk)
            row_dict["model"] = file_model_dict[file]

            row_dict["fields"] = fields
            entries.append(row_dict)

        fo.write("%s" % json.dumps(entries, indent=4, ensure_ascii=False))

        f.close()
        fo.close()
