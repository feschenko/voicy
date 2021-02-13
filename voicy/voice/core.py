from string import ascii_uppercase, ascii_letters, digits
from python_rucaptcha import ReCaptchaV2
from pydantic import BaseModel
from base64 import b64decode
from typing import Optional
from ..http import Request
from random import choice


class MaxLengthError(Exception):
    """Throws when text length is more than 4600 characters."""

    pass


class VoiceModelError(Exception):
    """Throws when the user provides non-correct voice arguments."""

    pass


class BadTokenError(Exception):
    """Throws when the client does not accept a token."""

    pass


class File(BaseModel):
    """This object represents an audio file. Contains a path and file format."""

    path: str
    format: str


class Voice:
    def __init__(self, token: str):
        """
        :param token: The token for the client.
        """
        self.request = Request()
        self.token = token

    def tts(
            self,
            text: str,
            voice: dict,
            rate: float = 1,
            pitch: float = 0,
            path: str = "",
            format: str = "wav",
    ) -> File:
        """
        Does a http to the client with the token, that provided in init. After does TTS and returns the path to file.
        :param text: Text with length no more than 4600 characters. Supports multi-language, but with issues.
        :param voice: Dictionary like {"en-US": "en-US-Wavenet-A"}. More about you can read in README.
        :param rate: Speed of voice speaking. By default, is 1.
        :param pitch: Pitch of the voice. By default, is 0.
        :param path: Saving path for the audio file. Empty for saving in the current path.
        :param format: Format for the audio file. By default, is wav.
        :return: File object.
        """
        if len(text) > 4600:
            raise MaxLengthError("Max text length is 4600 characters.")
        response = Request.make(
            "POST",
            "https://cxl-services.appspot.com/proxy",
            params={
                "url": "https://texttospeech.googleapis.com/v1beta1/text:synthesize",
                "token": self.token,
            },
            json={
                "input": {"text": text},
                "voice": {"languageCode": list(voice.items())[0][0], "name": list(voice.items())[0][1]},
                "audioConfig": {
                    "audioEncoding": "LINEAR16",
                    "pitch": pitch,
                    "speakingRate": rate,
                },
            }
        )
        if response.status_code == 200:
            if "audioContent" in response.json():
                filename = "".join(
                    choice(ascii_uppercase + ascii_letters + digits) for _ in range(15)
                )
                path = f"{path}/{filename}.{format}" if path else f"{filename}.{format}"
                file = open(path, "wb")
                file.write(b64decode(response.json()["audioContent"]))
                file.close()
                return File(path=path, format=format)
        elif response.status_code == 400:
            raise VoiceModelError("Could not find the provided voice model. Please watch README.")
        elif response.status_code == 401:
            raise BadTokenError("Bad token. Generate a new one.")


class Token:
    @staticmethod
    def get_token(rucaptcha_key: str) -> Optional[str]:
        """
        Does a http to the client, solve a captcha and return a token.
        :param rucaptcha_key: Rucaptcha API key.
        :return: The token.
        """
        response = Request().make("GET", "https://cloud.google.com/text-to-speech")
        recaptcha_response = ReCaptchaV2.ReCaptchaV2(
            rucaptcha_key=rucaptcha_key
        ).captcha_handler(
            site_key="6LdBnhQUAAAAAMkYSqdAnkafemcA6JtM1N3hlgiL", page_url=response.url
        )
        if recaptcha_response["captchaSolve"]:
            return recaptcha_response["captchaSolve"]
        return None
