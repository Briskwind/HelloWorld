from HelloWorld.settings import BASE_DIR

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'first_formatter': {
            'format': '%(levelname)s [%(asctime)s] [%(name)s:%(module)s:%(funcName)s:%(lineno)s] [%(exc_info)s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'filters': {
        # 对 DEBUG 参数情况设置时触发
        'DebugFalse': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'DebugTrue': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {

        'console': {
            'level': 'DEBUG',
            'filters': ['DebugTrue'],
            'class': 'logging.StreamHandler',
            'formatter': 'first_formatter'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': '{0}/logs/request.log'.format(BASE_DIR),
            'formatter': 'first_formatter',
            'when': 'midnight'
        },

        'admin_log': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': '{0}/logs/admin_log.log'.format(BASE_DIR),
            'formatter': 'first_formatter',
            'when': 'midnight'
        },
        'request_error': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': '{0}/logs/request_error.log'.format(BASE_DIR),
            'formatter': 'first_formatter',
            'when': 'midnight'
        }
        ,
        'db': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': '{0}/logs/db.log'.format(BASE_DIR),
            'formatter': 'first_formatter',
            'when': 'midnight'
        },

    },
    'loggers': {
        # 记录请求过对url
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False,
        },

        # 记录500、400错误信息
        'django.request': {
            'handlers': ['request_error'],
            'level': 'DEBUG',
            'propagate': False,
        },

        # mysql相关操作
        # 'django.db': {
        #     'handlers': ['console','db'],
        #     'level': 'DEBUG',
        #     'propagate': False,
        # },

        # 作为管理员记录自定义请求参数日志
        'admin_log': {
            'handlers': ['console', 'admin_log'],
            'level': 'DEBUG',
            'propagate': False,
        }
    }
}
