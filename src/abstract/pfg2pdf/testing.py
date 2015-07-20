# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import abstract.pfg2pdf


class AbstractPfg2PdfLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=abstract.pfg2pdf)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'abstract.pfg2pdf:default')


ABSTRACT_PFG2PDF_FIXTURE = AbstractPfg2PdfLayer()


ABSTRACT_PFG2PDF_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ABSTRACT_PFG2PDF_FIXTURE,),
    name='AbstractPfg2PdfLayer:IntegrationTesting'
)


ABSTRACT_PFG2PDF_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ABSTRACT_PFG2PDF_FIXTURE,),
    name='AbstractPfg2PdfLayer:FunctionalTesting'
)


ABSTRACT_PFG2PDF_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ABSTRACT_PFG2PDF_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='AbstractPfg2PdfLayer:AcceptanceTesting'
)
