import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback

from .const import (
    DOMAIN,
    CONF_HOST,
    CONF_PORT,
    CONF_SCAN_INTERVAL,
    CONF_TIMEOUT,
    CONF_RETRIES,
    DEFAULT_SCAN_INTERVAL,
    DEFAULT_TIMEOUT,
    DEFAULT_RETRIES,
)


class PortMonitorConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(
                title=f"{user_input[CONF_HOST]}:{user_input[CONF_PORT]}",
                data=user_input,
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_HOST): str,
                vol.Required(CONF_PORT): int,
                vol.Optional(CONF_SCAN_INTERVAL, default=DEFAULT_SCAN_INTERVAL): int,
                vol.Optional(CONF_TIMEOUT, default=DEFAULT_TIMEOUT): int,
                vol.Optional(CONF_RETRIES, default=DEFAULT_RETRIES): int,
            }),
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return PortMonitorOptionsFlow(config_entry)


class PortMonitorOptionsFlow(config_entries.OptionsFlow):
    def __init__(self, entry):
        self.entry = entry

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Optional(
                    CONF_SCAN_INTERVAL,
                    default=self.entry.options.get(
                        CONF_SCAN_INTERVAL,
                        self.entry.data.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL),
                    ),
                ): int,
                vol.Optional(
                    CONF_TIMEOUT,
                    default=self.entry.options.get(
                        CONF_TIMEOUT,
                        self.entry.data.get(CONF_TIMEOUT, DEFAULT_TIMEOUT),
                    ),
                ): int,
                vol.Optional(
                    CONF_RETRIES,
                    default=self.entry.options.get(
                        CONF_RETRIES,
                        self.entry.data.get(CONF_RETRIES, DEFAULT_RETRIES),
                    ),
                ): int,
            }),
        )
