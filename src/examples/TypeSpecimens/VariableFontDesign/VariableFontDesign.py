# -----------------------------------------------------------------------------
#     Copyright (c) 2016+ Type Network, www.typenetwork.com, www.pagebot.io
#
#     P A G E B O T
#
#     Licensed under MIT conditions
#     Made for usage in DrawBot, www.drawbot.com
# -----------------------------------------------------------------------------
#
#     AutomaticPageComposition.py
#
#     This script generates an article (in Dutch) of 2009 about the approach to
#     generate automatic layouts, using Style, Galley, Typesetter and Composer classes.
#
from pagebot import getFormattedString, textBoxBaseLines

import pagebot.style
reload(pagebot.style)
from pagebot.style import getRootStyle, LEFT_ALIGN

import pagebot.document 
reload(pagebot.document)
from pagebot.document import Document

import pagebot.page
reload(pagebot.page)
from pagebot.page import Page, Template

import pagebot.composer
reload(pagebot.composer)
from pagebot.composer import Composer

import pagebot.typesetter
reload(pagebot.typesetter)
from pagebot.typesetter import Typesetter

import pagebot.elements
reload(pagebot.elements)
from pagebot.elements import Galley, Rect

import pagebot.fonttoolbox.variationbuilder
reload(pagebot.fonttoolbox.variationbuilder)
from pagebot.fonttoolbox.variationbuilder import generateInstance
    
DEBUG = False

SHOW_GRID = DEBUG
SHOW_GRID_COLUMNS = DEBUG
SHOW_BASELINE_GRID = DEBUG
SHOW_FLOW_CONNECTIONS = DEBUG

EXPORT_PATH = 'export/variableFontDesign.pdf'
  
# Get the default root style and overwrite values for this document.
U = 7
baselineGrid = 2*U
listIndent = 1.5*U

RS = getRootStyle(
    u = U, # Page base unit
    # Basic layout measures altering the default rooT STYLE.
    w = 595, # Om root level the "w" is the page width 210mm, international generic fit.
    h = 11 * 72, # Page height 11", international generic fit.
    ml = 7*U, # Margin left rs.mt = 7*U # Margin top
    baselineGrid = baselineGrid,
    g = U, # Generic gutter.
    # Column width. Uneven means possible split in 5+1+5 or even 2+1+2 +1+ 2+1+2
    # 11 is a the best in that respect for column calculation.
    cw = 11*U, 
    ch = 6*baselineGrid - U, # Approx. square and fitting with baseline.
    listIndent = listIndent, # Indent for bullet lists
    listTabs = [(listIndent, LEFT_ALIGN)], # Match bullet+tab with left indent.
    # Display option during design and testing
    showGrid = SHOW_GRID,
    showGridColumns = SHOW_GRID_COLUMNS,
    showBaselineGrid = SHOW_BASELINE_GRID,
    showFlowConnections = SHOW_FLOW_CONNECTIONS,
    # Text measures
    leading = baselineGrid,
    rLeading = 0,
    fontSize = 9
)
# Tracking presets
H1_TRACK = H2_TRACK = 0.015 # 1/1000 of fontSize, multiplier factor.
H3_TRACK = 0.030 # Tracking as relative factor to font size.
P_TRACK = 0.030

FONT_PATH = '../../../fonts/'

def getFontByLocation(weight, width):
    name = 'PromisePageBot-wght%d-wdth%d' % (weight, width)
    location = dict(wght=weight, wdth=width)
    
    VFONT_PATH = 'PromisePageBot-GX.ttf'
    installFont(FONT_PATH + VFONT_PATH)
    fontName, fontPath = generateInstance(FONT_PATH + VFONT_PATH, 
        location, targetDirectory=FONT_PATH + 'instances')
    return fontName
    
def makeMatrix(rs, page, s, steps):

    x = rs['ml']
    y = rs['mb']
    for weight in range(0, 1000, int(1000/steps)):
        for width in range(0, 1000, int(1000/steps)):
            fontName = getFontByLocation(weight, width)
            fs = FormattedString(s, font=fontName,  fontSize=72, fill=0)
            w, h = fs.size()
            page.text(fs, x+weight/2-w/2, y+width/2)  

# -----------------------------------------------------------------         
def makeSpecimen(rs):
        
    # Template 1
    template1 = Template(rs) # Create template of main size. Front page only.
    # Show grid columns and margins if rootStyle.showGrid or rootStyle.showGridColumns are True
    template1.grid(rs) 
    # Show baseline grid if rs.showBaselineGrid is True
    template1.baselineGrid(rs)
   
    # Create new document with (w,h) and fixed amount of pages.
    # Make number of pages with default document size.
    # Initially make all pages default with template2
    doc = Document(rs, pages=3, template=template1) 

    steps = 4
    makeMatrix(rs, doc[1], 'Ha', steps)
    makeMatrix(rs, doc[2], 'an', steps)
    makeMatrix(rs, doc[3], 'aé', steps)
    return doc
        
d = makeSpecimen(RS)
d.export(EXPORT_PATH) 
