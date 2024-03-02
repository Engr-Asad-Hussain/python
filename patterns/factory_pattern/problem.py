import json
import random
import string
import xml.etree.ElementTree as et
from typing import Literal


class Song:
    def __init__(self, id: str, title: str, artist: str) -> None:
        self.id = id
        self.title = title
        self.artist = artist


class SongSerializer:
    def serialize(self, song: Song, format: Literal["JSON", "XML"]):
        if format == "JSON":
            info = {"id": song.id, "title": song.title, "artist": song.artist}
            return json.dumps(info)
        elif format == "XML":
            info = et.Element("song", attrib={"id": song.id})
            title = et.SubElement(info, "title")
            title.text = song.title
            artist = et.SubElement(info, "artist")
            artist.text = song.artist
            return et.tostring(info, encoding="unicode")
        else:
            raise ValueError(f"Unsupported format `{format}")


def generate_id(length: int = 8) -> str:
    return "".join(random.choices(string.ascii_letters, k=length))


song = Song(id=generate_id(), title="We love Pakistan...", artist="Anonymous")
serializer = SongSerializer()
print(serializer.serialize(song, format="JSON"))
print(serializer.serialize(song, format="XML"))
print(serializer.serialize(song, format="YAML"))
