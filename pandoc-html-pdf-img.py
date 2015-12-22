#! /usr/bin/env python3
"""Pandoc filter to force the <img> tag for pdf images in html.

Useful for integrating pandoc with Marked.

"""

from pandocfilters import toJSONFilter, RawInline, Str
import re

def pdf_img(key, val, fmt, meta):
    if key == 'Image' and fmt == 'html':
        caption, target = val

        precap = "<figure><img src=\"" + target[0] + "\" /><figcaption>"
        postcap = "</figcaption></figure>"

        return [RawInline(fmt, precap)] + caption + [RawInline(fmt, postcap)]

if __name__ == '__main__':
    toJSONFilter(pdf_img)
