import json
import os
import random

all_torrents_list = []

main_folder = os.path.join(os.getcwd(), "GifGang")
for file in os.listdir(main_folder):
    file_exact_path = os.path.join(main_folder, file)
    if os.path.isfile(file_exact_path):
        if file.lower().endswith("json"):
            print(file)
            with open(file_exact_path, "r", encoding="utf-8") as _file:
                data = json.load(_file)
                for element in data:
                    all_torrents_list.append(element)
            print(len(all_torrents_list))

with open("output.json", "w", encoding="utf-8") as _file:
    json.dump(all_torrents_list, _file, ensure_ascii=True, indent=4)

shuffled = random.shuffle(all_torrents_list)

with open("shuffled.json", "w", encoding="utf-8") as _file:
    json.dump(all_torrents_list, _file, ensure_ascii=True, indent=4)
