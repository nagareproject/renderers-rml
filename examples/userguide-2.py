# Encoding: UTF-8
# --
# Copyright (c) 2008-2018 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.trt, which you should have received as part of
# this distribution.
# --

from nagare.renderers import rml


def sample(output):
    r = rml.Renderer()

    with r.document:
        with r.template:
            with r.pageTemplate(id='main'):
                with r.pageGraphics:
                    r << r.fill(color='red')
                    r << r.setFont(name='Helvetica', size=24)
                    r << r. drawCentredString('Lines in RML.', x=297.5, y=800)

                    r << r.lineMode(width=1)
                    r << r.lines('1in 10.5in 2in 10.5in 2in 10.5in 1.5in 10in 1.5in 10in 1.5in 10.75in')
                    r << r.fill(color='black')
                    r << r.setFont(name='Helvetica', size=9)
                    r << r.drawCentredString('width=1', x='1.5 in', y='9.75 in')

                    r << r.lineMode(width=5)
                    r << r.lines('2.5in 10.5in 3.5in 10.5in 3.5in 10.5in 3in 10in 3in 10in 3in 10.75in')
                    r << r.drawCentredString('width=5', x='3 in', y='9.75 in')

                    r << r.lineMode(width=10)
                    r << r.lines('4in 10.5in 5in 10.5in 5in 10.5in 4.5in 10in 4.5in 10in 4.5in 10.75in')
                    r << r.drawCentredString('width=10', x='4.5 in', y='9.75 in')

                    r << r.lineMode(width=15)
                    r << r.lines('5.5in 10.5in 6.5in 10.5in 6.5in 10.5in 6in 10in 6in 10in 6in 10.75in')
                    r << r.drawCentredString('width=15', x='6 in', y='9.75 in')

                    r << r.lineMode(width=5)
                    r << r.lines('1in 9in 2in 9in 2in 9in 1.5in 8.5in 1.5in 8.5in 1.5in 9.25in')
                    r << r.fill(color='black')
                    r << r.setFont(name='Helvetica', size=9)
                    r << r.drawCentredString('width=5', x='1.5 in', y='8.25 in')

                    r << r.lineMode(width='5', join='round')
                    r << r.lines('2.5in 9in 3.5in 9in 3.5in 9in 3in 8.5in 3in 8.5in 3in 9.25in')
                    r << r.drawCentredString('width=5, join=round', x='3 in', y='8.25 in')

                    r << r.lineMode(idth='5', join='mitered')
                    r << r.lines('4in 9in 5in 9in 5in 9in 4.5in 8.5in 4.5in 8.5in 4.5in 9.25in')
                    r << r.drawCentredString('width=5, join=mitered', x='4.5 in', y='8.25 in')

                    r << r.lineMode(width='5', join='bevelled')
                    r << r.lines('5.5in 9in 6.5in 9in 6.5in 9in 6in 8.5in 6in 8.5in 6in 9.25in')
                    r << r.drawCentredString('width=5, join=bevelled', x='6 in', y='8.25 in')

                    r << r.lineMode(width=10)
                    r << r.lines('1in 7.5in 2in 7.5in 2in 7.5in 1.5in 7in 1.5in 7in 1.5in 7.75in')
                    r << r.fill(color='black')
                    r << r.setFont(name='Helvetica', size=9)
                    r << r.drawCentredString('width=10', x='1.5 in', y='6.75 in')

                    r << r.lineMode(width='10', cap='default')
                    r << r.lines('2.5in 7.5in 3.5in 7.5in 3.5in 7.5in 3in 7in 3in 7in 3in 7.75in')
                    r << r.drawCentredString('width=10, cap=default', x='3 in', y='6.75 in')

                    r << r.lineMode(width=10, cap='round')
                    r << r.lines('4in 7.5in 5in 7.5in 5in 7.5in 4.5in 7in 4.5in 7in 4.5in 7.75in')
                    r << r.drawCentredString('width=10, cap=round', x='4.5 in', y='6.75 in')

                    r << r.lineMode(width=10, cap='square')
                    r << r.lines('5.5in 7.5in 6.5in 7.5in 6.5in 7.5in 6in 7in 6in 7in 6in 7.75in')
                    r << r.drawCentredString('width=10, cap=square', x='6 in', y='6.75 in')

                    r << r.lineMode(width='5', cap='default')
                    r << r.lineMode(width='5', join='mitered')
                    r << r.lines('1in 6in 2in 6in 2in 6in 1.5in 5.5in 1.5in 5.5in 1.5in 6.25in')
                    r << r.fill(color='black')
                    r << r.setFont(name='Helvetica', size=9)
                    r << r.drawCentredString('width=5, join=mitered', x='1.5 in', y='5.25 in')

                    r << r.lineMode(width=5, join='mitered', miterLimit=10)
                    r << r.lines('2.5in 6in 3.5in 6in 3.5in 6in 3in 5.5in 3in 5.5in 3in 6.25in')
                    r << r.drawCentredString('width=5, join=mitered', x='3 in', y='5.25 in')
                    r << r.drawCentredString('miterLimit=10', x='3 in', y='5.1 in')

                    r << r.lineMode(width=10, join='mitered')
                    r << r.lines('4in 6in 5in 6in 5in 6in 4.5in 5.5in 4.5in 5.5in 4.5in 6.25in')
                    r << r.drawCentredString('width=10, join=mitered', x='4.5 in', y='5.25 in')

                    r << r.lineMode(width=10, join='mitered', miterLimit=20)
                    r << r.lines('5.5in 6in 6.5in 6in 6.5in 6in 6in 5.5in 6in 5.5in 6in 6.25in')
                    r << r.drawCentredString('width=10, join=mitered', x='6 in', y='5.25 in')
                    r << r.drawCentredString('miterLimit=20', x='6 in', y='5.1 in')

                    r << r.lineMode(width=2)
                    r << r.lines('1in 4.5in 2in 4.5in 2in 4.5in 1.5in 4in 1.5in 4in 1.5in 4.75in')
                    r << r.fill(color='black')
                    r << r.setFont(name='Helvetica', size=9)
                    r << r.drawCentredString('width=2', x='1.5 in', y='3.75 in')

                    r << r.lineMode(width='2', dash='5,5')
                    r << r.lines('2.5in 4.5in 3.5in 4.5in 3.5in 4.5in 3in 4in 3in 4in 3in 4.75in')
                    r << r.drawCentredString('width=2, dash=5,5', x='3 in', y='3.75 in')

                    r << r.lineMode(width=2, dash='2,10')
                    r << r.lines('4in 4.5in 5in 4.5in 5in 4.5in 4.5in 4in 4.5in 4in 4.5in 4.75in')
                    r << r.drawCentredString('width=2, dash=2,10', x='4.5 in', y='3.75 in')

                    r << r.lineMode(width='2', dash='5,5,2,10')
                    r << r.lines('5.5in 4.5in 6.5in 4.5in 6.5in 4.5in 6in 4in 6in 4in 6in 4.75in')
                    r << r.drawCentredString('width=2, dash=5,5,2,10', x='6 in', y='3.75 in')

                r << r.frame(id='first', x1=72, y1=72, width=451, height=698)

        r << r.stylesheet
        r << r.story(r.para)

    return r.root.topdffile(output)


if __name__ == '__main__':
    sample('/tmp/sample.pdf')
