<h1>Voicy</h1>
<h4>Wrapper for free use TTS & STT services.</h4>


<h2>Installation:</h2>
<h6>Download library using pip</h6>

```bash
$ pip3 install voicy -U
```


<h2>Usage example:</h2>

<h3>Google Cloud</h3>

<p>
    For a request to the Google Cloud client, you need to provide a token. You can easily get it using GoogleToken object,
    or in a browser by yourself.
</p>
<p>Both options are described below:</p>

<details>
  <summary>Automated option</summary>
    <ol>
        <li>By first, you need to get API key in <a href="http://rucaptcha.com/">rucaptcha</a>.</li>
        <li>
            After that import a GoogleToken object from voicy:
            <br>
            <code>from voicy import GoogleToken</code>
        </li>
        <li>
            Then provide the API key to the get_token function:
            <br>
            <code>GoogleToken.get_token(rucaptcha_key="Key, that you got in the rucaptcha account.")</code>
        </li>
        <li>If you do all alright you would get long string, that you should provide to Google object in init.</li>
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
            Scroll to the "Query string parameters". That long string is your token. Provide it to Google object in init.  
        </li>
    </ol>
</details>


<p>
For using TTS you need to provide a dictionary where the key is your language code and the value is your voice model.
Format to both you can find in <a href="https://cloud.google.com/text-to-speech/docs/voices">docs</a>. Also, 
if you don't want to get a token you can use a TTS from Google Translate.
</p>

<h5>Simple TTS example:</h5>

```python3
from voicy import Google

google = Google(token="token")

print(
    google.tts(
        text="You are using a Voicy library. Please, give a star, if you like it.",
        voice={"en-US": "en-US-Wavenet-A"},
    )
)
```

<h6>This example will return <code>File(path="84PFetz5IJdT4Je.wav", format="wav")</code></h6>

<br> 

<h5>Simple STT example:</h5>

<p>
For using STT you only need to provide a language code.
Format for it you can find in <a href="https://cloud.google.com/text-to-speech/docs/voices">docs</a>.
</p>

```python3
from voicy import Google

google = Google(token="token")

print(
    google.stt(
        file="84PFetz5IJdT4Je.wav",
        language_code="en-US",
    )
)
```

<h6> This example will return <code>Transcript(text="You are using a Voicy library. Please, give a star, if you like it.", confidence=0.93750596, path="84PFetz5IJdT4Je.wav", format="wav")</code>
</h6>

<br> 

<h3>Yandex Cloud:</h3>

<p>For using Yandex TTS you don't need to provide any token. Just pass text, language code and voice model:</p>

```python3
from voicy import Yandex

yandex = Yandex()

print(
    yandex.tts(
        text="You are using a Voicy library. Please, give a star, if you like it.",
        language_code="en-US",
        voice="ermil",
    )
)
```

<h6>This example will return <code>File(path="SUypGpSLTvGKTTy.wav", format="wav")</code></h6>


<h2>License</h2>
<p>The library is under the GNU LGPLv3 license.</p>
<p>
    BE AWARE THAT THE AUTHORS ARE UNDER NO CIRCUMSTANCES RESPONSIBLE FOR CONSEQUENCES OF USE AND 
    ANY INTERACTION WITH THE LIBRARY. NOT LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF 
    CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
    IN THE SOFTWARE. THE CODE IS PROVIDED FOR EDUCATION PURPOSES ONLY.
</p>
<p>
    Read the <a href="https://github.com/xcaq/voicy/blob/master/LICENSE">LICENSE</a> for more information.
</p>


<h2>Contributing</h2>

<a href="https://github.com/xcaq/voicy/graphs/contributors">Feel free to contribute.</a>