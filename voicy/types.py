from pydantic import BaseModel


class File(BaseModel):
    """This object represents an audio file. Contains a path and file format."""

    path: str
    format: str


class Transcript(BaseModel):
    """This object represents a transcript of an audio file.
    Contains text, transcript confidence, and a path to an audio file with its format."""

    text: str
    confidence: float
    file: File
