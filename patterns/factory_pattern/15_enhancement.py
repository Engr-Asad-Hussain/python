import json
import xml.etree.ElementTree as et
from abc import ABC, abstractmethod
from typing import Any, Literal


class Serializer(ABC):
    @abstractmethod
    def start_object(self, object_name: str, object_id: str | int) -> None: ...

    @abstractmethod
    def add_property(self, name: str, value: Any) -> None: ...

    @abstractmethod
    def to_string(self) -> str: ...


class JSONSerializer(Serializer):
    def __init__(self) -> None:
        self._current_object: dict[str, Any] = {}

    def start_object(self, object_name: str, object_id: str | int) -> None:
        self._current_object["id"] = object_id

    def add_property(self, name: str, value: Any) -> None:
        self._current_object[name] = value

    def to_string(self) -> str:
        return json.dumps(self._current_object)


class XMLSerializer(Serializer):
    def __init__(self) -> None:
        self._element: et.Element = None

    def start_object(self, object_name: str, object_id: str | int) -> None:
        self._element = et.Element(object_name, attrib={"id": object_id.__str__()})

    def add_property(self, name: str, value: Any) -> None:
        prop = et.SubElement(self._element, name)
        prop.text = value

    def to_string(self) -> str:
        return et.tostring(self._element, encoding="unicode")


class SongSerializer:
    def __init__(self, id: int, title: str, artist: str) -> None:
        self.id = id
        self.title = title
        self.artist = artist

    def serialize(self, serializer: Serializer):
        serializer.start_object(name="song", value=self.id)
        serializer.start_object(name="title", value=self.title)
        serializer.start_object(name="artist", value=self.artist)


class SerializerFactory:
    """
    In the original example, you implemented the creator as a
    function (_get_serializer). Functions are fine for very simple examples,
    but they don't provide too much flexibility when requirements change.

    Classes can provide additional interfaces to add functionality,
    and they can be derived to customize behavior. Unless you have a very
    basic creator that will never change in the future, you want to implement
    it as a class and not a function. These type of classes are called
    object factories.
    """

    def get_serializer(self, format: Literal["JSON", "XML"]) -> Serializer:
        if format == "JSON":
            return JSONSerializer()
        elif format == "XML":
            return XMLSerializer()
        else:
            raise ValueError(f"Unsupported format: {format}")


factory = SerializerFactory()


class ObjectSerializer:
    def serialize(self, serializable: SongSerializer, format: Literal["JSON", "XML"]):
        serializer = factory.get_serializer(format)
        serializable.serialize(serializer)
        return serializer.to_string()


song = SongSerializer(id=1, title="We love Pakistan...", artist="Anonymous")
serializer = ObjectSerializer()
serializer.serialize(serializable=song, format="JSON")
serializer.serialize(serializable=song, format="XML")
serializer.serialize(serializable=song, format="YAML")
