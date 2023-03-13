#!/usr/bin/env python
# Copyright BSD-3 evdcush
'''
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Fart
====
Make text banners to visually divide segments in your code.

How can you fart on your code? Say you have two main parts in
your script: preprocess and train. You can make two farts to divide the
sections via:

$ fart PRE-PROCESS

#=============================================================================#
#                                 PRE-PROCESS                                 #
#=============================================================================#


Maybe you'd like to pad the inside of the  <cap> chars (``#`` being default)
with spaces so that your auto-formatter doesn't mess with your farting.
To do so, specify the ``-p --pad-caps``, eg:

$ fart -p TRAINING

# =========================================================================== #
#                                   TRAINING                                  #
# =========================================================================== #


You can also fart with one line via the ``-o --oneline`` flag.
I also like thinner lines for these farts, so let's also specify the line char
via ``-l --line`` option, eg:

$ fart -op -l '-' Pathing Utils

# -----------------------------  Pathing Utils  ----------------------------- #


Or you have a new, totally different section in code ``export``.
Here you might want to use the figlet-based fart, eg:

$ fart -f ansi_regular Export

#=============================================================================#
#                                                                             #
#              ███████ ██   ██ ██████   ██████  ██████  ████████              #
#              ██       ██ ██  ██   ██ ██    ██ ██   ██    ██                 #
#              █████     ███   ██████  ██    ██ ██████     ██                 #
#              ██       ██ ██  ██      ██    ██ ██   ██    ██                 #
#              ███████ ██   ██ ██       ██████  ██   ██    ██                 #
#                                                                             #
#=============================================================================#


Maybe you want your farts to be ascii only, and also want a font that supports
mixed-case and more chars.

$ fart -f roman Export!

#=============================================================================#
#                                                                             #
#     oooooooooooo                                               .   .o.      #
#     `888'     `8                                             .o8   888      #
#      888         oooo    ooo oo.ooooo.   .ooooo.  oooo d8b .o888oo 888      #
#      888oooo8     `88b..8P'   888' `88b d88' `88b `888""8P   888   Y8P      #
#      888    "       Y888'     888   888 888   888  888       888   `8'      #
#      888       o  .o8"'88b    888   888 888   888  888       888 . .o.      #
#     o888ooooood8 o88'   888o  888bod8P' `Y8bod8P' d888b      "888" Y8P      #
#                               888                                           #
#                              o888o                                          #
#                                                                             #
#=============================================================================#

Serifs aren't your thing?
And you want you want padding spaces after ``--cap char`` (default ``#``)
so code-formatting doesn't complain about your farting?

$ fart -f colossal -p Export!

# =========================================================================== #
#                                                                             #
#          8888888888                                    888    888           #
#          888                                           888    888           #
#          888                                           888    888           #
#          8888888    888  888 88888b.   .d88b.  888d888 888888 888           #
#          888        `Y8bd8P' 888 "88b d88""88b 888P"   888    888           #
#          888          X88K   888  888 888  888 888     888    Y8P           #
#          888        .d8""8b. 888 d88P Y88..88P 888     Y88b.   "            #
#          8888888888 888  888 88888P"   "Y88P"  888      "Y888 888           #
#                              888                                            #
#                              888                                            #
#                              888                                            #
#                                                                             #
# =========================================================================== #

Fart now and see the difference!

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

'''

import argparse
import glob
import importlib
import os
import sys

import clipper


# Pathing
# =======
# Get path to font directory.
SRC_DIR = os.path.dirname(__file__)
FONTS_DIR = SRC_DIR + '/fonts'

# Fonts.
font_fnames = glob.glob(FONTS_DIR + '/[!_]*.py')  # exclude dunders (__init__)
get_font_name = lambda fname: os.path.splitext(os.path.basename(fname))[0]
FONT_NAMES = [get_font_name(font_fname) for font_fname in font_fnames]


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


def maybe_pad_text(text: str, pad=False):
    pad_char = '' if not pad else ' '
    return pad_char + text + pad_char


