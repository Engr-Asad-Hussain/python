import json
import random
import string
import xml.etree.ElementTree as et
from typing import Any, Literal


class JSONSerializer:
    def __init__(self) -> None:
        self._current_object: dict[str, Any] = {}

    def start_object(self, object_name: str, object_id: str | int):
        self._current_object["id"] = object_id

    def add_property(self, name: str, value: Any):
        self._current_object[name] = value

    def to_string(self):
        return json.dumps(self._current_object)


class XMLSerializer:
    def __init__(self) -> None:
        self._element: et.Element = None

    def start_object(self, object_name: str, object_id: str | int):
        self._element = et.Element(object_name, attrib={"id": object_id.__str__()})

    def add_property(self, name: str, value: Any):
        prop = et.SubElement(self._element, name)
        prop.text = value

    def to_string(self):
        return et.tostring(self._element, encoding="unicode")


# Factory Creator
class SerializerFactory:
    def get_serializer(self, format: Literal["JSON", "XML"]):
        if format == "JSON":
            return JSONSerializer()
        elif format == "XML":
            return XMLSerializer()
        else:
            raise ValueError(f"Unsupported format `{format}")


class Song:
    def __init__(self, id: str, title: str, artist: str) -> None:
        self.id = id
        self.title = title
        self.artist = artist

    def serialize(self, serializable: JSONSerializer | XMLSerializer):
        serializable.start_object("id", self.id)
        serializable.add_property("title", self.title)
        serializable.add_property("artist", self.artist)


class ObjectSerializer:
    def serialize(
        self,
        object: Song,
        factory: SerializerFactory,
        format: Literal["JSON", "XML"],
    ):
        # Which serializer to create [JSON | XML | ...]
        serializer = factory.get_serializer(format)
        # Add attributes to particular serializer
        object.serialize(serializer)
        # Return string representation to that serializer
        return serializer.to_string()


def generate_id(length: int = 8) -> str:
    return "".join(random.choices(string.ascii_letters, k=length))


song = Song(id=generate_id(), title="We love Pakistan...", artist="Anonymous")
factory = SerializerFactory()
serializer = ObjectSerializer()
print(serializer.serialize(song, factory, format="JSON"))
print(serializer.serialize(song, factory, format="XML"))
print(serializer.serialize(song, factory, format="YAML"))
