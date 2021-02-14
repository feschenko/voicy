<h1>Voicy</h1>
<h4>Wrapper for free use Google cloud TTS.</h4>


<h2>Installation:</h2>
<h6>Download library using pip</h6>

```bash
$ pip3 install voicy
```


<h2>Getting the token:</h2>

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
For using TTS you need to provide a voice setting. In Voicy you need to provide a dictionary, with a key, that is your 
language code and voice model. Format to both you can find in
<a href="https://cloud.google.com/text-to-speech/docs/voices">docs</a>
<p>. Example <code>{"en-US": "en-US-Wavenet-A"}</code>. 

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
