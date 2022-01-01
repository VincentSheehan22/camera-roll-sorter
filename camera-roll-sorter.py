from datetime import  datetime
import os
import shutil

"""Python script to move images from a single source directory to destination directories,
based on year (date modified).

To Do:
* Filter by file type (.jpeg vs .mov/.mp4).
* Allow for flexible sorting options.
    * Quantity of destination directories.
    * User specified sort criteria.
        * Year, month, day, subject, etc.
* Option to copy rather than move.
"""

src = input(r"Enter path of source directory: ")

dst_2021 = input(r"Enter path of destination directory for year 2021: ")
dst_2020 = input(r"Enter path of destination directory for year 2020: ")
dst_2019 = input(r"Enter path of destination directory for year 2019: ")
dst_2018 = input(r"Enter path of destination directory for year 2018: ")
dst_2017 = input(r"Enter path of destination directory for year 2017: ")

for file in os.listdir(src):
    src_file = os.path.join(src, file)

    date_modified = os.path.getmtime(src_file)
    date_modified = datetime.fromtimestamp(date_modified).strftime('%Y-%m-%d %H:%M:%S')

    if '2021' in date_modified:
        dst_file = os.path.join(dst_2021, file)
        shutil.move(src_file, dst_file)

        print(f"{file} moved.")

    if '2020' in date_modified:
        dst_file = os.path.join(dst_2020, file)
        shutil.move(src_file, dst_file)

        print(f"{file} moved.")

    elif '2019' in date_modified:
        dst_file = os.path.join(dst_2019, file)
        shutil.move(src_file, dst_file)

        print(f"{file} moved.")

    elif '2018' in date_modified:
        dst_file = os.path.join(dst_2018, file)
        shutil.move(src_file, dst_file)

        print(f"{file} moved.")

    elif '2017' in date_modified:
        dst_file = os.path.join(dst_2017, file)
        shutil.move(src_file, dst_file)

        print(f"{file} moved.")
    else:
        print(f"Year not in range. {file} not moved.")