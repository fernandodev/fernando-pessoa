"""
    expected arguments input:
        filename.txt
        outputfilename.json
"""
import json
import sys
import regex

def extract_texts(filename):
    """
    extract_text.py <input> <output.json>
    output:
    [
      {
        title: String
        text: [String]
      }
    ]
    """
    file = open(filename, "r")
    title_regex = regex.compile(r"(\p{Lu}+\ ?)+")

    entries = []
    entry = {}
    keep_running = True
    line = file.readline()
    while keep_running:
        match = title_regex.search(line)
        content = line.replace("\n", "")

        if(match is not None and match.group(0) == content):
            title = entry.get('title')

            if title is not None:
                entries.append(entry)
                entry = {}

            entry['title'] = content
        else:
            text = entry.get('text', [])
            text.append(content)
            entry['text'] = text

        line = file.readline()
        if line == '':
            entries.append(entry)
            keep_running = False

    return entries


def export(json_hash, filename):
    """ just exports the generated has to a json file """
    exportable = json.dumps(json_hash)
    file = open(filename, "w")
    file.write(exportable)
    file.close()


RESULT = extract_texts(str(sys.argv[1]))
export(RESULT, str(sys.argv[2]))
