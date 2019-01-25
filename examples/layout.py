# Encoding: UTF-8
# --
# Copyright (c) 2008-2019 Net-ng.
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
        with r.stylesheet:
            with r.blockTableStyle(id='style'):
                r << r.blockAlignment(value='center')
                r << r.lineStyle(kind='box', colorName='#336699')
                r << r.lineStyle(kind='lineabove', colorName='red', start='0,1', end='1,-1')

        with r.template:
            with r.pageTemplate(id='main'):
                r << r.frame(id='one', x1='1cm', y1='15cm', width='19cm', height='10cm')
                r << r.frame(id='two', x1='1cm', y1='1cm', width='19cm', height='10cm')

        with r.story:
            r << r.title('Title on page 1') << r.nextPage
            r << r.title('Title on page 2')

            r << r.para(u'héhéhé')
            r << r.hr(width='80%', spaceBefore=5, spaceAfter=5)
            with r.blockTable(rowHeights='1.25cm 1.25cm', colWidths='4cm, 2cm', style='style'):
                with r.tr:
                    with r.td:
                        with r.para:
                            r << 'Bold'
                            r << ' and red text '
                            r << r.link('Net-ng', destination='http://www.net-ng.com')
                    r << r.td(42)

                with r.tr:
                    r << r.td('Laaaaaaaaarge')

    return r.root.topdffile(output)


if __name__ == '__main__':
    sample('/tmp/sample.pdf')
