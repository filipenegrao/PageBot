#!/usr/bin/env python
# -----------------------------------------------------------------------------
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens & Font Bureau
#     www.pagebot.io
#
#     P A G E B O T
#
#     Licensed under MIT conditions
#
#     Supporting usage of DrawBot, www.drawbot.com
# -----------------------------------------------------------------------------
#
#     testBabelStrings.py
#
# Test BabelString both under DrawBotContext and FlatContext
from pagebot.contexts.drawbotcontext import DrawBotContext
from pagebot.contexts.flatcontext import FlatContext

W = H = 800
M = 100

testContexts = (
    (DrawBotContext(), '_export/testDrawBotString.pdf'),
    (FlatContext(), '_export/testFlatString.pdf'),
)
for context, path in testContexts:
    context.newPage(W, H)
    # Create a new BabelString with the DrawBot FormttedString inside.
    style=dict(font='Roboto-Regular', fontSize=48, textFill=(1, 0, 0))
    bs = context.newString('This is a string', style=style)
    # It prints it content.
    print(bs)
    # Adding or appending strings are added to the internal formatted string.
    bs += ' and more'
    print(bs)
    # Draw grid, matching the position of the text.
    context.fill(None)
    context.stroke(0.7)
    context.line((M, 0), (M, H))
    context.line((0, M), (W, M))
    # Usage in DrawBot by addressing the embedded FS for drawing.
    context.text(bs, (M, M))
    context.saveImage(path)
    