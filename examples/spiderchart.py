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

    with r.document:
        with r.template:
            with r.pageTemplate(id='main'):
                r << r.frame(id='one', x1='1cm', y1='15cm', width='19cm', height='10cm')
                r << r.frame(id='two', x1='1cm', y1='1cm', width='19cm', height='10cm')

        with r.pageDrawing:
            r << r.setFont(name='Helvetica-Bold', size=16)
            r << r.drawCenteredString('Spider Chart Demo', x='4.1in', y='11in')

            with r.spiderChart(dx='2in', dy='7in', dwidth='6in', dheight='4in', x=0, y=0, width='3in', height='3in'):
                with r.labels:
                    r << (r.label(letter) for letter in 'abcdef')

                with r.strands:
                    r << [r.strand(stokeColor=color, fillColor=color) for color in ('cornsilk', 'cyan', 'palegreen')]

                with r.data:
                    for serie in ((12, 14, 16, 14, 12), (6, 8, 10, 12, 9, 15), (7, 8, 17, 4, 12, 8)):
                        r << r.series(' '.join(str(i) for i in serie))

    return r.root.topdffile(output)


if __name__ == '__main__':
    sample('/tmp/sample.pdf')
