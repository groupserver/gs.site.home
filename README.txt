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

``ISiteHomeMain``:
  The main column that is used for the most important data::

    <browser:viewlet
      name="gs-site-welcome"
      for="Products.GSContent.interfaces.IGSSiteFolder"
      manager="gs.site.home.interfaces.ISiteHomeMain"
      class=".box.WelcomeBox"
      template="browser/templates/box.pt"
      weight="10"
      permission="zope2.View" />

``ISiteHomeSecondary``:
  The right column, which is normally used for minor information::

    <browser:viewlet 
      name="gs-site-about-home"
      for="Products.GSContent.interfaces.IGSSiteFolder"
      manager="gs.site.home.interfaces.ISiteHomeSecondary"
      template="browser/templates/about.pt"
      class="gs.viewlet.SiteViewlet"
      permission="zope2.View"
      weight="10"
      title="About" />


``ISiteHomeEpilogue``:
  Unimportant information that appears at the bottom of the page.

There are two viewlet managers that are not visible. One for the metadata
(``ISiteHomeMetadata``) and one for some JavaScript (``ISiteHomeJS``)::

  <browser:viewlet 
    name="gs-site-about-home-js"
    for="Products.GSContent.interfaces.IGSSiteFolder"
    manager="gs.site.home.interfaces.ISiteHomeJS"
    template="browser/templates/about-js.pt"
    class="gs.viewlet.SiteViewlet"
    permission="zope2.View"
    weight="10"
    title="About Script" />


The layout of the seven viewlet managers is as follows::

  ┌─Page───────────────────────────────────┐
  │┌─Metadata─────────────────────────────┐│
  ││ ISiteHomeMetadata                    ││
  │└──────────────────────────────────────┘│
  │┌─Body─────────────────────────────────┐│
  ││┌────────────────────────────────────┐││
  │││ ISiteHomeIntroduction              │││
  ││└────────────────────────────────────┘││
  ││┌───────────────┬────────────────────┐││
  │││ ISiteHomeMain │ ISiteHomeSecondary │││
  ││└───────────────┴────────────────────┘││
  ││┌────────────────────────────────────┐││
  │││ ISiteHomeEpilogue                  │││
  ││└────────────────────────────────────┘││
  │└──────────────────────────────────────┘│
  │┌─JS───────────────────────────────────┐│
  ││ ISiteHomeJS                          ││
  │└──────────────────────────────────────┘│
  └────────────────────────────────────────┘

.. [#group] See `the Group Page product 
            <http://source.iopen.net/groupserver/gs.group.home/summary>`_ 
            for more information on the layout of the Group page..
