"""Definition of the FormToPDFAdapter content type
"""

# from Acquisition import aq_inner
# from Acquisition import aq_parent
from AccessControl import ClassSecurityInfo

from zope.interface import implements
# from zope.component import getMultiAdapter

from Products.Archetypes import atapi
from Products.ATContentTypes.content import schemata
# from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.CMFCore.permissions import ModifyPortalContent

from Products.PloneFormGen.content.actionAdapter import FormActionAdapter
from Products.PloneFormGen.content.actionAdapter import FormAdapterSchema
from Products.PloneFormGen.config import EDIT_TALES_PERMISSION

from Products.TemplateFields import ZPTField


from abstract.pfg2pdf.interfaces import IFormToPDFAdapter
from abstract.pfg2pdf.config import PROJECTNAME
from abstract.pfg2pdf import _


FormToPDFAdapterSchema = FormAdapterSchema.copy() + atapi.Schema((

    ZPTField(
        'pdf_body_pt',
        # schemata='template',
        write_permission=EDIT_TALES_PERMISSION,
        default_method='getPDFBodyDefault',
        read_permission=ModifyPortalContent,
        widget=atapi.TextAreaWidget(
            label=_(
                _(u'PDF-Body Template')
            ),
            description=_(
                _(u"This is a Zope Page Template "
                  u"used for rendering of the PDF for this form. "
                  u"You will find data from the form "
                  u"in the `options` var (es: options/comments)")
            ),
            rows=20,
            visible={'edit': 'visible', 'view': 'invisible'},
        ),
        validators=('zptvalidator',),
    ),

    atapi.IntegerField(
        'download_timeout',
        storage=atapi.AnnotationStorage(),
        widget=atapi.IntegerWidget(
            label=_(u"Download Timeout"),
            description=_(u"How many seconds should pass "
                          u"before downloading the PDF?"),
        ),
        validators=('isInt'),
        default=5,
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

FormToPDFAdapterSchema['title'].storage = atapi.AnnotationStorage()
FormToPDFAdapterSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(FormToPDFAdapterSchema, moveDiscussion=False)


class FormToPDFAdapter(FormActionAdapter):
    """Description of the Example Type"""
    implements(IFormToPDFAdapter)

    portal_type = meta_type = "FormToPDFAdapter"
    schema = FormToPDFAdapterSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    security = ClassSecurityInfo()

    security.declarePrivate('getPDFBodyDefault')

    def getPDFBodyDefault(self): # noqa
        """ Get default pdf template """

        return ''

    security.declarePrivate('onSuccess')

    def onSuccess(self, fields, REQUEST=None): # noqa
        """ redirect to pdf download view
        """
        request = REQUEST or self.REQUEST
        data = {}
        for k, v in request.form.iteritems():
            data[k] = v
        request.set('pdf_data', data)
        request.set('pdf_adapter_path', self.absolute_url_path())
        request.set('pdf_adapter_url', self.absolute_url())
        request.set('download_timeout',
                    self.getField('download_timeout').get(self))


atapi.registerType(FormToPDFAdapter, PROJECTNAME)
