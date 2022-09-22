import unidecode

class UnicodeDecodeError(Exception):
    pass

def u2asc(input):
    """
    Converts/transliterates unicode characters to ASCII, using the unidecode package.
    Functionality is similar to the legacy code in adspy.Unicode, but may treat some characters differently
    (e.g. umlauts). Standard unidecode package only handles Latin-based characters.
    :param input: string to be transliterated. Can be either unicode or encoded in utf-8
    :return output: transliterated string, in either unicode or encoded (to match input)
    """

    # TODO If used on anything but author names, add special handling for math symbols and other special chars
    if sys.version_info < (3,):
        test_type = unicode
    else:
        test_type = str

    if not isinstance(input, test_type):
        try:
            input = input.decode('utf-8')
        except UnicodeDecodeError:
            raise UnicodeHandlerError('Input must be either unicode or encoded in utf8.')

    try:
        output = unidecode.unidecode(input)
    except UnicodeDecodeError:
        raise UnicodeHandlerError('Transliteration failed, check input.')

    if not isinstance(input, test_type):
        output = output.encode('utf-8')

    return output
