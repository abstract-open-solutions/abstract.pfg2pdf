# -*- coding: utf-8 -*-

from Products.Five import BrowserView
from plone.api.portal import show_message
from zope.i18nmessageid.message import Message

from abstract.wkhtmltopdf import PDFRenderer
from abstract.pfg2pdf import _


class PDFView(BrowserView):

    err_msg = _(u'Something went wrong, please check your template!')

    def __call__(self):
        data = self.get_data()
        tmpl_field = self.context.getField('pdf_body_pt')
        compiled_tmpl = tmpl_field.get(self.context, **data)
        if isinstance(compiled_tmpl, Message):
            # we got an error...
            show_message(self.err_msg)
            return
        else:
            return self._render_pdf(compiled_tmpl)

    def get_data(self):
        return self.request

    def _render_pdf(self, content, fname='download.me.pdf'):
        renderer = PDFRenderer()
        self.request.response.setHeader(
            'Content-Type',
            'application/pdf')
        self.request.response.setHeader(
            'Content-Disposition',
            'attachment; filename="%s.pdf"' % fname)
        return renderer(content)
