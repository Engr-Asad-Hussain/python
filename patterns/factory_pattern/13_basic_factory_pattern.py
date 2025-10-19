# The central idea in Factory Method is to provide a separate component
# with the responsibility to decide which concrete implementation should be
# used based on some specified parameter.
# That parameter in our example is the format.
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
    The .serialize() method is the application code that depends on an
    interface to complete its task.
        * This is referred to as the CLIENT component of the pattern.
        * The interface defined is referred to as the PRODUCT component.

    The ._serialize_to_json() and ._serialize_to_xml() methods are concrete
    implementations of the product.

    The ._get_serializer() method is the creator component. The creator decides
    which concrete implementation to use.
    """

    def serialize(self, song: Song, format: Literal["JSON", "XML"]):
        serializer = self._get_serializer(format)
        return serializer(song)

    def _get_serializer(self, format: Literal["JSON", "XML"]) -> Callable[..., Any]:
        if format == "JSON":
            return self._serialize_to_json
        elif format == "XML":
            return self._serialize_to_xml
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


# Because you started with some existing code, all the
# components of Factory Method are members of the same class SongSerializer.
#
# Usually, this is not the case and, as you can see, none of the added
# methods use the self parameter. This is a good indication that they
# should not be methods of the SongSerializer class, and they can become
# external functions.
