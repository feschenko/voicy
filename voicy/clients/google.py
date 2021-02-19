from voicy.exceptions import (
    BadLanguageCodeError,
    BadTokenError,
    TranslateTTSError,
    MaxLengthError,
    VoiceModelError,
)
from string import ascii_uppercase, ascii_letters, digits
from python_rucaptcha import ReCaptchaV2
from base64 import b64decode, b64encode
from voicy.types import File, Transcript
from pydub.utils import mediainfo
from typing import Optional
from voicy.http import Request
from random import choice


class Google:
    def __init__(self, token: Optional[str] = None):
        """
        :param token: The token for the client. Provide it if you need to use TTS or SST.
        """
        self.request = Request()
        self.token = token

    def tts(
        self,
        text: str,
        voice: dict,
        rate: float = 1,
        pitch: float = 0,
        ssml: bool = False,
        path: str = "",
        format: str = "wav",
    ) -> File:
        """
        Does a request to the client with the token, that provided in init. Returns the File object.
        :param text: Text with length no more than 4600 characters. Supports multi-language, but with issues.
        :param voice: Dictionary like {"en-US": "en-US-Wavenet-A"}. More about you can read in README.
        :param rate: Speed of voice speaking. By default, is 1.
        :param pitch: Pitch of the voice. By default, is 0.
        :param ssml: Google SSML support.
        :param path: Saving path for the audio file. Empty for saving in the current path.
        :param format: Format for the audio file. By default, is wav.
        :return: File object.
        """
        if len(text) > 4600:
            raise MaxLengthError("Max text length is 4600 characters.")
        if not self.token:
            raise BadTokenError("The token is not provided.")
        response = Request.make(
            "POST",
            "https://cxl-services.appspot.com/proxy",
            params={
                "url": "https://texttospeech.googleapis.com/v1beta1/text:synthesize",
                "token": self.token,
            },
            json={
                "input": {"ssml" if ssml else "text": text},
                "voice": {
                    "languageCode": list(voice.items())[0][0],
                    "name": list(voice.items())[0][1],
                },
                "audioConfig": {
                    "audioEncoding": "LINEAR16",
                    "pitch": pitch,
                    "speakingRate": rate,
                },
            },
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
            raise VoiceModelError(
                "Could not find the provided voice model. Please watch README."
            )
        elif response.status_code == 401:
            raise BadTokenError("Bad token. Generate a new one.")

    def translate_tts(
        self,
        text: str,
        language_code: str,
        path: str = "",
        format: str = "wav",
    ) -> File:
        """
        Does a request to the translate client without a token. Returns the File object.
        :param text: Text with length no more than 4600 characters. Supports multi-language, but with issues.
        :param language_code: String like "en-US". More about you can read in README.
        :param path: Saving path for the audio file. Empty for saving in the current path.
        :param format: Format for the audio file. By default, is wav.
        :return: File object.
        """
        if len(text) > 200:
            raise MaxLengthError("Max text length is 200 characters.")
        response = self.request.make(
            "GET",
            "https://translate.google.com/translate_tts",
            params={"ie": "utf-8", "tl": language_code, "client": "tw-ob", "q": text},
        )
        if response.status_code == 200:
            filename = "".join(
                choice(ascii_uppercase + ascii_letters + digits) for _ in range(15)
            )
            path = f"{path}/{filename}.{format}" if path else f"{filename}.{format}"
            file = open(path, "wb")
            file.write(response.content)
            file.close()
            return File(path=path, format=format)
        elif response.status_code == 404:
            raise TranslateTTSError("Text is empty or provided a wrong language code.")

    def stt(self, file: str, language_code: str) -> Optional[Transcript]:
        """
        Does a request to the client with the token, that provided in init. Returns the Transcript object.
        :param file: Full path for an audio file.
        :param language_code: String like "en-US". More about you can read in README.
        :return: Transcript object.
        """
        if not self.token:
            raise BadTokenError("The token is not provided.")
        response = self.request.make(
            "POST",
            "https://cxl-services.appspot.com/proxy",
            params={
                "url": "https://speech.googleapis.com/v1p1beta1/speech:recognize",
                "token": self.token,
            },
            json={
                "audio": {
                    "content": b64encode(open(file, "rb").read()).decode("utf-8")
                },
                "config": {
                    "enableAutomaticPunctuation": "true",
                    "encoding": "LINEAR16",
                    "languageCode": language_code,
                    "model": "default",
                    "sampleRateHertz": mediainfo(file)["sample_rate"],
                },
            },
        )
        if response.status_code == 200:
            if "results" in response.json():
                return Transcript(
                    text=response.json()["results"][0]["alternatives"][0]["transcript"],
                    confidence=response.json()["results"][0]["alternatives"][0][
                        "confidence"
                    ],
                    file=File(path=file, format=file.split(".")[-1]),
                )
            return None
        elif response.status_code == 400:
            raise BadLanguageCodeError("Incorrect language code. Please watch README.")
        elif response.status_code == 401:
            raise BadTokenError("Bad token. Generate a new one.")


class GoogleToken:
    @staticmethod
    def get_token(rucaptcha_key: str) -> Optional[str]:
        """
        Does a request to the client, solve a captcha and return a token.
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
