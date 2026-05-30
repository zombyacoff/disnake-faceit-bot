from __future__ import annotations


def setup_logging() -> None:
    import logging  # noqa: PLC0415

    logging.basicConfig(
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S",
        level=logging.INFO,
    )
