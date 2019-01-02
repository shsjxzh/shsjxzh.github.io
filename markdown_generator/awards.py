import pandas as pd
import os
import sys

if len(sys.argv)>1:
    path = sys.argv[1]
else:
    path = "awards.tsv"

awards = pd.read_csv(path, sep="\t", header=0)

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

for row, item in awards.iterrows():

    md_filename = str(item.year) + "-" + item.url_slug + ".md"
    html_filename = str(item.year) + "-" + item.url_slug
    year = item.date[:4]

    md = "---\ntitle: \""   + item.title + '"\n'
    md += "collection: awards" + "\n"

    #if len(str(item.type)) > 3:
        #md += 'type: "' + item.type + '"\n'
    #else:
    md += 'type: "Award"\n'

    md += "permalink: /awards/" + html_filename + "\n"

    if len(str(item.granter)) > 3:
        md += 'granter: "' + item.granter + '"\n'

    if len(str(item.date)) > 3:
        md += "date: " + str(item.date) + "\n"

    md += "---\n"

    if len(str(item.description)) > 3:
        md += "\n" + html_escape(item.description)+"\n"


    md_filename = os.path.basename(md_filename)
    #print(md)

    with open("../_awards/" + md_filename, 'w') as f:
        f.write(md)
