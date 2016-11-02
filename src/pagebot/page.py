# -*- coding: UTF-8 -*-
#-----------------------------------------------------------------------------
#     Copyright (c) 2016+ Type Network, www.typenetwork.com, www.pagebot.io
#     Licensed under MIT conditions
#     Made for usage in Drawbot, www.drawbot.com
#
#     P A G E B O T
#
# -----------------------------------------------------------------------------
#
#     page.py
#

import weakref
import copy
from drawBot import stroke, newPath, drawPath, moveTo, lineTo, strokeWidth, oval, fill, curveTo
from style import NO_COLOR
from pagebot import cr2p, cp2p, setFillColor, setStrokeColor
from elements import Grid, BaselineGrid, Image, TextBox, Text, Rect, Line, Oval

class Page(object):
 
    DEFAULT_STYLE = 'page'

    def __init__(self, parent, w, h, pageNumber=None, template=None):
        self.parent = parent # Resource for self.parent.styles and self.parent.templates dictionaries.
        self.w = w # Page width
        self.h = h # Page height
        self.pageNumber = pageNumber
        self.setTemplate(template) # Create storage of elements and copy template elements.
        
    def __repr__(self):
        return '[%s w:%d h:%d elements:%d elementIds:%s]' % (self.__class__.__name__, self.w, self.h, len(self.elements), self.elementIds.keys())
            
    def setTemplate(self, template):
        u"""Clear the elements from the page and set the template. Copy the elements."""
        self.elements = [] # Sequential drawing order of Element instances.
        # Stored elements by their unique id, so they can be altered later, before rendering starts.
        self.elementIds = {}
        self.placed = {} # Placement by (x,y) key. Value is a list of elements.
        self.template = template # Keep in order to clone pages or if addition info is needed.
        if template is not None:
            # Copy elements from the template and put them in the designated positions.
            for element, (x, y) in template.elements:
                self.place(copy.copy(element), x, y)

    def place(self, e, x, y):
        u"""Place the element on position (x, y). Note that the elements do not know that they
        have a position by themselves. This also allows to place the same element on multiple
        position on the same page or multiple pages (as for template elements)."""
        # Store the element by position. There can be multiple elements on the same position.
        if not (x,y) in self.placed:
            self.placed[(x,y)] = []
        self.placed[(x,y)].append(e)
        # Store the elements for sequential drawing with their (x,y) as elementPos for
        # easy sequential drawing. We need to keep the original order, because of overlapping
        # elements.
        elementPos = (e, (x, y))
        self.elements.append(elementPos)
        # If the element has an eId, then store elementPos by id, for direct retrieval, e.g.
        # for the Composer lookup. Note that since (x, y) is used multiple times, moving
        # elements to other positions on the page, required some bookkeeping.
        if e.eId is not None:
            assert e.eId not in self.elementIds
            self.elementIds[e.eId] = elementPos
            
    def getElementPos(self, eId):
        u"""Answer the (e, (x, y)) element/position. Answer None if the element cannot be found."""
        return self.elementIds.get(eId)

    def getElement(self, eId):
        u"""Answer the page element, if it has a unique element Id."""
        elementPos = self.getElementPos(eId)
        if elementPos is not None:
            return elementPos[0]
        return None

    def findImageElement(self, w, h):
        u"""Find unused image space that closest fits the requested w/h/ratio."""
        for element, (_, _) in self.elements:
            if isinstance(element, Image) and not element.path:
                return element
        return None
                             
    def _get_parent(self):
        return self._parent()    
    def _set_parent(self, parent):
        self._parent = weakref.ref(parent)
    parent = property(_get_parent, _set_parent)
    
    def nextPage(self, nextPage=1, makeNew=True):
        u"""Answer the next page after self in the document."""
        return self.parent.nextPage(self, nextPage, makeNew)

    def getNextFlowBox(self, tb, makeNew=False):
        if tb.nextPage:
            page = self.nextPage(tb.nextPage, makeNew)
            #print 'bbbbbb', tb.eId, tb.nextBox, tb.nextPage
            assert page is not None
            tb = page.getElement(tb.nextBox)
            assert tb is not None and not len(tb)
        else:
            page = self
            #print 'aaaaaaa', tb.eId, tb.nextBox
            tb = self.getElement(tb.nextBox)
            # Make sure that this one is empty, otherwise mistake in template
            assert not len(tb)
        return page, tb
        
    def getStyle(self, name=None):
        u"""Get the named style. Otherwise search for default or root style in parent document."""
        style = None
        if name is None and self.template is not None:
            style = self.template.getStyle()
        if style is None: # No style found, then search in document for named style.
            style = self.parent.getStyle(name)
        if style is None: # No style found, then try default style
            style = self.parent.getStyle(self.DEFAULT_STYLE)
        if style is None:
            style = self.parent.getRootStyle()
        return style
        
    def getStyles(self):
        return self.parent.styles

    def textBox(self, fs, x, y, w, h, eId=None, nextBox=None, nextPage=1, 
            fill=NO_COLOR, stroke=NO_COLOR, strokeWidth=None):
        e = TextBox(fs, w, h, eId, nextBox, nextPage, fill, stroke, strokeWidth)
        self.place(e, x, y) # Append to drawing sequence and store by (x,y) and optional element id.
        return e

    def cTextBox(self, fs, cx, cy, cw, ch, eId=None, nextBox=None, nextPage=1, 
            fill=NO_COLOR, stroke=NO_COLOR, strokeWidth=None):
        x, y, w, h = cr2p(cx, cy, cw, ch, self.getStyle())
        return self.textBox(fs, x, y, w, h, eId, nextBox, nextPage, fill, stroke, strokeWidth)
        
    def text(self, fs, x, y, eId=None, font=None, fontSize=None, fill=NO_COLOR):
        u"""Draw formatted string.
        We don't need w and h here, as it is made by the text and style combinations."""
        e = Text(fs, eId, font, fontSize, fill)
        self.place(e, x, y) # Append to drawing sequence and store by (x,y) and optional element id.
        return e
                
    def cText(self, fs, cx, cy, eId=None, font=None, fontSize=None, fill=NO_COLOR):
        u"""Draw formatted string.
        We don't need w and h here, as it is made by the text and style combinations."""
        x, y = cp2p(cx, cy, self.getStyle())
        return self.text(fs, x, y, eId, font, fontSize, fill)
                
    def rect(self, x, y, w, h, eId=None, fill=0, stroke=None, strokeWidth=None):
        e = Rect(w, h, eId, fill=fill, stroke=stroke, strokeWidth=strokeWidth)
        self.place(e, x, y) # Append to drawing sequence and store by optional element id.
        return e
                
    def cRect(self, cx, cy, cw, ch, eId=None, fill=0, stroke=None, strokeWidth=None):
        x, y, w, h = cr2p(cx, cy, cw, ch, self.getStyle())
        return self.rect(x, y, w, h, eId, fill, stroke, strokeWidth)
                
    def oval(self, x, y, w, h, eId=None, fill=NO_COLOR, stroke=NO_COLOR, strokeWidth=None):
        e = Oval(x, self.h - y, w, h, eId, fill=fill, stroke=stroke)
        self.append(e) # Append to drawing sequence and store by optional element id.
        return e
               
    def line(self, x, y, w, h, eId=None, stroke=None, strokeWidth=None):
        e = Line(x, self.h - y, w, -h, eId, stroke=stroke, strokeWidth=strokeWidth)
        self.append(e) # Append to drawing sequence and store by optional element id.
        return e
                
    def cLine(self, cx, cy, cw, ch, eId=None, stroke=None, strokeWidth=None):
        x, y, w, h = cr2p(cx, cy, cw, ch, self.getStyle())
        e = Line(w, h, eId, stroke=stroke, strokeWidth=strokeWidth)
        self.place(e, x, y) # Append to drawing sequence and store by optional element id.
        return e
                
    def image(self, path, x, y, w=None, h=None, eId=None, s=None, sx=None, sy=None, fill=NO_COLOR, stroke=None, 
            strokeWidth=None, missingImageFill=NO_COLOR, caption=None, hyphenation=True):
        e = Image(path, w, h, eId, s, sx, sy, fill, stroke, strokeWidth, missingImageFill, caption, hyphenation)
        self.place(e, x, y)
        return e
            
    def cImage(self, path, cx, cy, cw=None, ch=None, eId=None, s=None, sx=None, sy=None, fill=NO_COLOR, stroke=None, 
            strokeWidth=None, missingImageFill=NO_COLOR, caption=None, hyphenation=True):
        # Convert the column size into point size, depending on the column settings of the current template,
        # when drawing images "hard-coded" directly on a certain page.
        x, y, w, h = cr2p(cx, cy, cw, ch, self.getStyle())
        return self.image(path, x, y, w, h, eId, s, sx, sy, fill, stroke, strokeWidth, missingImageFill, 
            caption, hyphenation)
            
    def grid(self, x=0, y=0, eId=None):
        e = Grid(eId)
        self.place(e, x, y)
        return e
        
    def baselineGrid(self, x=0, y=0, eId=None):
        e = BaselineGrid(eId)
        self.place(e, x, y)
        return e

    def getFlows(self):
        u"""Answer the set of flow sequences on the page."""
        flows = {} # Key is nextBox of first textBox. Values is list of TextBox instances.
        for element, (x, y) in self.elements:
            if not element.isFlow():
                continue
            # Now we know that this element has a e.nextBox and e.nextPage
            # There should be a flow with that name in our flows yet
            found = False
            for nextId, seq in flows.items():
                if seq[-1].nextBox == element.eId: # Glue to the end of the sequence.
                    seq.append(element)
                    found = True
                elif element.nextBox == seq[0].eId: # Add at the start of the list.
                    seq.insert(0, element)
                    found = True
            if not found: # New entry
                flows[element.next] = [element]
        return flows

    def drawArrow(self, xs, ys, xt, yt, onText=1):
        u"""Draw curved arrow marker between the two points.
        TODO: Add drawing of real arrow-heads, rotated in the right direction."""
        style = self.parent.getRootStyle()
        fms = style.flowMarkerSize
        fmf = style.flowCurvatureFactor
        if onText == 1:
            c = style.flowConnectionStroke2
        else:
            c = style.flowConnectionStroke1
        setStrokeColor(c, style.flowConnectionStrokeWidth)
        setFillColor(style.flowMarkerFill)
        oval(xs - fms, ys - fms, 2 * fms, 2 * fms)
        xm = (xt + xs)/2
        ym = (yt + ys)/2
        xb1 = xm + onText * (yt - ys) * fmf
        yb1 = ym - onText * (xt - xs) * fmf
        xb2 = xm - onText * (yt - ys) * fmf
        yb2 = ym + onText * (xt - xs) * fmf
        setFillColor(None)
        newPath()
        moveTo((xs, ys))
        curveTo((xb1, yb1), (xb2, yb2), (xt, yt))
        drawPath()
        oval(xt - fms, yt - fms, 2 * fms, 2 * fms)

    def drawFlowConnections(self):
        u"""If rootStyle.showFlowConnections is True, then draw the flow connections
        on the page, using their stroke/width settings of the style."""
        style = self.parent.getRootStyle()
        if not style.showFlowConnections:
            return
        for seq in self.getFlows().values():
            # For all the floq sequences found in the page, draw flow arrows
            tbStart, (startX, startY) = self.getElementPos(seq[0].eId)
            for tbTarget in seq[1:]:
                tbTarget, (targetX, targetY) = self.getElementPos(tbTarget.eId)
                self.drawArrow(startX, startY+tbStart.h, startX+tbStart.w, startY, -1)
                self.drawArrow(startX+tbStart.w, startY, targetX, targetY + tbTarget.h, 1)
                tbStart = tbTarget
                startX = targetX
                startY = targetY
            self.drawArrow(startX, startY + tbStart.h, startX + tbStart.w, startY, -1)

    def draw(self):
        for element, (x, y) in self.elements:
            element.draw(self, x, y)
        # Check if we need to draw the flow arrows.
        self.drawFlowConnections()

class Template(Page):
    u"""Template is a special kind of Page class. Possible the draw in 
    the same way. Difference is that templates cannot contain other templates."""
    
    def __init__(self, style):
        self.w = style.w # Page width
        self.h = style.h # Page height
        self.elements = [] # Sequential drawing order of elementPos (e, (x, y)) tuples.
        # Stored elementPos (e, (x, y)) by their unique id, so they can be altered later,
        # before rendering starts.
        self.elementIds = {} # Key is eId.
        self.placed = {} # Placement by (x,y) key. Value is a list of elements.
        self.style = style # In case None, the page should use the document root style.
 
    def getStyle(self, name=None):
        return self.style
            
    def draw(self, page, x, y):
        # Templates are supposed to be copied from by Page, never to be drawing themselves.
        pass 
