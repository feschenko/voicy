class MaxLengthError(Exception):
    """Throws when text length is more than 4600 characters."""

    pass


class VoiceModelError(Exception):
    """Throws when the user provides non-correct voicy arguments."""

    pass


class BadTokenError(Exception):
    """Throws when the client does not accept a token."""

    pass


class BadLanguageCodeError(Exception):
    """Throws when the client does not accept provided language code."""

    pass


class TranslateTTSError(Exception):
    """Throws then the user makes TTS with empty text or provide a wrong language code."""

    pass
