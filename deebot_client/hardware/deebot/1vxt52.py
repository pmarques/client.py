# DEBUG:deebot_client.authentication:Calling api(1/3): url=https://portal-ww.ecouser.net/api/appsvr/app.do, params=None, json={'userid': 'ghhluxb18bab213e', 'todo': 'GetGlobalDeviceList'}
# DEBUG:deebot_client.authentication:Success calling api url=https://portal-ww.ecouser.net/api/appsvr/app.do, params=None, json={'userid': 'ghhluxb18bab213e', 'todo': 'GetGlobalDeviceList'}, response={'code': 0, 'todo': 'result', 'ret': 'ok', 'devices': [{'did': '[REMOVED]', 'name': 'E05315612D1FP5BZ0025', 'class': '1vxt52', 'resource': 'zZpM', 'company': 'eco-ng', 'bindTs': 1701248539680, 'service': {'jmq': 'jmq-ngiot-eu.dc.ww.ecouser.net', 'mqs': 'api-ngiot.dc-as.ww.ecouser.net'}, 'deviceName': 'DEEBOT X1 OMNI', 'icon': 'https://portal-ww.ecouser.net/api/pim/file/get/6225bd1c2af2127804f540e5', 'ota': True, 'UILogicId': 't10_ww_n_omni', 'materialNo': '110-2102-0300', 'pid': '6185e29610683da4d6a7a9cd', 'product_category': 'DEEBOT', 'model': 'EINSTEIN_INT', 'updateInfo': {'needUpdate': False, 'changeLog': ''}, 'nick': 'X1 OMNI', 'homeId': '62efa88d85c763eaaa7a6064', 'homeSort': 1, 'status': 1, 'otaUpgrade': {}}]}
# WARNING:deebot_client.hardware.deebot:No capabilities found for 1vxt52. Using fallback.
"""DEEBOT X1 OMNI Capabilities."""
from deebot_client.capabilities import (
    Capabilities,
    CapabilityClean,
    CapabilityCleanAction,
    CapabilityCustomCommand,
    CapabilityEvent,
    CapabilityExecute,
    CapabilityLifeSpan,
    CapabilityMap,
    CapabilitySet,
    CapabilitySetEnable,
    CapabilitySettings,
    CapabilitySetTypes,
    CapabilityStats,
)
from deebot_client.commands.json.advanced_mode import GetAdvancedMode, SetAdvancedMode
from deebot_client.commands.json.battery import GetBattery
from deebot_client.commands.json.carpet import (
    GetCarpetAutoFanBoost,
    SetCarpetAutoFanBoost,
)
from deebot_client.commands.json.charge import Charge
from deebot_client.commands.json.charge_state import GetChargeState
from deebot_client.commands.json.clean import Clean, CleanArea, GetCleanInfo
from deebot_client.commands.json.clean_count import GetCleanCount, SetCleanCount
from deebot_client.commands.json.clean_logs import GetCleanLogs
from deebot_client.commands.json.clean_preference import (
    GetCleanPreference,
    SetCleanPreference,
)
from deebot_client.commands.json.continuous_cleaning import (
    GetContinuousCleaning,
    SetContinuousCleaning,
)
from deebot_client.commands.json.custom import CustomCommand
from deebot_client.commands.json.error import GetError
from deebot_client.commands.json.fan_speed import GetFanSpeed, SetFanSpeed
from deebot_client.commands.json.life_span import GetLifeSpan, ResetLifeSpan
from deebot_client.commands.json.map import GetCachedMapInfo, GetMajorMap, GetMapTrace
from deebot_client.commands.json.multimap_state import (
    GetMultimapState,
    SetMultimapState,
)
from deebot_client.commands.json.network import GetNetInfo
from deebot_client.commands.json.play_sound import PlaySound
from deebot_client.commands.json.pos import GetPos
from deebot_client.commands.json.relocation import SetRelocationState
from deebot_client.commands.json.stats import GetStats, GetTotalStats
from deebot_client.commands.json.true_detect import GetTrueDetect, SetTrueDetect
from deebot_client.commands.json.voice_assistant_state import (
    GetVoiceAssistantState,
    SetVoiceAssistantState,
)
from deebot_client.commands.json.volume import GetVolume, SetVolume
from deebot_client.commands.json.water_info import GetWaterInfo, SetWaterInfo
from deebot_client.const import DataType
from deebot_client.events import (
    AdvancedModeEvent,
    AvailabilityEvent,
    BatteryEvent,
    CachedMapInfoEvent,
    CarpetAutoFanBoostEvent,
    CleanCountEvent,
    CleanLogEvent,
    CleanPreferenceEvent,
    ContinuousCleaningEvent,
    CustomCommandEvent,
    ErrorEvent,
    FanSpeedEvent,
    FanSpeedLevel,
    LifeSpan,
    LifeSpanEvent,
    MajorMapEvent,
    MapChangedEvent,
    MapTraceEvent,
    MultimapStateEvent,
    NetworkInfoEvent,
    PositionsEvent,
    ReportStatsEvent,
    RoomsEvent,
    StateEvent,
    StatsEvent,
    TotalStatsEvent,
    TrueDetectEvent,
    VoiceAssistantStateEvent,
    VolumeEvent,
    WaterAmount,
    WaterInfoEvent,
)
from deebot_client.models import StaticDeviceInfo
from deebot_client.util import short_name

