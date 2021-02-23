# --
# Copyright (c) 2008-2021 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --

"""RML renderer"""

from lxml import etree
from zope import schema
from z3c.rml import document
from nagare.renderers import xml
from reportlab.platypus.para import Para


class DummyFile(object):

    def __init__(self):
        self.content = ''

    def write(self, content):
        self.content = content

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass


class Tag(xml.Tag):

    def init(self, renderer):
        super(Tag, self).init(renderer)

        self.sourceline = 1

    def topdffile(self, filename):
        def init_canvas(doc, init_canvas, canvas, filename):
            if not doc.postProcessors:
                canvas._filename = filename

            init_canvas(canvas)

        doc = document.Document(self)
        doc._initCanvas = lambda canvas, f=doc._initCanvas: init_canvas(doc, f, canvas, filename)

        with (open(filename, 'w') if doc.postProcessors else DummyFile()) as output_file:
            doc.process(output_file)

    def topdfstring(self):
        doc = document.Document(self)

        with DummyFile() as output_file:
            doc.process(output_file)

            return output_file.content


class Renderer(xml.XmlRenderer):

    doctype = '<!DOCTYPE document SYSTEM "rml.dtd">'
    content_type = 'application/pdf'
    namespace = 'http://namespaces.zope.org/rml'

    _parser = etree.XMLParser()
    _parser.set_element_class_lookup(etree.ElementDefaultClassLookup(element=Tag))

    def __init__(self, parent=None, *args, **kw):
        super(Renderer, self).__init__(parent, *args, **kw)

        self.namespaces = {None: self.namespace}

    @classmethod
    def get_tags(cls, tags, tag, signature):
        if tag not in tags:
            tags[tag] = set(schema.getFields(signature))

            for child in signature.queryTaggedValue('directives', ()):
                cls.get_tags(tags, child.tag, child.signature)

        return tags

    @classmethod
    def create_RML_tags(cls):
        for tag, signature in cls.get_tags({}, 'document', document.IDocument).items():
            setattr(cls, tag, xml.TagProp(tag, signature))

    @classmethod
    def create_para_extra_tags(cls):
        tags = [method[8:] for method in Para.__dict__ if method.startswith('compile_')]

        for tag in tags:
            setattr(cls, tag, xml.TagProp(tag))


Renderer.create_RML_tags()
Renderer.create_para_extra_tags()
