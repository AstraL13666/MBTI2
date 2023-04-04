from config_data import DEFAULT_COMMANDS


async def set_default_commands(dp):
    await dp.bot.set_my_commands(DEFAULT_COMMANDS)
