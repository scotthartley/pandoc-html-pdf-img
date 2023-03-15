"""Pandoc filter to force the <img> tag for pdf images in html.

Useful for integrating pandoc with Marked.

"""

from pandocfilters import toJSONFilter, RawInline, Str
import re


def pdf_img(key, val, fmt, meta):
    if key == 'Image' and fmt == 'html':
        attrs, caption, target = val

        new_html = "<img src=\"" + target[0] + "\" />"
        return [RawInline(fmt, new_html)]


def main():
    toJSONFilter(pdf_img)


if __name__ == '__main__':
    main()
