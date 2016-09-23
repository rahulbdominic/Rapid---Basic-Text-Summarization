import io, json

def export(text, filename):
    lst = []
    lt = []
    j = {"title": filename, "content_short": text}
    lst.append(j)
    with io.open(filename + '.json', 'w') as f:
        f.write(json.dumps(lst, ensure_ascii=False))
