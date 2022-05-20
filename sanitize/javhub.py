import clipboard as c


text = c.paste()
text = text.strip()
title = text.split(".")[0]
date = text.split(".")[1:4]
mid_text = text.split(".")[4:-4]
final = f"{title} - {' '.join(mid_text)} - {'.'.join(date)}"
c.copy(final)
print(final)
