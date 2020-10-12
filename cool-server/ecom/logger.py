import os
from logging.config import dictConfig


def setup_logging():
    package_name = __name__.split('.')[0]
    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s [%(levelname)s] '
                          '[%(name)s:%(lineno)s - %(funcName)s()] '
                          '%(message)s'
            },
        },
        'handlers': {
            'default': {
                'level': 'INFO',
                'formatter': 'standard',
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            '': {
                'handlers': ['default'],
                'level': 'WARNING',
                'propagate': True
            },
            package_name: {
                'handlers': ['default'],
                'level': os.environ.get(
                    '%s_LOG_LEVEL' % (package_name.upper()),
                    'INFO'),
                'propagate': False
            },
        }
    }

    dictConfig(logging_config)