def box_text(text, cap=CAP, line_char=LINE, width=WIDTH,
        oneline=False, pad=False):
    """ Encapsulates text in a "box" of width, with cap and lines
    #===========#
    #  Example  #
    #===========#

    Currently, only text that can fit on single line is supported

    Parameters
    ==========
    text : str
        text to be encapsulated
    cap : str
        char that starts and ends line (typically commenting char, like '#')
    line_char : str
        char that makes the lines of box (eg '-', '=')
    width : int
        max width of box
    oneline : bool
        whether to print text in a single-line or within a box
    pad : bool
        whether to pad inner-side of caps with a single space (width inclusive)

    Returns
    =======
    text_box : str
        text formatted into a "box"
    """
    #=== Calculate width
    #   width - 2 - (2 * pad) :
    #   (max_line_len) - (space from two cap chars) - (space from padding)
    w = width - 2 - (2 * pad)

    #=== Check valid width
    # Text is additionally padded by two spaces so that text is sufficiently
    # distinct from any cap (or line, if `oneline`) chars, eg:
    #   OK: '#  Hello!  #'
    #   NO: '#Hello!#'
    text_len = len(text)
    assert text_len <= (w - 4), \
        f"Formatted text length exceeds max width! {text_len} > {w - 4}"

    #=== Format main text
    pre_fill_text = f"  {text}  "
    fill_char = ' ' if not oneline else line_char
    fill_width = w
    fill_text = pre_fill_text.center(fill_width, fill_char)
    padded_text = maybe_pad_text(fill_text, pad)
    capped_text = cap_text(padded_text, cap)

    if oneline:
        return capped_text

    #=== Format lines of box
    line = line_char * w
    line = maybe_pad_text(line, pad)
    capped_line = cap_text(line, cap)
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


def build_fart_from_font(text_to_fart: str, font: dict[str, list[str]]) -> str:
    """ This function gets the corresponding figlet font subsets for each
    char in the text string and splices them into a string.

    In Fart, Figlet fonts are represented by dictionaries that map characters
    (``str``) to a list of strings that can be described as top-to-bottom
    slice or row of a rendered font character. Joined together, they will
    render a font character.

    Consider the following example, the letter ``'A'`` in the ``georgia11``
    font dict:

    >>> font['A']
    ['              ',
     '              ',
     '      db      ',
     '     ;MM:     ',
     '    ,V^MM.    ',
     '   ,M  `MM    ',
     '   AbmmmqMA   ',
     "  A'     VML  ",
     '.AMA.   .AMMA.',
     '              ',
     '              ']

    It is pretty-printed here to make the structure and representation of
    fonts clearer.
    We can see here that if we simply printed the join on this list, we'd get
    this font's ``A`` printed cleanly:

    >>> print('\n'.join(font['A']))


          db
         ;MM:
        ,V^MM.
       ,M  `MM
       AbmmmqMA
      A'     VML
    .AMA.   .AMMA.


    (Note, the whitespace and padding is not represented)

    ----

    So, the way we convert a string of chars from the text into a fart
    from the font is by splicing the rows of each string's char set from the
    font dict.
    """
    # TODO: this function is currently only used for the font sample feature,
    #       yet this logic is redundantly performed in the ``render_fart``
    #       function.
    spliced = ''

    # Join chars row-wise
    joined = zip(*[font[c] for c in text])
    for c in joined:
        txt = ''.join(c)
        if txt.replace(' ', '') == '': continue  # don't add blank lines
        spliced += txt + '\n'
    return spliced


def render_fart(text: str, font: dict[str, list[str]], cap=CAP, line=LINE, width=WIDTH, pad=False):
    """ Render the fart text with the given font

    Primary farting function. This func requires the name of the
    figlet font (as the font arg).

    Parameters
    ==========
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
    pad : bool
        whether to pad inside of caps

    Returns
    =======
    fart : str
        rendered fart
    """
    mostly_space = False  # whether topmost line contains mostly space
    fart = ''
    line_width = width if not pad else width - 2

    #=== Join chars row-wise
    joined = zip(*[font[c] for c in text])
    for i, char_tups in enumerate(joined):
        txt = ''.join(char_tups)
        txt_len = len(txt) + 4  # extra 4 widths from left & right caps
        line_width = max(line_width, txt_len)

        # Don't render blank lines
        if txt.replace(' ', '') == '': continue

        # Check if first line mostly empty
        if i == 0 and '_' in txt:
            mostly_space = True

        # Add prepend chars (commenting chars)
        filled_txt = txt.center(line_width - 2)
        padded_txt = maybe_pad_text(filled_txt, pad)
        fart += cap_text(padded_txt, cap)

    #=== Make box
    # Box lines
    edge_line = maybe_pad_text(line * (line_width - 2), pad)
    padding_line = maybe_pad_text(' ' * (line_width - 2), pad)
    capped_edge_line    = cap_text(edge_line, cap)
    capped_padding_line = cap_text(padding_line, cap)

    # Whitespace above and below figlet font rendering
    top = capped_edge_line
    if not mostly_space:
        top += capped_padding_line
    bot = capped_padding_line + capped_edge_line

    # Insert text
    fart = top + fart + bot
    return fart


