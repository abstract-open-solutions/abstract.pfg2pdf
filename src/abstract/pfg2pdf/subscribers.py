from Acquisition import aq_inner
from Acquisition import aq_parent


def on_create_form_adapter(context, event):
    """ apply `pdf_redirect` view to the thanks page
    """
    form = aq_parent(aq_inner(context))
    thanks_page_id = form.getThanksPage()
    if thanks_page_id in form.objectIds():
        thanks_page = form[thanks_page_id]
        thanks_page.setLayout('pdf_redirect')
