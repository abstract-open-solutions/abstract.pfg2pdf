# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from abstract.pfg2pdf.testing import ABSTRACT_PFG2PDF_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that abstract.pfg2pdf is properly installed."""

    layer = ABSTRACT_PFG2PDF_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if abstract.pfg2pdf is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('abstract.pfg2pdf'))

    def test_uninstall(self):
        """Test if abstract.pfg2pdf is cleanly uninstalled."""
        self.installer.uninstallProducts(['abstract.pfg2pdf'])
        self.assertFalse(self.installer.isProductInstalled('abstract.pfg2pdf'))

    def test_browserlayer(self):
        """Test that IAbstractPfg2PdfLayer is registered."""
        from abstract.pfg2pdf.interfaces import IAbstractPfg2PdfLayer
        from plone.browserlayer import utils
        self.assertIn(IAbstractPfg2PdfLayer, utils.registered_layers())
