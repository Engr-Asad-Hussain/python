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
            return json.dumps(
                {
                    "id": song.id,
                    "title": song.title,
                    "artist": song.artist,
                }
            )
        elif format == "XML":
            song_info = et.Element("song", attrib={"id": song.id})
            title = et.SubElement(song_info, "title")
            title.text = song.title
            artist = et.SubElement(song_info, "artist")
            artist.text = song.artist
            return et.tostring(song_info, encoding="unicode")
        else:
            raise ValueError(f"Unsupported format: {format}")


song1 = Song(id=1, title="Water of Love", artist="Dire Straits")
song_serializer = SongSerializer()
song_serializer.serialize(song1, format="JSON")
song_serializer.serialize(song1, format="XML")
song_serializer.serialize(song1, format="YAML")  # Raise exception

## Problems:

# 1. Complex logical code uses if/elif/else structures to change the
# behavior of an application. Using if/elif/else conditional structures
# makes the code harder to read, harder to understand, and harder to maintain.

# 2. The single responsibility principle states that a module, a class,
# or even a method should have a single responsibility. It should do just
# one thing and have only one reason to change. The .serialize() method
# in SongSerializer will require changes for many different reasons.
# This increases the risk of introducing new defects or breaking existing
# functionality when changes are made. Let’s take a look at all the
# situations that will require modifications to the implementation:
#    - When a new format is introduced: The method will have to change to
#       implement the serialization to that format.
#    - When the Song object changes: Adding or removing properties to the
#       Song class will require the implementation to change in order to
#       accommodate the new structure.
#    - When the string representation for a format changes (plain JSON vs
#       JSON API): The .serialize() method will have to change if the
#       desired string representation for a format changes because the
#       representation is hard-coded in the .serialize() method implementation.

# The ideal situation would be if any of those changes in requirements
# could be implemented without changing the .serialize() method.
