==============================================================================
abstract.pfg2pdf
==============================================================================

A PFG action for creating and downloading a PDF built with data from user input.


Usage
-----

Add Form Folder and add a `FormToPDFAdapter` to it.

On the adapter, in the field `PDF-Body Template` you can insert the ZPT code that will be used to generate the PDF. In the field `download timeout` you can set the amount of seconds that will pass
before the download starts.

Once you add the form adapter to the form, the `pdf_redirect` view will be applied
to the thanks page configured in the form. In this way, whenever the user gets to the final page
the download will start after the timeout you set on the adapter.


NOTE: if you create/change the thanks page associated w/ the form, remember to apply the view to it.

You can do it by goint to this URL: `http://myplone/myform/thanks-page/setLayout?layout=pdf_redirect`.


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
