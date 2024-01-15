import asyncio
import logging
import os

import aiohttp

from deebot_client.api_client import ApiClient
from deebot_client.authentication import Authenticator
from deebot_client.commands.json import (
    GetBattery,
    GetCachedMapInfo,
    GetChargeState,
    GetCleanInfo,
    GetError,
    GetFanSpeed,
    GetLifeSpan,
    GetNetInfo,
    GetStats,
    GetTotalStats,
    GetWaterInfo,
)
from deebot_client.device import Device
from deebot_client.events import LifeSpan
from deebot_client.models import Configuration
from deebot_client.util import md5

device_id = md5("vscode")  # str(time.time()))
account_id = os.getenv("DEEBOT_USERNAME")
password_hash = md5(os.getenv("DEEBOT_PASSWORD"))
country = "uk"


# async def on_request_start(session, trace_config_ctx, params):
#     print("Starting request")


# async def on_request_end(session, trace_config_ctx, params):
#     print("Ending request")


async def main():
    # trace_config = aiohttp.TraceConfig()
    # trace_config.on_request_start.append(on_request_start)
    # trace_config.on_request_end.append(on_request_end)
    # async with aiohttp.ClientSession(trace_configs=[trace_config]) as session:
    async with aiohttp.ClientSession() as session:
        logging.basicConfig(level=logging.DEBUG)
        config = Configuration(session, device_id=device_id, country=country)

        authenticator = Authenticator(config, account_id, password_hash)
        api_client = ApiClient(authenticator)

        devices_ = await api_client.get_devices()

        bot = Device(devices_[0], authenticator)

        # mqtt_config = MqttConfiguration(config=config)
        # mqtt = MqttClient(mqtt_config, authenticator)

        # await bot.initialize(mqtt)

        # async def on_battery(event: BatteryEvent):
        #     print(event)
        #     # # Do stuff on battery event
        #     # if event.value == 100:
        #     #     # Battery full
        #     #     pass

        # # Subscribe for events (more events available)
        # bot.events.subscribe(BatteryEvent, on_battery)

        # Execute commands
        # await bot.execute_command(Clean(CleanAction.START))
        # await asyncio.sleep(900)  # Wait for...
        # await bot.execute_command(Charge())

        await asyncio.sleep(2)
        print("\n\n\n\n\n")
        print("\n\n=== Get Stats ===")
        await bot.execute_command(GetStats())
        await bot.execute_command(GetTotalStats())
        await asyncio.sleep(2)
        print("\n\n=== Get Battery ===")
        await bot.execute_command(GetBattery())
        await asyncio.sleep(2)
        print("\n\n=== Get Errors ===")
        await bot.execute_command(GetError())
        await asyncio.sleep(2)
        print("\n\n=== Get State ===")
        await bot.execute_command(GetChargeState())
        # NOTE: Not supported
        # 'body': {'data': {'trigger': 'none'}, 'code': 20003, 'msg': 'task type did  not support'}}, 'id': 'bhQT', 'payloadType': 'j'}
        await bot.execute_command(GetCleanInfo())
        await asyncio.sleep(2)
        print("\n\n=== Get Fan Speed ===")
        await bot.execute_command(GetFanSpeed())
        await asyncio.sleep(2)
        print("\n\n=== Get Water Info ===")
        await bot.execute_command(GetWaterInfo())
        await asyncio.sleep(2)
        print("\n\n=== Get Net Info ===")
        await bot.execute_command(GetNetInfo())
        await asyncio.sleep(2)
        print("\n\n=== Get Cached Map Info ===")
        await bot.execute_command(GetCachedMapInfo())
        await asyncio.sleep(2)
        print("\n\n=== Get Life Span ===")
        await bot.execute_command(
            GetLifeSpan(
                [
                    LifeSpan.BRUSH,
                    LifeSpan.FILTER,
                    LifeSpan.SIDE_BRUSH,
                    LifeSpan.UNIT_CARE,
                    LifeSpan.ROUND_MOP,
                ]
            )
        )
        await asyncio.sleep(2)
        # while True:
        #     # print("\n\nplay sound")
        #     # await bot.execute_command(PlaySound())
        #     await asyncio.sleep(10)

        # await mqtt.disconnect()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
