from Acquisition import aq_inner
from Acquisition import aq_parent

from .interfaces import IFormToPDFAdapter


def on_create_form_adapter(context, event):

    form = aq_parent(aq_inner(context))
    set_redirect_view(form)


def set_redirect_view(form):
    """ apply `pdf_redirect` view on the thanks page
    """
    thanks_page_id = form.getThanksPage()
    if thanks_page_id in form.objectIds():
        thanks_page = form[thanks_page_id]
        thanks_page.setLayout('pdf_redirect')


def unset_redirect_view(form):
    """ remove `pdf_redirect` view on the thanks page
    """
    page_id = form.getThanksPage()
    page = getattr(form, page_id, None)
    if page and page.getLayout() == 'pdf_redirect':
        # default view
        try:
            page.fg_thankspage_view_p3
            page.setLayout('fg_thankspage_view_p3')
        except AttributeError:
            # XXX: looks like in version 1.7.17
            # there's no template w/ this id :S
            # page.setLayout('fg_thankspage_view_p3')
            # fallback to base view....
            page.setLayout('base_view')


def on_delete_form_adapter(context, event):
    form = context.aq_parent
    unset_redirect_view(form)


def on_edit_form(context, event):
    form = context
    pdf_on = False
    for action_id in form.getActionAdapter():
        if IFormToPDFAdapter.providedBy(form[action_id]):
            pdf_on = True
            break
    if pdf_on:
        set_redirect_view(form)
    else:
        unset_redirect_view(form)
