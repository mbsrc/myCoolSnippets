fileTypeCommentSymbols = {
    'js': '//',
    'py': '#',
    'sh': '#',
    'vim': '#',
    'conf': '#',
    'tmux': '#',
    'snippets': '#',
}

def commentSymbol(fileType):
    if fileType not in fileTypeCommentSymbols: return ""
    return fileTypeCommentSymbols[fileType]


def titlePadding(tabstop):
    return "-" * (65 - len(tabstop))
