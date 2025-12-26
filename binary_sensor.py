import asyncio
import socket
import time
from datetime import timedelta

from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.event import async_track_time_interval

from .const import (
    CONF_HOST,
    CONF_PORT,
    CONF_SCAN_INTERVAL,
    CONF_TIMEOUT,
    CONF_RETRIES,
    DEFAULT_SCAN_INTERVAL,
    DEFAULT_TIMEOUT,
    DEFAULT_RETRIES,
)

async def async_setup_entry(hass, entry, async_add_entities):
    monitor = TCPPortMonitor(hass, entry)
    async_add_entities([monitor.binary, monitor.latency])
    monitor.start()


class TCPPortMonitor:
    def __init__(self, hass, entry):
        self.hass = hass
        self.entry = entry

        self.host = entry.data[CONF_HOST]
        self.port = entry.data[CONF_PORT]

        self.interval = timedelta(
            seconds=entry.options.get(
                CONF_SCAN_INTERVAL,
                entry.data.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL),
            )
        )
        self.timeout = entry.options.get(
            CONF_TIMEOUT,
            entry.data.get(CONF_TIMEOUT, DEFAULT_TIMEOUT),
        )
        self.retries = entry.options.get(
            CONF_RETRIES,
            entry.data.get(CONF_RETRIES, DEFAULT_RETRIES),
        )

        self.binary = PortBinarySensor(self)
        self.latency = PortLatencySensor(self)

    def start(self):
        async_track_time_interval(self.hass, self._async_check, self.interval)

    async def _async_check(self, now):
        loop = asyncio.get_running_loop()

        for _ in range(self.retries):
            start = time.perf_counter()
            try:
                await loop.run_in_executor(None, self._check_socket)
                latency = int((time.perf_counter() - start) * 1000)

                self.binary.set_state(True)
                self.latency.set_state(latency)
                return
            except Exception:
                await asyncio.sleep(0.1)

        self.binary.set_state(False)
        self.latency.set_state(None)

    def _check_socket(self):
        with socket.create_connection(
            (self.host, self.port), timeout=self.timeout
        ):
            pass


class PortBinarySensor(BinarySensorEntity):
    def __init__(self, monitor):
        self.monitor = monitor
        self._attr_name = f"Port {monitor.host}:{monitor.port}"
        self._attr_unique_id = f"{monitor.entry.entry_id}_binary"
        self._attr_device_class = "connectivity"
        self._attr_is_on = False

    def set_state(self, state):
        self._attr_is_on = state
        self.async_write_ha_state()


class PortLatencySensor(SensorEntity):
    def __init__(self, monitor):
        self.monitor = monitor
        self._attr_name = f"Port {monitor.host}:{monitor.port} Latency"
        self._attr_unique_id = f"{monitor.entry.entry_id}_latency"
        self._attr_unit_of_measurement = "ms"
        self._attr_state_class = "measurement"
        self._attr_native_value = None

    def set_state(self, latency):
        self._attr_native_value = latency
        self.async_write_ha_state()
