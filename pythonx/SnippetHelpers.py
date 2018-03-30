fileTypeCommentSymbols = {
    'js': '//',
    'py': '#',
    'sh': '#',
    'vim': '"',
    'conf': '#',
    'tmux': '#',
    'snippets': '#',
    'gitconfig': '#',
}

def commentSymbol(fileType):
    if fileType not in fileTypeCommentSymbols: return ""
    return fileTypeCommentSymbols[fileType]


def titlePadding(tabstop, foldType=None):
    paddingSize = 65

    if foldType == 'm': paddingSize = 62

    return "-" * (paddingSize - len(tabstop))
