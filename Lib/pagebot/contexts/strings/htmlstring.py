# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens & Font Bureau
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting usage of DrawBot, www.drawbot.com
#     Supporting usage of Flat, https://github.com/xxyxyz/flat
# -----------------------------------------------------------------------------
#
#     htmlstring.py
#
from pagebot.contexts.strings.babelstring import BabelString
from pagebot.style import css, LEFT

class HtmlString(BabelString):

    BABEL_STRING_TYPE = 'html'

    u"""HtmlString is a wrapper around an HTML tagged string."""
    def __init__(self, s, context, style=None):
        self.context = context # Store the context, in case we need it.
        self.s = s # Enclose the Flat string
        self.style = style or {}

    def _get_font(self):
        u"""Answer the current state of fontName."""
        return self.style.get('font')
    def _set_font(self, fontName):
        if fontName is not None:
            self.context.font(fontName)
        self.style['font'] = fontName
    font = property(_get_font, _set_font)

    def _get_fontSize(self):
        u"""Answer the current state of the fontSize."""
        return self.style.get('fontSize')
    def _set_fontSize(self, fontSize):
        if fontSize is not None:
            self.context.font(fontSize)
        self.style['fontSize'] = fontSize
    fontSize = property(_get_fontSize, _set_fontSize)
       
    def _get_s(self):
        u"""Answer the embedded HTML string by property, to enforce checking type of the string."""
        return self._s
    def _set_s(self, html):
        assert isinstance(html, basestring)
        self._s = html
    s = property(_get_s, _set_s)
    
    def asText(self):
        return self.s # TODO: Use re to find non-tagged text to return.

    def textSize(self, w):
        u"""Answer the (w, h) size for a given width, with the current text.
        For html this probably won't be an accurate guess. Let's think about something else."""
        return len(self.s)*10, 12

    def textOverflow(self, w, h, align=LEFT):
        u"""How to decide if there is HTML text overflow? Useful to do?"""
        # TODO: Some stuff needs to get here.
        return ''

    @classmethod
    def newString(cls, s, context, e=None, style=None, w=None, h=None, fontSize=None, styleName=None, 
            pixelFit=None, tagName=None):
        u"""Answer a FlatString instance from valid attributes in *style*. Set all values after testing
        their existence, so they can inherit from previous style formats.
        If target width *w* or height *h* is defined, then *fontSize* is scaled to make the string fit *w* or *h*."""

        sUpperCase = css('uppercase', e, style)
        sLowercase = css('lowercase', e, style)
        sCapitalized = css('capitalized', e, style)
        if sUpperCase:
            s = s.upper()
        elif sLowercase:
            s = s.lower()
        elif sCapitalized:
            s = s.capitalize()

        return cls(s, context)


if __name__ == '__main__':
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])

