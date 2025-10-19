import json
import xml.etree.ElementTree as et
from typing import Any, Callable, Literal


class Song:
    def __init__(self, id: int, title: str, artist: str) -> None:
        self.id = id
        self.title = title
        self.artist = artist


class SongSerializer:
    """
    The mechanics of Factory Method are always the same.

    A client SongSerializer.serialize() depends on a concrete
    implementation of an interface.

    It requests the implementation from a creator component get_serializer()
    using some sort of identifier (format).

    The creator returns the concrete implementation according to the value
    of the parameter to the client, and the client uses the provided object
    to complete its task.
    """

    def serialize(self, song: Song, format: Literal["JSON", "XML"]):
        serializer = _get_serializer(format)
        return serializer(song)


def _get_serializer(format: Literal["JSON", "XML"]) -> Callable[..., Any]:
    if format == "JSON":
        return _serialize_to_json
    elif format == "XML":
        return _serialize_to_xml
    else:
        raise ValueError(f"Unsupported format: {format}")


def _serialize_to_json(song: Song) -> str:
    return json.dumps(
        {
            "id": song.id,
            "title": song.title,
            "artist": song.artist,
        }
    )


def _serialize_to_xml(song: Song) -> str:
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
