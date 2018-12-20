#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
The Curious Case Encoding
~~~~~~~~~~~~~~~~~~~~~~~~~
This is working code for python2
"""

from __future__ import print_function

import jinja2

OUTPUT_FILE_PATH = '/tmp/file.out'
TEMPLATE_FILE_PATH = 'fixtures/1/template.in'

with open(TEMPLATE_FILE_PATH) as f:
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
    utf8_in_template = '⚡'

    # foo:
    #   - ⚡
    #   - bar
    print(out)

    # <type 'str'>
    print(type(out))

    # assert True
    assert utf8_in_template in out

    # Write the file
    with open(OUTPUT_FILE_PATH, 'w') as f:
        f.write(out)


if __name__ == '__main__':
    main()