def fart(text, font_name=None, cap=CAP, line=LINE,
        copy=True, oneline=False, pad=False):
    """ Interface for farting. Gets fart, prints, and copies it to clip.

    Params
    ------
    text : str
        text to be farted
    font_name : str
        figlet font name
    cap : str
        <cap>characters at the ends of a line of text<cap>
    line : str
        line char, eg '=' : #=====================#
    copy : bool
        whether to copy the fart to the clipboard
    oneline : bool
        whether to fart in a single line
    pad : bool
        whether to pad inner cap chars with a single space
    """
    #=== fart box
    if font_name is None:
        assert len(text) < WIDTH - 5  # must fit in box
        fart = box_text(text, cap, line, oneline=oneline, pad=pad)

    #=== font (figlet) fart
    else:
        assert font_name is not None
        assert len(text) < 25 # this thresholding and the magic number is hacky
        font = load_font(font_name)
        fart = render_fart(text, font, cap, line, pad=pad)

    #=== Print 'n copy
    print('\n' + fart + '\n')
    if copy:
        clipper.copy(fart)


def sample_farts(sample='Sample'):
    """ Print sample of all fart fonts """
    for fname in FONT_NAMES:
        font   = load_font(fname)
        farted = build_fart_from_font(sample, font)
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
    cd1 = '/'.join(os.path.realpath(__file__).split('/')[:-1])
    curdir = os.path.realpath(__file__)

    #=== Make CLI
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    arg = parser.add_argument

    # NB: Text is actually a required arg (so more like nargs='+'), but
    #     it is set to '*' for the sole purpose of permitting the user to
    #     view the figlet font samples, eg `fart -s`.
    arg('text', nargs='*', type=str, help='Text to fart')
    arg('-f', '--font', type=str, choices=FONT_NAMES,
        help='Name of the Figlet font used for fart')

    arg('-n', '--no-copy', action='store_true',
        help="Don't copy fart to clipboard")

    arg('-s', '--sample', action='store_true',
        help="Print text samples of all figlet fonts")

    arg('-c', '--cap', default=CAP, type=str,
        help="<cap>character that is appended to ends of text lines<cap>")

    arg('-l', '--line', default=LINE, type=str,
        help="Character used to make lines, eg '~': #~~~~~~~~#")

    arg('-o', '--oneline', action='store_true',
        help="Fart text as one line, instead of in the default 3-line 'box'")

    arg('-p', '--pad-caps', action='store_true',
        help="Optionally pad inner side of caps with a space, eg: `# ==== #`")


    # Parse args.
    args = parser.parse_args()

    # Print figlet font samples if specified.
    # This conditional is placed prior to the required 'text' arg check
    # for end-user convenience.
    if args.sample:
        sample_farts('Sample')
        sys.exit(0)

    # Check if user provided text.
    # NB: charset depends on the figlet font.
    if len(args.text) == 0:
        print("Nothing to fart! Please provide some text.")
        sys.exit(1)

    text = ' '.join(args.text)

    # Process format options.
    font = args.font
    copy = not args.no_copy
    oneline = args.oneline
    pad = args.pad_caps

    cap  = args.cap
    assert len(cap) == 1, \
        "Only single, non-whitespace characters are allowed for cap!"

    line = args.line
    assert len(line) == 1, \
        "Only single, non-whitespace characters are allowed for line!"

    # Let 'er rip.
    fart(text, font, cap, line, copy, oneline, pad)
    sys.exit(0)

if __name__ == '__main__':
    main()
