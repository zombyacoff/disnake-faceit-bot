from __future__ import annotations

import logging

import decouple

from .bot import FaceitBot
from .cogs import StatsCommand
from .utils import setup_logging

logger = logging.getLogger(__name__)


def main() -> None:
    setup_logging()

    token = decouple.config("DISCORD_BOT_TOKEN", default=None)
    if token is None:
        logger.error("DISCORD_BOT_TOKEN not found in environment or .env file.")
        return

    bot = FaceitBot()
    bot.add_cog(StatsCommand(bot))
    logger.info("Starting FACEIT Discord Bot...")
    bot.run(token)


if __name__ == "__main__":
    main()
