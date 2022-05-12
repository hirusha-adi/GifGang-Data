from flask import Flask, redirect, render_template, request, url_for
import os
import json

torrents_json_file_name = os.path.join(os.getcwd(), "GifGang", "torrents.json")

app = Flask(__name__)


@app.route("/torrents_add_post", methods=['POST'])
def torrents_add_post():
    with open(torrents_json_file_name, "r", encoding="utf-8") as _file:
        data = json.load(_file)

    TorrentQuality = request.form.get('TorrentQuality')

    temp_data = {
        'title': str(request.form.get('TorrentTitle')).strip(),
        'size': str(request.form.get('TorrentSize')).strip(),
        'link': str(request.form.get('TorrentLink')).strip(),
        'quality': '1080p' if TorrentQuality == "1" else '480p',
        'se': int(request.form.get('TorrentSeeds').strip()),
        'channel': str(request.form.get('TorrentChannel')).strip(),
        'page': str(request.form.get('TorrentPage')).strip()
    }

    print("Recieved Data --->")
    print("\n\t", temp_data, "\n")

    if not(temp_data in data):
        data.append(temp_data)
        print("Added data to list")
    else:
        print("Dictionary already exists in list.\nSkipping...")

    with open(torrents_json_file_name, "w", encoding="utf-8") as _file:
        json.dump(data, _file, indent=4, ensure_ascii=True)

    print("Saved data to GifGang/torrents.json")
    print(f'Total Torrents Available: {len(data)}\n\n')

    return redirect(url_for('torrents'))


@app.route("/")
def torrents():
    return render_template(
        "settings.html",
        show_torrents_form=True
    )


app.run("0.0.0.0", port=8090, debug=True)
