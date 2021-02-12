<h1>Voicy</h1>
<h3>Free wrapper for cloud.google.com TTS.</h3>


<p>For a request to the client need to provide a token. You can easily get it using Token object, or in a browser by yourself.</p>
<p>Both options are described below:</p>

<details>
  <summary>Automated option</summary>
    <ol>
        <li>By first, you need to get API token in <a href="http://rucaptcha.com/">rucaptcha</a>.</li>
        <li>
            After that import a Token object from voicy:
            <br>
            <code>from voicy import Token</code>
        </li>
        <li>
            Then provide the API key to the get_token function:
            <br>
            <code>Token.get_token(rucaptcha_key="Token, that you got in the rucaptcha account.")</code>
        </li>
        <li>If you do all alright you would get long string, that you should provide to Voice object in init.</li>
    </ol>
</details>

<details>
  <summary>Browser option</summary>
    <p>Sorry, currently this part is not written, please come back later or make a pull request.</p>
</details>

## Usage example:
```python3
from voicy import Voice

voice = Voice(token="token")

print(
    voice.tts(
        text="Вы используете библиотеку voicy. Поставьте звездочку, "
              "если считаете ее полезной. Автор – Кирилл Фещенко",
        voice="2",
        format="wav"
    )
)
```
