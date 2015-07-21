==============================================================================
abstract.pfg2pdf
==============================================================================

A PFG action for creating and downloading a PDF built with data from user input.

PDF download happens as you submit the form.


Usage
-----

Add Form Folder and add a `FormToPDFAdapter` to it.

On the adapter, in the field `PDF-Body Template` you can insert the ZPT code that will be used to generate the PDF.


Installation
------------

Install abstract.pfg2pdf by adding it to your buildout::

   [buildout]

    ...

    eggs =
        abstract.pfg2pdf


and then running "bin/buildout"


Dependencies
------------

Depends on `abstract.wkhtmltopdf <https://github.com/abstract-open-solutions/abstract.wkhtmltopdf>`_ to generate the PDF.



TODO
----

* handle redirect to thank you page


Contribute
----------

- Issue Tracker: https://github.com/abstract-open-solutions/abstract.pfg2pdf/issues
- Source Code: https://github.com/abstract-open-solutions/abstract.pfg2pdf
- Documentation: https://github.com/abstract-open-solutions


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@example.com

License
-------

The project is licensed under the GPLv2.
