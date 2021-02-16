from setuptools import setup, find_packages
import pathlib
import re

WORK_DIR = pathlib.Path(__file__).parent

try:
    with open("README.md", "r", encoding="utf-8") as readme:
        long_description = readme.read()
except:
    long_description = "Wrapper for free use Google cloud TTS and STT."


def get_version():
    try:
        file = (WORK_DIR / "voicy" / "__init__.py").read_text("utf-8")
        return re.findall(r"^__version__ = \"([^\"]+)\"\r?$", file, re.M)[0]
    except IndexError:
        raise RuntimeError("Unable to determine version.")


setup(
    name="voicy",
    version=get_version(),
    description="Wrapper for free use Google cloud TTS.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="wrapper text-to-speech google-cloud tts stt tts-engines wrapper-library tts-api "
    "google-cloud-text-to-speech google-cloud-tts stt-engines stt-api google-cloud-speech-to-text",
    author="Kirill Feschenko",
    author_email="swipduces@yandex.com",
    python_requires=">=3.7.0",
    url="https://github.com/xcaq/voicy/",
    packages=find_packages(),
    install_requires=["requests", "python-rucaptcha", "pydantic", "pydub"],
    include_package_data=True,
    license="GNU LGPLv3",
    classifiers=[
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
        "Typing :: Typed",
    ],
)
