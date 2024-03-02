import asyncio

from iot.message import MessageType


class HueHightDevice:
    async def connect(self) -> None:
        print("Connecting hue light ...")
        await asyncio.sleep(0.5)
        print("Hue light has been connected!")

    async def disconnect(self) -> None:
        print("Disconnecting hue light ...")
        await asyncio.sleep(0.5)
        print("Hue light has been disconnected!")

    async def send_message(self, message_type: MessageType, data: str = "") -> None:
        print(
            f"Hue light handling message of type: {message_type.name} with data: [{data}]"
        )
        await asyncio.sleep(0.5)
        print("Hue light received message!")


class SmartSpeakerDevice:
    async def connect(self) -> None:
        print("Connecting smart speaker ...")
        await asyncio.sleep(0.5)
        print("Smart speaker has been connected!")

    async def disconnect(self) -> None:
        print("Disconnecting smart speaker ...")
        await asyncio.sleep(0.5)
        print("Smart speaker has been disconnected!")

    async def send_message(self, message_type: MessageType, data: str = "") -> None:
        print(
            f"Smart speaker handling message of type: {message_type.name} with data: [{data}]"
        )
        await asyncio.sleep(0.5)
        print("Smart speaker received message!")


class OldToiletDevice:
    async def connect(self) -> None:
        print("Connecting old toilet ...")
        await asyncio.sleep(0.5)
        print("Old toilet has been connected!")

    async def disconnect(self) -> None:
        print("Disconnecting old toilet ...")
        await asyncio.sleep(0.5)
        print("Old toilet has been disconnected!")

    async def send_message(self, message_type: MessageType, data: str = "") -> None:
        print(
            f"Old toilet handling message of type: {message_type.name} with data: [{data}]"
        )
        await asyncio.sleep(0.5)
        print("Old toilet received message!")
