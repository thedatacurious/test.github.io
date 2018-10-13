import sys
from datetime import datetime

TEMPLATE = """
title: {title}
date: {year}-{month}-{day} {hour}:{minute:02d}
tags:
category:
slug: {slug}
summary:
status: draft
"""


def create_post(title):
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '-')
    file_name = "content/{}_{:0>2}_{:0>2}_{}.md".format(
        today.year, today.month, today.day, slug)
    t = TEMPLATE.strip().format(title=title,
                                year=today.year,
                                month=today.month,
                                day=today.day,
                                hour=today.hour,
                                minute=today.minute,
                                slug=slug)
    with open(file_name, 'w') as w:
        w.write(t)
    print("File created -> " + file_name)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        create_post(sys.argv[1])
    else:
        print "No title given"
