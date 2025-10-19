import json
import xml.etree.ElementTree as et
from typing import Literal


class Song:
    def __init__(self, id: int, title: str, artist: str) -> None:
        self.id = id
        self.title = title
        self.artist = artist


class SongSerializer:
    def serialize(self, song: Song, format: Literal["JSON", "XML"]):
        if format == "JSON":
            return self._serialize_to_json(song)
        elif format == "XML":
            return self._serialize_to_xml(song)
        else:
            raise ValueError(f"Unsupported format: {format}")

    def _serialize_to_json(self, song: Song) -> str:
        return json.dumps(
            {
                "id": song.id,
                "title": song.title,
                "artist": song.artist,
            }
        )

    def _serialize_to_xml(self, song: Song) -> str:
        song_info = et.Element("song", attrib={"id": song.id})
        title = et.SubElement(song_info, "title")
        title.text = song.title
        artist = et.SubElement(song_info, "artist")
        artist.text = song.artist
        return et.tostring(song_info, encoding="unicode")


song1 = Song(id=1, title="Water of Love", artist="Dire Straits")
song_serializer = SongSerializer()
song_serializer.serialize(song1, format="JSON")
song_serializer.serialize(song1, format="XML")
song_serializer.serialize(song1, format="YAML")  # Raise exception
