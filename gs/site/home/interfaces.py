# coding=utf-8
from zope.viewlet.interfaces import IViewletManager

# Metadata
class ISiteHomeMetadata(IViewletManager):
    '''Viewlet manager for the metadata on the site homepage.'''

# Body
class ISiteHomeIntroduction(IViewletManager):
    '''The initial text, which is considered very important.'''

class ISiteHomeLeftColumn(IViewletManager):
    '''The left column, which is normally used for static data.'''

class ISiteHomeRightColumn(IViewletManager):
    '''The right column, which is normally used for dynamic information.'''

class ISiteHomeActivity(IViewletManager):
    '''Some tabs, which are very similar to the Tabs shown on the Group page.'''

class ISiteHomeEpilogue(IViewletManager):
    '''Unimportant information that appears at the bottom of the page.'''

# JavaScript
class ISiteHomeJS(IViewletManager):
    '''The JavaScript text for the site homepage'''

