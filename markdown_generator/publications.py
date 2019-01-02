import pandas as pd
import sys

if len(sys.argv)>1:
    path = sys.argv[1]
else:
    path = "publications.tsv"

publications = pd.read_csv(path, sep="\t", header=0)

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)

import os
for row, item in publications.iterrows():

    md_filename = str(item.pub_date) + "-" + item.url_slug + ".md"
    html_filename = str(item.pub_date) + "-" + item.url_slug
    year = item.pub_date[:4]

    ## YAML variables

    md = "---\ntitle: \""   + item.title + '"\n'

    md += """collection: publications"""

    md += """\npermalink: /publication/""" + html_filename

    if len(str(item.excerpt)) > 5:
        md += "\nexcerpt: '" + html_escape(item.excerpt) + "'"

    md += "\ndate: " + str(item.pub_date)

    md += "\nvenue: '" + html_escape(item.venue) + "'"

    md+= "\nlead: " + str(item.lead)

    if len(str(item.paper_url)) > 5:
        md += "\npaperurl: '" + item.paper_url + "'"

    md += "\n---"

    ## Markdown description for individual page

    if len(str(item.paper_url)) > 5:
        md += "\n\n<a href='" + item.paper_url + "'>Download paper here</a>\n"

    if len(str(item.excerpt)) > 5:
        md += "\n" + html_escape(item.excerpt) + "\n"

    md_filename = os.path.basename(md_filename)

    with open("../_publications/" + md_filename, 'w') as f:
        f.write(md)
