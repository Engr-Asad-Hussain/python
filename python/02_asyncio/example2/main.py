import asyncio
from typing import Any, Awaitable

from iot.devices import HueHightDevice, OldToiletDevice, SmartSpeakerDevice
from iot.message import Message, MessageType
from iot.service import IoTService


async def run_sequence(*functions: Awaitable[Any]) -> None:
    for function in functions:
        await function


async def run_parallel(*functions: Awaitable[Any]) -> None:
    await asyncio.gather(*functions)


async def main():
    # Create IoT Service
    iot_service = IoTService()

    # Create devices
    hue_light = HueHightDevice()
    smart_speaker = SmartSpeakerDevice()
    old_toilet = OldToiletDevice()

    # Register devices with IoTService
    hue_light_id, smart_speaker_id, old_toilet_id = await asyncio.gather(
        iot_service.register_device(hue_light),
        iot_service.register_device(smart_speaker),
        iot_service.register_device(old_toilet),
    )

    # Create program
    wake_up_task = [
        Message(hue_light_id, MessageType.SWITCH_ON),
        Message(smart_speaker_id, MessageType.SWITCH_ON),
        Message(smart_speaker_id, MessageType.PLAY_SONG, "Miles days ... Oham Oham!"),
    ]
    # sleep_task = [
    #     Message(hue_light_id, MessageType.SWITCH_OFF),
    #     Message(smart_speaker_id, MessageType.SWITCH_OFF),
    #     Message(old_toilet_id, MessageType.FLUSH),
    #     Message(old_toilet_id, MessageType.CLEAN),
    # ]

    # Run the programs
    print()
    await iot_service.run_program(wake_up_task)
    print()

    # await iot_service.run_program(sleep_task)
    # With above approach, there are couple of programs that depends on each other for example,
    # toilet CLEAN will be done after FLUSH. But it works parallel with this appraoch.

    await run_parallel(
        iot_service.send_msg(Message(hue_light_id, MessageType.SWITCH_OFF)),
        iot_service.send_msg(Message(smart_speaker_id, MessageType.SWITCH_OFF)),
        run_sequence(
            iot_service.send_msg(Message(old_toilet_id, MessageType.FLUSH)),
            iot_service.send_msg(Message(old_toilet_id, MessageType.CLEAN)),
        ),
    )


if __name__ == "__main__":
    asyncio.run(main())
