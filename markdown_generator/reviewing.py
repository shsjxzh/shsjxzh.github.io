import pandas as pd
import os
import sys

if len(sys.argv)>1:
    path = sys.argv[1]
else:
    path = "reviewing.tsv"

service = pd.read_csv(path, sep="\t", header=0).dropna(how='all')

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    if type(text) is str:
        return "".join(html_escape_table.get(c,c) for c in text)
    else:
        return "False"


loc_dict = {}

for row, item in service.iterrows():

    md_filename = str(int(item.year)) + "-" + item.url_slug + ".md"
    html_filename = str(int(item.year)) + "-" + item.url_slug
    year = item.date[:4]

    md = "---\ntitle: \""   + item.title + '"\n'
    md += "collection: reviewing" + "\n"

    #if len(str(item.type)) > 3:
        #md += 'type: "' + item.type + '"\n'
    #else:
    md += 'type: "Reviewing"\n'

    md += "permalink: /reviewing/" + html_filename + "\n"

    if len(str(item.venue)) > 3:
        md += 'venue: "' + item.venue + '"\n'

    if len(str(item.date)) > 3:
        md += 'date: ' + str(item.date) + '\n'

    if len(str(item.date_str)) > 3:
        md += 'date_str: "' + str(item.date_str) + '"\n'

    md += "---\n"


    md_filename = os.path.basename(md_filename)
    #print(md)

    with open("../_reviewing/" + md_filename, 'w') as f:
        f.write(md)
