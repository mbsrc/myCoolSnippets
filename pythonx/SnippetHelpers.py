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

def commentSymbol(snip):
    if snip.ft not in fileTypeCommentSymbols: return ""
    return fileTypeCommentSymbols[snip.ft]


def titlePadding(tabstop, snip, foldType=None):
    paddingSize = 66
    commentLen = len(commentSymbol(snip))
    if foldType == 'm': paddingSize = 63

    snip.rv = "-" * (paddingSize - len(tabstop) - commentLen)
