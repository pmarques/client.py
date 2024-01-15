"""Battery commands."""

from deebot_client.messages.json import OnBattery

from .common import JsonCommandWithMessageHandling


# class GetBattery(OnBattery, JsonCommandWithMessageHandling, CommandMqttP2P):
class GetBattery(OnBattery, JsonCommandWithMessageHandling):
    """Get battery command."""

    name = "getBattery"
    # _mqtt_params = MappingProxyType({"type": InitParam(LifeSpan, "battery")})
    # _mqtt_params = MappingProxyType({"id": InitParam(int)})

    def __init__(self, *, is_available_check: bool = False) -> None:
        super().__init__()
        self._is_available_check = is_available_check

    # def handle_mqtt_p2p(self, event_bus: EventBus, response: dict[str, Any]) -> None:
    #     """Handle response received over the mqtt channel "p2p"."""
    #     print("\n\n\n\n\nhandle_mqtt_p2p")
    #     result = self.handle(event_bus, response)
    #     if result.state == HandlingState.SUCCESS:
    #         event_bus.request_refresh(LifeSpanEvent)
