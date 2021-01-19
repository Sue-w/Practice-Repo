"""
Specifying the dictionary for the logging configuration

"""
import logging.config

dictConfiguration = {
    "version": 1,
    "handlers": {
        "fileHandler": {
            "class": "logging.FileHandler",
            "formatter": "myFormatter",
            "filename": "my_file.log"
        }
    },
    "loggers": {
        "app_logger": {
            "handlers": ["fileHandler"],
            "level": "DEBUG"
        },
        "app_mod_logger": {
            "handlers": ["fileHandler"],
            "level": "DEBUG"
        }
    },
    "formatters": {
        "myFormatter": {
            "format": "%(asctime)s - %(name)s %(levelname)s %(message)s"
        }
    }

}

if __name__ == "__main__":
    logging.config.dictConfig(dictConfiguration)