import logging


def get_logger(name: str, log_level: str = "INFO") -> logging.Logger:
    logging.basicConfig(level=log_level)
    return logging.getLogger(name)