from . import DEVICES

DEVICES[short_name(__name__)] = StaticDeviceInfo(
    DataType.JSON,
    Capabilities(
        availability=CapabilityEvent(
            AvailabilityEvent, [GetBattery(is_available_check=True)]
        ),
        # confirmed
        battery=CapabilityEvent(BatteryEvent, [GetBattery()]),
        charge=CapabilityExecute(Charge),
        clean=CapabilityClean(
            action=CapabilityCleanAction(command=Clean, area=CleanArea),
            continuous=CapabilitySetEnable(
                ContinuousCleaningEvent,
                [GetContinuousCleaning()],
                SetContinuousCleaning,
            ),
            count=CapabilitySet(CleanCountEvent, [GetCleanCount()], SetCleanCount),
            log=CapabilityEvent(CleanLogEvent, [GetCleanLogs()]),
            preference=CapabilitySetEnable(
                CleanPreferenceEvent, [GetCleanPreference()], SetCleanPreference
            ),
        ),
        custom=CapabilityCustomCommand(
            event=CustomCommandEvent, get=[], set=CustomCommand
        ),
        # confirmed
        error=CapabilityEvent(ErrorEvent, [GetError()]),
        # confirmed
        fan_speed=CapabilitySetTypes(
            event=FanSpeedEvent,
            get=[GetFanSpeed()],
            set=SetFanSpeed,
            types=(
                FanSpeedLevel.QUIET,
                FanSpeedLevel.NORMAL,
                FanSpeedLevel.MAX,
                FanSpeedLevel.MAX_PLUS,
            ),
        ),
        # confirmed
        life_span=CapabilityLifeSpan(
            types=(
                LifeSpan.BRUSH,
                LifeSpan.FILTER,
                LifeSpan.SIDE_BRUSH,
                LifeSpan.UNIT_CARE,
                LifeSpan.ROUND_MOP,
            ),
            event=LifeSpanEvent,
            get=[
                GetLifeSpan(
                    [
                        LifeSpan.BRUSH,
                        LifeSpan.FILTER,
                        LifeSpan.SIDE_BRUSH,
                        LifeSpan.UNIT_CARE,
                        LifeSpan.ROUND_MOP,
                    ]
                )
            ],
            reset=ResetLifeSpan,
        ),
        map=CapabilityMap(
            chached_info=CapabilityEvent(CachedMapInfoEvent, [GetCachedMapInfo()]),
            changed=CapabilityEvent(MapChangedEvent, []),
            major=CapabilityEvent(MajorMapEvent, [GetMajorMap()]),
            multi_state=CapabilitySetEnable(
                MultimapStateEvent, [GetMultimapState()], SetMultimapState
            ),
            position=CapabilityEvent(PositionsEvent, [GetPos()]),
            relocation=CapabilityExecute(SetRelocationState),
            rooms=CapabilityEvent(RoomsEvent, [GetCachedMapInfo()]),
            trace=CapabilityEvent(MapTraceEvent, [GetMapTrace()]),
        ),
        # confirmed
        network=CapabilityEvent(NetworkInfoEvent, [GetNetInfo()]),
        # confirmed
        play_sound=CapabilityExecute(PlaySound),
        settings=CapabilitySettings(
            advanced_mode=CapabilitySetEnable(
                AdvancedModeEvent, [GetAdvancedMode()], SetAdvancedMode
            ),
            carpet_auto_fan_boost=CapabilitySetEnable(
                CarpetAutoFanBoostEvent,
                [GetCarpetAutoFanBoost()],
                SetCarpetAutoFanBoost,
            ),
            true_detect=CapabilitySetEnable(
                TrueDetectEvent, [GetTrueDetect()], SetTrueDetect
            ),
            voice_assistant=CapabilitySetEnable(
                VoiceAssistantStateEvent,
                [GetVoiceAssistantState()],
                SetVoiceAssistantState,
            ),
            volume=CapabilitySet(VolumeEvent, [GetVolume()], SetVolume),
        ),
        # NOTE: GetCleanInfo is not supported
        state=CapabilityEvent(StateEvent, [GetChargeState(), GetCleanInfo()]),
        # confirmed
        stats=CapabilityStats(
            clean=CapabilityEvent(StatsEvent, [GetStats()]),
            report=CapabilityEvent(ReportStatsEvent, []),
            total=CapabilityEvent(TotalStatsEvent, [GetTotalStats()]),
        ),
        # confirmed
        water=CapabilitySetTypes(
            event=WaterInfoEvent,
            get=[GetWaterInfo()],
            set=SetWaterInfo,
            types=(
                WaterAmount.LOW,
                WaterAmount.MEDIUM,
                WaterAmount.HIGH,
            ),
        ),
    ),
)
