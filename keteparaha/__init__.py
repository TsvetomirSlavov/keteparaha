# -*- coding: utf-8 -*-
"""A collection of tools to help when functional testing

It contains utilities that assist with tasks like running a browser in a
headless environment, or checking that emails have been sent, or a file has
been uploaded to a server, or common testing flow control like retrying or
ignoring certain errors.

Installation
------------

Keteparaha is available on PyPi. To install the latest release simply use:

    pip install keteparaha

License
-------

Keteparaha is released under the MIT license, see LICENSE in the software
repository for more details. Copyright 2015 by Hansel Dunlop.

"""

__version__ = '0.0.16'
from .email_client import GmailImapClient
from .page import Component, Page
from .browser import (
    BrowserTestCase,
    HeadlessBrowserTestCase,
    snapshot_on_error
)
from .flow import ignore, retry

__version__ = '0.0.12'
__all__ = ['BrowserTestCase', 'Component', 'Page']
