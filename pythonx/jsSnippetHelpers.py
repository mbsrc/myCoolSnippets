import re

specialImports = {
    'lodash':                   '_',
    'bcryptjs':                 'bcrypt',
    'supertest':                'request',
    'socket.io':                'socketIO',
    'stellar-sdk':              'StellarSdk',
    'jsonwebtoken':             'jwt',
    'express-graphql':          'expressGraphQL',
    'react-stripe-checkout':    'StripeCheckout',
    'passport-google-oauth20':  'GooglePassportStrategy',
    'styled-components':  'styled',
}


def parseLib(snip, match):
    library = match.group(1)

    if library in specialImports:
        snip.rv = specialImports[library]
    elif '-' in library:
        snip.rv = re.sub('-.',lambda x: x.group()[1].upper(), library)
    else:
        snip.rv = library


def camelCase(s):
    if len(s) < 2: return s

    return s[0].lower() + s[1:]


def titleCamelCase(s):
    if len(s) < 2: return s

    return s[0].upper() + s[1:]

