# Encoding: UTF-8
# --
# Copyright (c) 2008-2023 Net-ng.
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
        with r.template(
            pageSize='(21cm, 29.7cm)',
            leftMargin='2.5cm',
            rightMargin='2.5cm',
            topMargin='2.5cm',
            bottomMargin='2.5cm',
            title='Example 5 - templates and pageTemplates',
            author='Reportlab Inc (Documentation Team)',
            showBoundary=1,
            allowSplitting=1,
        ):
            with r.pageTemplate(id='main'):
                r << r.pageGraphics
                r << r.frame(id='titleBox', x1='2.5cm', y1='27.7cm', width='16cm', height='1cm')
                r << r.frame(id='columnOne', x1='2.5cm', y1='2.5cm', width='7.5cm', height='24.7cm')
                r << r.frame(id='columnTwo', x1='11cm', y1='2.5cm', width='7.5cm', height='24.7cm')

        with r.stylesheet:
            with r.initialize:
                r << r.name(id='FileTitle', value='Example 5 - templates and pageTemplates')
                r << r.name(id='ColumnOneHeader', value='This is Column One')
                r << r.name(id='ColumnTwoHeader', value='This is Column Two')

            r << r.paraStyle(
                name='titleBox', fontName='Helvetica-Bold', fontSize=18, spaceBefore='0.4 cm', alignment='CENTER'
            )
            r << r.paraStyle(name='body', fontName='Helvetica', fontSize=10, leftIndent=5, spaceAfter=5)

        with r.story:
            with r.para(style='titleBox'):
                r << r.b(r.getName(id='FileTitle'))

            r << r.nextFrame
            r << r.condPageBreak(height=144)

            r << r.h2(r.getName(id='ColumnOneHeader'))

            r << r.para('This is the contents for ', r.b('column one'), '.')
            r << r.para('It uses the default style for paragraph.')
            r << r.para('Does it come out OK?')
            r << r.para('There now follows some random text to see how these paragraphs look with longer content:')
            r << r.para(
                'Blah blah morale blah benchmark blah blah blah blah blah blah'
                'communication blah blah blah blah blah blah blah blah blah'
                'blah stretch the envelope blah blah blah.'
            )
            r << r.para(
                'Blah blah blah blah blah blah blah blah blah blah blah blah'
                'architect blah inter active backward-compatible blah blah blah'
                'blah blah. Blah blah blah blah value-added.'
            )
            r << r.para(
                'Blah blah blah blah blah blah blah blah blah re-factoring'
                'phase blah knowledge management blah blah. Blah blah blah blah'
                'interactive blah vision statement blah.'
            )
            r << r.para(
                'Blah blah blah blah blah blah conceptualize blah downsize blah'
                'blah blah blah. Blah blah blah blah blah blah blah blah blah'
                'blah blah blah synergy client-centered vision statement.'
            )
            r << r.para(
                'Blah blah dysfunctional blah blah blah blah blah blah blah'
                'appropriate blah blah blah blah blah blah blah blah'
                're-factoring go the extra mile blah blah blah blah.'
            )

            r << r.nextFrame
            r << r.condPageBreak(height=144)

            r << r.h2(r.getName(id='ColumnTwoHeader'))

            r << r.para('This is the contents for ', r.i('column two'), '.', style='body')
            r << r.para('It uses the paragraph style we have called "body".', style='body')
            r << r.para('Does it come out OK?', style='body')
            with r.para(style='body'):
                r << 'There now follows some random text to see how these paragraphs'
                r << 'look with longer content:'
            with r.para(style='body'):
                r << 'Blah OS/2 blah blah blah blah coffee blah blah blah blah'
                r << 'Windows blah blah blah blah blah blah blah. Blah blah blah'
                r << 'blah blah blah blah Modula-3 blah blah blah. Blah blah bug'
                r << 'report blah blah blah blah blah memory blah blah TeX TCP/IP'
                r << 'SMTP blah blah.'
            with r.para(style='body'):
                r << 'Blah blah blah blah blah Em blah letterform blah blah blah'
                r << 'blah blah blah blah blah blah letterform blah blah. Blah blah'
                r << 'blah blah leader blah blah blah blah.'
            with r.para(style='body'):
                r << 'Blah blah blah blah blah uppercase blah blah right justified'
                r << 'blah blah blah flush-right blah blah blah. Blah blah blah blah'
                r << 'blah blah spot-colour blah Em.'
            with r.para(style='body'):
                r << 'Blah dingbat blah blah blah blah blah blah blah blah blah blah'
                r << 'blah blah blah blah blah. Blah blah blah blah blah drop-cap'
                r << 'blah blah blah blah blah blah blah.'

    return r.root.topdffile(output)


if __name__ == '__main__':
    sample('/tmp/sample.pdf')
