#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
The Curious Case Encoding
~~~~~~~~~~~~~~~~~~~~~~~~~
This is working code for python2 and python3
"""

from __future__ import print_function

import jinja2

OUTPUT_FILE_PATH = '/tmp/file.out'
TEMPLATE_FILE_PATH = 'fixtures/1/template.in'

# Python2
# -------
# using the 'b' flag on unix-type systems returns a "str" object, so this means
# there is no change for python2 code.
#
# Python3
# -------
# using the 'b' flag returns a "bytes" object. Without it a "str" object is
# returned. An "str" object in python3 is equivalent to a "unicode" object in
# python2 whereas a "bytes" object in python3 is equivalent with a "str" in
# python2. So to ensure we have _roughly_ the same type of object in python2
# and python3 we add the 'b' flag.
with open(TEMPLATE_FILE_PATH, 'rb') as f:
    TEMPLATE_FILE = f.read()

def main():
    """
    Render a template with unicode, ensure the unicode exists
    """
    loader = {OUTPUT_FILE_PATH: TEMPLATE_FILE}
    loader = {n: f.decode('utf-8') for n, f in loader.items()}
    loader = jinja2.DictLoader(loader)
    env_args = {'loader': loader}
    env = jinja2.Environment(**env_args)
    template = env.get_template(OUTPUT_FILE_PATH)

    out = template.render().encode('utf-8')

    utf8_in_template = u'⚡'
    utf8_in_template = utf8_in_template.encode('utf-8')

    # Python2
    # -------
    #
    #     foo:
    #       - ⚡
    #       - bar
    #
    # because the str type is used for bytes as well as ascii text
    #
    # Python3
    # -------
    #
    #     b'foo:\n  - \xe2\x9a\xa1\n  - bar'
    #
    # because python3 has not str type and instead uses "bytes" to represent
    # binary data and ascii text.
    print(out)

    # Python2
    # -------
    #
    # <type 'str'>
    #
    # Which is roughly the same type as "bytes" in python3
    #
    # Python3
    # -------
    #
    # <class 'bytes'>
    print(type(out))

    # assert True
    assert utf8_in_template in out

    # Write the file
    #
    # Python2
    # -------
    #
    # Changing this to 'wb' has no real effect in python2 since out is a "str"
    # which is equivalent to the "bytes" object in python3
    #
    # Python3
    # -------
    #
    # the 'b' is crucuial, otherwise we'd need to somehow covert our bytes
    # object to a "str" (which in python3 contians unicode) and a "unicode"
    # object in python2 (which is distinct from a str which contains only ascii
    # and bytes). There doesn't seem to be a compatible way to do this, so just
    # add the 'b' flag to the write!
    with open(OUTPUT_FILE_PATH, 'wb') as f:
        f.write(out)


if __name__ == '__main__':
    main()
