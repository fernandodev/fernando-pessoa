import regex
import json
import sys

# extract_text.py <input> <output.json>
# output:
# [
#   {
#     title: String
#     text: [String]
#   }
# ]
#

def extract_texts(filename):
  file = open(filename, "r")
  title_regex = regex.compile(r"(\p{Lu}+\ ?)+")

  json = []
  entry = {}
  keep_running = True
  line = file.readline()
  while keep_running :
    match = title_regex.search(line)
    content = line.replace("\n", "")

    if(match != None and match.group(0) == content):
      title = entry.get('title')

      if(title != None):
        json.append(entry)
        entry = {}

      entry['title'] = content
    else:
      text = entry.get('text')

      if(text == None):
        text = []

      text.append(content)
      entry['text'] = text

    line = file.readline()
    if(line == ''):
      json.append(entry)
      keep_running = False

  return json

def export(json_hash, filename):
  exportable = json.dumps(json_hash)
  file = open(filename, "w")
  file.write(exportable)
  file.close()


result = extract_texts(str(sys.argv[1]))
export(result, str(sys.argv[2]))