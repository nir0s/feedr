LOGGER = {
    "version": 1,
    "formatters": {
        "file": {
            "format": "%(asctime)s %(levelname)s - %(message)s"
        },
        "console": {
            "format": "### %(levelname)s - %(message)s"
        }
    },
    "handlers": {
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "file",
            "level": "DEBUG",
            "filename": "feeder.log",
            "maxBytes": "5000000",
            "backupCount": "20"
        },
        "console": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "console"
        }
    },
    "loggers": {
        "user": {
            "handlers": ["file", "console"]
        },
    }
}
