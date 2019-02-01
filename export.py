import sys
import quip
from bs4 import BeautifulSoup


def export(id):
    thread = quip.get_thread(id)
    messages = quip.get_recent_messages(id)

    doc = BeautifulSoup(thread['html'], 'html.parser')
    doc_end = doc.contents[-1]

    for m in messages:
        if m['annotation']:
            ids = []
            if 'highlight_section_ids' in m['annotation']:
                ids.extend(m['annotation']['highlight_section_ids'])
            if 'id' in m['annotation']:
                ids.append(m['annotation']['id'])

            anchor = next(
                filter(None, map(lambda id: doc.find(id=id), ids)), doc_end)
        else:
            anchor = doc_end

        blockquote = doc.new_tag('blockquote')
        cite = doc.new_tag('cite')
        author_name = doc.new_tag('em')
        author_name.append(m['author_name'])
        cite.append('– ')
        cite.append(author_name)
        p = doc.new_tag('p')
        is_first = True
        for line in m['text'].splitlines():
            if is_first:
                is_first = False
            else:
                p.append(doc.new_tag('br'))
            p.append(line)
        blockquote.append(p)
        blockquote.append(cite)
        anchor.insert_after(blockquote)

    filename = thread['thread']['title'] + '.html'
    with open(filename, 'w') as fp:
        print(doc.prettify(), file=fp)
        print('export to ' + filename)


if __name__ == "__main__":
    export(sys.argv[1])
