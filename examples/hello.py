# Encoding: UTF-8
# --
# Copyright (c) 2008-2021 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --

from nagare.renderers import rml


def sample(output):
    r = rml.Renderer()

    with r.document(invariant=1):
        r << r.stylesheet

        with r.pageDrawing:
            with r.drawCentredString(x='4.1in', y='5.8in'):
                r << 'Hello World. First Page Drawing'

        with r.pageDrawing:
            with r.drawCentredString(x='4.1in', y='5.8in'):
                r << 'Hello World. Second Page Drawing'

    return r.root.topdffile(output)


if __name__ == '__main__':
    sample('/tmp/sample.pdf')
