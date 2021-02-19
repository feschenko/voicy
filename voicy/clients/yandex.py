from voicy.exceptions import (
    BadLanguageCodeError,
    MaxLengthError,
    VoiceModelError,
)
from string import ascii_uppercase, ascii_letters, digits
from voicy.types import File
from voicy.http import Request
from random import choice
from pydub import AudioSegment
import re
import io


class Yandex:
    def __init__(self):
        self.request = Request()

    def tts(
        self,
        text: str,
        voice: str,
        language_code: str,
        emotion: str = "good",
        rate: float = 1,
        path: str = "",
        format: str = "wav",
    ) -> File:
        """
        Does a request to the client. Returns the File object.
        :param text: Text with length no more than 4600 characters. Supports multi-language, but with issues.
        :param voice: Voice. More about you can read in README.
        :param language_code: String like "en-US". More about you can read in README.
        :param emotion: The emotion of voice. By default, is "good".
        :param rate: Speed of voice speaking. By default, is 1.
        :param path: Saving path for the audio file. Empty for saving in the current path.ы
        :param format: Format for the audio file. By default, is wav.
        :return: File object.
        """
        if len(text) > 5000:
            raise MaxLengthError("Max text length is 5000 characters.")
        response = self.request.make(
            "GET", "https://cloud.yandex.com/services/speechkit"
        )
        csrf = re.findall(
            r"<meta name=\"csrf-token\" content=\"(.*?)\"/>", response.text
        )
        if csrf:
            response = self.request.make(
                "POST",
                "https://cloud.yandex.com/api/speechkit/tts",
                headers={"x-csrf-token": csrf[0]},
                json={
                    "message": text,
                    "language": language_code,
                    "speed": rate,
                    "voice": voice,
                    "emotion": emotion,
                    "format": "oggopus",
                },
            )
            if response.status_code == 200:
                if "error_message" not in response.text:
                    filename = "".join(
                        choice(ascii_uppercase + ascii_letters + digits)
                        for _ in range(15)
                    )
                    path = (
                        f"{path}/{filename}.{format}"
                        if path
                        else f"{filename}.{format}"
                    )
                    AudioSegment.from_file(io.BytesIO(response.content)).export(
                        path, format=format
                    )
                    return File(path=path, format=format)
                if "error_message" in response.text:
                    if "Unsupported language" in response.json()["error_message"]:
                        raise BadLanguageCodeError(
                            "Incorrect language code. Please watch README."
                        )
                    if "Unsupported voice" in response.json()["error_message"]:
                        raise VoiceModelError(
                            "Could not find the provided voice model. Please watch README."
                        )
