import clipboard as c


text = c.paste()
text = text.strip().split(" ")[:-3]
final = f"{' '.join(text)}"
c.copy(final)
print(final)
