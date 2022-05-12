import os
import json

torrents_json_file_name = os.path.join(os.getcwd(), "GifGang", "torrents.json")

with open(torrents_json_file_name, "r", encoding="utf-8") as _file:
    data = json.load(_file)
