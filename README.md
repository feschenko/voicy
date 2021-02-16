<h1>Voicy</h1>
<h4>Wrapper for free use Google Сloud TTS and STT.</h4>


<h2>Installation:</h2>
<h6>Download library using pip</h6>

```bash
$ pip3 install voicy -U
```


<h2>Getting the token:</h2>

<p>
    For a request to the Google Cloud client need to provide a token. You can easily get it using Token object,
    or in a browser by yourself.
</p>
<p>Both options are described below:</p>

<details>
  <summary>Automated option</summary>
    <ol>
        <li>By first, you need to get API key in <a href="http://rucaptcha.com/">rucaptcha</a>.</li>
        <li>
            After that import a Token object from voicy:
            <br>
            <code>from voicy import Token</code>
        </li>
        <li>
            Then provide the API key to the get_token function:
            <br>
            <code>Token.get_token(rucaptcha_key="Key, that you got in the rucaptcha account.")</code>
        </li>
        <li>If you do all alright you would get long string, that you should provide to Voice object in init.</li>
    </ol>
</details>

<details>
  <summary>Browser option</summary>
    <ol>
        <li>By first, go to <a href="https://cloud.google.com/text-to-speech">cloud.google.com/text-to-speech</a>.</li>
        <li>
            After that scroll down to the demo part.
            <br>
            <img src=".github/images/Recaptcha.png" alt="Recaptcha">
        </li>
        <li>Solve the captcha.</li>
        <li>
            After, open the developer console and go to the "Network" section. In column "Name" search for 
            proxy?url=https://texttospeech.googleapis.com ...
            <br>
            <img src=".github/images/DeveloperConsole.png" alt="The developer console">
            <br>
            Scroll to the "Query string parameters". And here is your token.
        </li>
    </ol>
</details>


<h2>Usage example:</h2>

<p>
For using TTS you need to provide a dictionary with a key, that is your language code and value – voice model. 
Format to both you can find in <a href="https://cloud.google.com/text-to-speech/docs/voices">docs</a>.
</p>

<h5>Simple TTS example:</h5>

```python3
from voicy import Voicy

voicy = Voicy(token="token")

print(
    voicy.tts(
        text="You are using a Voicy library. Please, give a star, if you like it.",
        voice={"en-US": "en-US-Wavenet-A"},
    )
)
```

<h6>This example will return <code>File(path="84PFetz5IJdT4Je.wav", format="wav")</code></h6>

<br> 

<h5>Simple STT example:</h5>

<p>
For using STT you only need to provide a language code. This value is the language of your audio file.
Format for the language code you can find in <a href="https://cloud.google.com/text-to-speech/docs/voices">docs</a>.
</p>

```python3
from voicy import Voicy

voicy = Voicy(token="token")

print(
    voicy.stt(
        file="84PFetz5IJdT4Je.wav",
        language_code="en-US",
    )
)
```

<h6> This example will return <code>Transcript(text="You are using a Voicy library. Please, give a star, if you like it.", confidence=0.93750596, path="84PFetz5IJdT4Je.wav", format="wav")</code>
</h6>

<br> 

<h5>Google Translate TTS example:</h5>

<p>
    If you don't want to get the token, you can use TTS from Google Translate. You don't need to provide anything, 
    but the max text length for one request is 200 characters, and you can use only one voice model.
</p>

```python3
from voicy import Voicy

voicy = Voicy()

print(
    voicy.translate_tts(
        text="You are using a Voicy library. Please, give a star, if you like it.",
        language_code="en-US",
    )
)
```   
<h6>This example will return <code>File(path="ILSp8RHEMFyNW9M.wav", format="wav")</code></h6>


<h2>🤝 Contributing</h2>
<a href="https://github.com/xcaq/voicy/graphs/contributors" align=center>Feel free to contribute.</a>