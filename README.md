# Voicy
### Free wrapper for cloud.google.com TTS.


# Usage example:
```python3
from voicy import Voice, Token

token = Token.get_token(rucaptcha_key="Key")

voice = Voice(token)

print(
    voice.tts(
        text="Вы используете библиотеку voicy. Поставьте звездочку, "
              "если считаете ее полезной. Автор – Кирилл Фещенко",
        voice="2",
        rate=1.1,
        pitch=0.6,
        format="wav"
    )
)
```
