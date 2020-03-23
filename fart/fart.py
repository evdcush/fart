#!/usr/bin/env python
"""
Fart
"""
# @TODO:
#     write a proper __doc__, and figure out that dang ArgumentParser
#     printing func (it doesn't print newlines)

import os
import sys
import glob
import argparse
import importlib

import pyperclip


# Pathing
# =======
# dir paths
SRC_DIR   = '/'.join(os.path.realpath(__file__).split('/')[:-1])
FONTS_DIR = SRC_DIR + '/fonts'

# fonts
font_fnames = glob.glob(FONTS_DIR + '/[!_]*.py')  # exclude dunders (__init__)
FONT_NAMES  = [fnt.split('/')[-1].split('.')[0] for fnt in font_fnames]


# Default vars
# ============
CAP   = '#'
LINE  = '='
WIDTH = 79  # by PEP8, currently fixed


#=============================================================================#
#                                  formatting                                 #
#=============================================================================#

def cap_text(text, cap=CAP):
    """ Adds a capping char to either end of a string
    NB: also adds newline to right end of line
      eg:
    >>> cap_text('hello world', '$')
    '$hello world$\n'
    """
    capped = cap + text + cap + '\n'
    return capped


def box_text(text, cap=CAP, line_char=LINE, width=WIDTH):
    """ Encapsulates text in a "box" of width, with cap and lines
    #===========#
    #  Example  #
    #===========#

    Currently, only text that can fit on single line is supported

    Params
    ------
    text : str
        text to be encapsulated
    cap : str
        char that starts and ends line (typically commenting char, like '#')
    line_char : str
        char that makes the lines of box (eg '-', '=')
    width : int
        max width of box

    Returns
    -------
    text_box : str
        text formatted into a "box"
    """
    #=== Check args
    w = width - 2  # two additional spaces req'd for comment chars
    # @TODO: allow for multi-line text boxes
    assert len(text) <= (w - 2) # 4-spaces total for padding text

    #=== Format lines
    line = line_char * w
    capped_line = cap_text(line, cap)

    #=== Format main text
    padded_text = text.center(w)
    capped_text = cap_text(padded_text, cap)

    #=== Make box
    text_box = capped_line + capped_text + capped_line
    return text_box


#=============================================================================#
#                              figlet-based farts                             #
#=============================================================================#

def load_font(fname):
    """ Load a ascii-art font from a py file """
    # Check font exists
    assert fname in FONT_NAMES
    assert os.path.exists(FONTS_DIR + '/' + fname + '.py')

    # Load
    font = importlib.import_module('fonts.' + fname).font
    return font


def splice_chars(text, font):
    """ combine text character lists (CURRENTLY UNUSED) """
    spliced = ''

    # Join chars row-wise
    joined = zip(*[font[c] for c in text])
    for c in joined:
        txt = ''.join(c)
        if txt.replace(' ', '') == '': continue  # don't add blank lines
        spliced += txt + '\n'
    return spliced


def render_fart(text, font, cap=CAP, line=LINE, width=WIDTH):
    """ Render the fart text with the given font

    Primary farting function. This func requires the name of the
    figlet font (as the font arg).

    Params
    ------
    text : str
        text to be farted
    font : dict<list<str>>
        figlet font dict, mapping str chars, eg 'A', '3', to ascii art strings
    cap : str
        # characters at the ends of a line of text #
    line : str
        line char, eg '=' : #=====================#
    width : int
        maximum text line width

    Returns
    -------
    fart : str
        rendered fart
    """
    mostly_space = False  # whether topmost line contains mostly space
    fart = ''
    W = width

    #=== Join chars row-wise
    joined = zip(*[font[c] for c in text])
    for i, char_tups in enumerate(joined):
        txt = ''.join(char_tups)
        txt_len = len(txt) + 4  # extra 4 widths from left & right caps
        W = max(W, txt_len)

        # Don't render blank lines
        if txt.replace(' ', '') == '': continue

        # Check if first line mostly empty
        if i == 0 and '_' in txt:
            mostly_space = True

        # Add prepend chars (commenting chars)
        fart += cap_text(txt.center(W - 2), cap)

    #=== Make box
    # Box lines
    edge = cap_text(line * (W - 2), cap)
    pad  = cap_text(' ' * (W - 2), cap)

    # padding
    top = edge
    if not mostly_space:
        top += pad
    bot = pad + edge

    # Insert text
    fart = top + fart + bot
    return fart


#=============================================================================#
#                                 driver funcs                                #
#=============================================================================#

def fart(text, font_name=None, cap=CAP, line=LINE, copy=True):
    """ Interface for farting. Gets fart, prints, and copies it to clip.

    Params
    ------
    text : str
        text to be farted
    font_name : str
        figlet font name
    cap : str
        # characters at the ends of a line of text #
    line : str
        line char, eg '=' : #=====================#
    copy : bool
        whether to copy the fart to the clipboard

    """
    #=== fart box
    if font_name is None:
        assert len(text) < WIDTH - 5  # must fit in box
        fart = box_text(text, cap, line)

    #=== farty fart
    else:
        assert font_name is not None
        assert len(text) < 25  # @TODO: two-line farts; this is ugly
        font = load_font(font_name)
        fart = render_fart(text, font, cap, line)

    #=== Print 'n copy
    print('\n' + fart + '\n')
    if copy:
        #pyperclip.copy(fart)
        pass


def sample_farts(sample='Sample'):
    """ Print sample of all fart fonts """
    for fname in FONT_NAMES:
        font   = load_font(fname)
        farted = splice_chars(sample, font)
        keys = list(sorted(font.keys()))
        keys.remove('name')
        keys = ''.join(keys)

        # Demo text
        pad  = ' ' * WIDTH + '\n'
        line = '-' * WIDTH + '\n'
        sample_fart = farted + pad + fname + '\n' + keys + '\n\n' + line
        print(sample_fart)


#=============================================================================#
#                                   __main__                                  #
#=============================================================================#

def main():
    #=== Make CLI
    parser = argparse.ArgumentParser(description='Fart on your docs')
    arg = parser.add_argument
    arg('text', nargs='*', type=str, help='text to fart')
    arg('-f', '--font', default=None, type=str, choices=FONT_NAMES,
        help='name of the figlet font used for fart')

    arg('-n', '--no_copy', action='store_true',
        help='don\'t copy fart to clipboard')

    arg('-s', '--sample', action='store_true',
        help='print sample of all figlet fonts')

    arg('-c', '--cap', default=CAP, type=str,
        help='<cap> character that is appended to ends of text lines <cap> ')

    arg('-l', '--line', default=LINE, type=str,
        help='character that makes lines, eg \'~\': #~~~~~~~~#')

    #=== Parse args
    args = parser.parse_args()

    # sample
    sample = args.sample
    if sample:
        sample_farts('Sample')
        return 0

    # primary args
    text = ' '.join(args.text)
    font_name = args.font
    cap  = args.cap
    line = args.line
    copy = not args.no_copy

    #=== Fart
    fart(text, font_name, cap, line, copy)
    return 0


if __name__ == '__main__':
    ret = main()




