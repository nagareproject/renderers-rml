# Encoding: UTF-8
# --
# Copyright (c) 2008-2022 Net-ng.
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
        with r.template(pageSize='letter', leftMargin=72, showBoundary=1):
            with r.pageTemplate(id='main', pageSize='letter portrait'):
                with r.pageGraphics:
                    r << r.setFont(name='Helvetica-BoldOblique', size=18)
                    r << r.drawRightString('RML2PDF Test Suite', x=523, y=800)

                    with r.textAnnotation:
                        r << r.param('0,0,1,1', name='Rect')
                        r << r.param(3, name='F')
                        r << r.param(6, name='escape')
                        r << '''X::PDF
                        PX(S)
                        MT(PINK)
                        '''
                r << r.frame(id='first', x1='1in', y1='1in', width='6.27in', height='9.69in')

        with r.stylesheet:
            with r.initialize:
                r << r.alias(id='style.normal', value='style.Normal')

            r << r.paraStyle(name='h1', fontName='Helvetica-BoldOblique', fontSize=32, leading=36)
            r << r.paraStyle(name='normal', fontName='Helvetica', fontSize=10, leading=12)
            r << r.paraStyle(name='spaced', fontName='Helvetica', fontSize=10, leading=12, spaceBefore=12, spaceAfter=12)

        with r.story:
            with r.para(style='normal'):
                r << u'Il était là. Hello World.  This is a normal paragraph. Blah '
                r << r.font('IPO ', color='red')
                r << 'blah blah blah blah growth forecast blah '
                r << 'blah blah forecast blah.Blah blah blah blah blah blah blah blah blah blah blah profit blah blah blah blah blah '
                r << 'blah blah blah blah blah IPO.Blah blah blah blah blah blah blah reengineering blah growth blah blah blah '
                r << 'proactive direction strategic blah blah blah forward-thinking blah.Blah blah doubletalk blah blah blah blah '
                r << 'blah profit blah blah growth blah blah blah blah blah profit.Blah blah blah blah venture capital blah blah blah '
                r << 'blah blah forward-thinking blah.'

            with r.para(style='normal'):
                r << 'This is another normal paragraph. Blah IPO blah blah blah blah growth forecast blah '
                r << 'blah blah forecast blah.Blah blah blah blah blah blah blah blah blah blah blah profit blah blah blah blah blah '
                r << 'blah blah blah blah blah IPO.Blah blah blah blah blah blah blah reengineering blah growth blah blah blah '
                r << 'proactive direction strategic blah blah blah forward-thinking blah.Blah blah doubletalk blah blah blah blah '
                r << 'blah profit blah blah growth blah blah blah blah blah profit.Blah blah blah blah venture capital blah blah blah '
                r << 'blah blah forward-thinking blah.'

            r << r.para('I should NOT have a tiny leading space in front of me!', style='normal')

            r << r.para('This is spaced.  There should be 12 points before and after.', style='spaced')

            with r.para(style='normal'):
                r << 'Hello World.  This is a normal paragraph. Blah IPO blah blah blah blah growth forecast blah '
                r << 'blah blah forecast blah.Blah blah blah blah blah blah blah blah blah blah blah profit blah blah blah blah blah '
                r << 'blah blah blah blah blah IPO.Blah blah blah blah blah blah blah reengineering blah growth blah blah blah '
                r << 'proactive direction strategic blah blah blah forward-thinking blah.Blah blah doubletalk blah blah blah blah '
                r << 'blah profit blah blah growth blah blah blah blah blah profit.Blah blah blah blah venture capital blah blah blah '
                r << 'blah blah forward-thinking blah.'

    return r.root.topdffile(output)


if __name__ == '__main__':
    sample('/tmp/sample.pdf')
