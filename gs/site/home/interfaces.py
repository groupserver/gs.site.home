# coding=utf-8
from zope.viewlet.interfaces import IViewletManager

# Metadata
class ISiteHomeMetadata(IViewletManager):
    '''Viewlet manager for the metadata on the site homepage.'''

# Body
class ISiteHomeIntroduction(IViewletManager):
    '''The initial text, which is considered very important.'''

class ISiteHomeMain(IViewletManager):
    '''The left column, which is normally used for static data.'''

class ISiteHomeSecondary(IViewletManager):
    '''The left column, which is normally used for static data.'''

class ISiteHomeActivity(IViewletManager):
    '''Some tabs, which are very similar to the Tabs shown on the Group page.'''

class ISiteHomeEpilogue(IViewletManager):
    '''Unimportant information that appears at the bottom of the page.'''

# JavaScript
class ISiteHomeJS(IViewletManager):
    '''The JavaScript text for the site homepage'''
