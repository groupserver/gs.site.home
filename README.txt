Introduction
============

This egg provides the core support for the site homepage, or *the* homepage
as it should be known. Most of what it provides is an single page that
contains some viewlet managers, to provide the page `structure`_. The
actual content of the page is provided by other products.

Structure
=========

There are seven sections on the homepage, each provided by a different 
viewlet manager. Five are visible in the body of the page:

``ISiteHomeIntroduction``:
  The initial text, which is considered very important.

``ISiteHomeLeftColumn``:
  The left column, which is normally used for static data.

``ISiteHomeRightColumn``:
  The right column, which is normally used for dynamic information.

``ISiteHomeActity``: 
  The activity on the site. These are shown as *tabs*, which are very
  similar to the Tabs shown on the Group page [#group]_. The tabs are
  contained within the right-hand column of the site homepage.

``ISiteHomeEpilogue``:
  Unimportant information that appears at the bottom of the page.

There are two viewlet managers that are not visible. One for the metadata
(``ISiteHomeMetadata``) and one for some JavaScript (``ISiteHomeJS``).

The layout of the seven viewlet managers is as follows::

  ┌─Page───────────────────────────────────────────┐
  │┌─Metadata─────────────────────────────────────┐│
  ││ ISiteHomeMetadata                            ││
  │└──────────────────────────────────────────────┘│
  │┌─Body─────────────────────────────────────────┐│
  ││┌────────────────────────────────────────────┐││
  │││ ISiteHomeIntroduction                      │││
  ││└────────────────────────────────────────────┘││
  ││┌─────────────────────┬──────────────────────┐││
  │││ ISiteHomeLeftColumn │ ISiteHomeRightColumn │││
  │││                     │┌────────────────────┐│││
  │││                     ││ISiteHomeTabs       ││││
  │││                     │└────────────────────┘│││
  ││└─────────────────────┴──────────────────────┘││
  ││┌────────────────────────────────────────────┐││
  │││ ISiteHomeEpilogue                          │││
  ││└────────────────────────────────────────────┘││
  │└──────────────────────────────────────────────┘│
  │┌─JS───────────────────────────────────────────┐│
  ││ ISiteHomeJS                                  ││
  │└──────────────────────────────────────────────┘│
  └────────────────────────────────────────────────┘

.. [#group] See `the Group Page product 
	    <http://source.iopen.net/groupserver/gs.group.home/summary>`_ 
	    for more information on the layout of the Group page..
