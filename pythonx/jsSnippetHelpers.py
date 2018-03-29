specialLibs = {
    'body-parser': 'bodyParser',
    'supertest': 'request',
    'lodash': '_',
    'jsonwebtoken': 'jwt',
    'bcryptjs': 'bcrypt',
    'socket.io': 'socketIO',
    'stellar-sdk': 'StellarSdk',
}

libStrings = {
    'global': "{} = require('{}')",
    'sibling': "{} = require('./{}')",
    'parent': "{} = require('../{}')",
}

def specialRequire(library, relation="global"):
    returnString = ""
    libraryNamePair = (library, library)

    if library in specialLibs:
        libraryNamePair = (specialLibs[library], library)

    return libStrings[relation].format(*libraryNamePair)


def camelCase(s):
    if len(s) < 2: return s

    return s[0].lower() + s[1:]


def titleCamelCase(s):
    if len(s) < 2: return s

    return s[0].upper() + s[1:]

