Introduction
============

This egg provides the core support for the site homepage, or *the* 
homepage as it should be known. Most of what it provides is an single
page with some viewlet managers. These are filled by other eggs.

Structure
=========

There are four sections on the homepage, each provided by a different 
content provider. Finally there is a space for some JavaScript::

  ┌─Body─────────────────────────────────────────┐
  │┌────────────────────────────────────────────┐│
  ││ Introduction                               ││
  ││ ISiteHomeIntroduction                      ││
  │└────────────────────────────────────────────┘│
  │┌─────────────────────┬──────────────────────┐│
  ││ Left column         │ Right column         ││
  ││ ISiteHomeLeftColumn │ ISiteHomeRightColumn ││
  │└─────────────────────┴──────────────────────┘│
  │┌────────────────────────────────────────────┐│
  ││ Epilogue                                   ││
  ││ ISiteHomeEpilogue                          ││
  │└────────────────────────────────────────────┘│
  └──────────────────────────────────────────────┘
  ┌─JS───────────────────────────────────────────┐
  │ ISiteHomeJS                                  │
  └──────────────────────────────────────────────┘

