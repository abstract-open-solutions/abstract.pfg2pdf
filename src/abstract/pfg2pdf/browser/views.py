# -*- coding: utf-8 -*-

import urllib

from Products.Five import BrowserView
from plone.api.portal import show_message
from zope.i18nmessageid.message import Message
from zope.security import checkPermission

from abstract.wkhtmltopdf import PDFRenderer
from abstract.pfg2pdf import _


class RedirectView(BrowserView):

    default_refresh_timeout = 5
    download_view = 'pdf_download'

    def can_edit(self):
        return checkPermission('cmf.ModifyPortalContent', self.context)

    def download_url(self):
        url = self.request.get('pdf_adapter_url')
        if url:
            data = self.request.get('pdf_data')
            return '/'.join([
                url.rstrip('/'),
                self.download_view + '?' + urllib.urlencode(data)
            ])
        return url

    @property
    def refresh_timeout(self):
        return self.request.get('download_timeout',
                                self.default_refresh_timeout)

    def get_metatag_refresh(self):

        url = self.download_url()
        if url:
            return "%s; url=%s" % (self.refresh_timeout,
                                   url)


class DownloadView(BrowserView):

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
            fname = self.context.getId()
            return self._render_pdf(compiled_tmpl, fname=fname)

    def get_data(self):
        return self.request

    def _render_pdf(self, content, fname='download.me.pdf'):
        if not fname.endswith('.pdf'):
            fname += '.pdf'
        renderer = PDFRenderer()
        self.request.response.setHeader(
            'Content-Type',
            'application/pdf')
        self.request.response.setHeader(
            'Content-Disposition',
            'attachment; filename="%s"' % fname)
        return renderer(content)
