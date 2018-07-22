PADDING_SIZE = 54

fileTypeCommentSymbols = {
    'javascript': '//',
    'javascript.jsx': '//',
    'jsx': '//',
    'py': '#',
    'sh': '#',
    'vim': '"',
    'zsh': '#',
    'conf': '#',
    'tmux': '#',
    'snippets': '#',
    'gitconfig': '#',
}

def upperFirstLetter(s):
    # Prevent string indexing errors.
    if len(s) < 2: return s
    return s[0].upper() + s[1:]

def capFirstLetter(words):
    return ' '.join(upperFirstLetter(word) for word in words.split(' '))


def commentSymbol(snip):
    if snip.ft not in fileTypeCommentSymbols: return ""
    return fileTypeCommentSymbols[snip.ft]


def titlePadding(tabstop, snip, foldType=None):
    paddingSize = PADDING_SIZE
    commentLen = len(commentSymbol(snip))
    if foldType == 'm': paddingSize = PADDING_SIZE - 3

    snip.rv = "-" * (paddingSize - len(tabstop) - commentLen)
