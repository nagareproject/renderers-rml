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
                with r.pageGraphics:
                    r << r.fill(color='red')
                    r << r.setFont(name='Helvetica', size=24)
                    r << r.drawCentredString('Simple Text and Graphics with RML.', x=297.5, y=800)

                    r << r.fill(color='red')
                    r << r.circle(x=127.5, y=672.75, radius='1 in', fill='no', stroke='yes')

                    r << r.fill(color='green')
                    r << r.stroke(color='black')
                    r << r.circle(x=297.5, y=672.75, radius='1 in', fill='yes', stroke='no')

                    r << r.fill(color='blue')
                    r << r.stroke(color='black')
                    r << r.circle(x=467.5, y=672.75, radius='1 in', fill='yes', stroke='yes')

                    r << r.fill(color='black')
                    r << r.setFont(name='Helvetica', size=9)

                    r << r.drawCentredString('Circle - with stroke, but no fill.', x=127.5, y=567.5)
                    r << r.drawCentredString('Circle - with fill, but no stroke.', x=297.5, y=567.5)
                    r << r.drawCentredString('Circle - with both stroke and fill.', x=467.5, y=567.5)

                    r << r.fill(color='red')
                    r << r.ellipse(x=77, y=382.25, width=100, height=150, fill='no', stroke='yes')
                    r << r.fill(color='green')
                    r << r.stroke(color='black')
                    r << r.ellipse(x=247, y=382.25, width=100, height=150, fill='yes', stroke='no')
                    r << r.fill(color='blue')
                    r << r.stroke(color='black')
                    r << r.ellipse(x=417, y=382.25, width=100, height=150, fill='yes', stroke='yes')

                    r << r.fill(color='black')
                    r << r.drawCentredString('Ellipse - with stroke, but no fill.', x=127.5, y=357)
                    r << r.drawCentredString('Ellipse - with fill, but no stroke.', x=297.5, y=357)
                    r << r.drawCentredString('Ellipse - with both stroke and fill.', x=467.5, y=357)

                    r << r.rect(x=84.5, y=214.3, width='1 in', height='1.15 in', fill='no', stroke='yes')
                    r << r.fill(color='green')
                    r << r.stroke(color='black')
                    r << r.rect(x=254.5, y=214.3, width='1 in', height='1.15 in', fill='yes', stroke='no')
                    r << r.fill(color='blue')
                    r << r.stroke(color='black')
                    r << r.rect(x=424.5, y=214.3, width='1 in', height='1.15 in', fill='yes', stroke='yes')

                    r << r.fill(color='black')
                    r << r.drawCentredString('Rect - with stroke, but no fill.', x=127.5, y=199.1)
                    r << r.drawCentredString('Rect - with fill, but no stroke.', x=297.5, y=199.1)
                    r << r.drawCentredString('Rect - with both stroke and fill.', x=467.5, y=199.1)

                    r << r.rect(x=84.5, y=56.5, width='1 in', height='1.15 in', fill='no', stroke='yes', round='0.15 in')
                    r << r.fill(color='green')
                    r << r.stroke(color='black')
                    r << r.rect(x=254.5, y=56.5, width='1 in', height='1.15 in', fill='yes', stroke='no', round='0.15 in')
                    r << r.fill(color='blue')
                    r << r.stroke(color='black')
                    r << r.rect(x=424.5, y=56.5, width='1 in', height='1.15 in', fill='yes', stroke='yes', round='0.15 in')
                    r << r.fill(color='black')
                    r << r.drawCentredString('Rect - with stroke and round, but no fill.', x=127.5, y=41.25)
                    r << r.drawCentredString('Rect - with fill and round, but no stroke.', x=297.5, y=41.25)
                    r << r.drawCentredString('Rect - with stroke, fill and round.', x=467.5, y=41.25)

                r << r.frame(id='first', x1='0.5in', y1='0.5in', width='20cm', height='28cm')

        r << r.stylesheet

        with r.story:
            with r.para:
                r << r.font('This is courier in crimson!', face='Courier', color='crimson')
                r << r.super('hello') << r.sub('world')

    return r.root.topdffile(output)


if __name__ == '__main__':
    sample('/tmp/sample.pdf')
