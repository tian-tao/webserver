import logging
import tornado
import tornado.template
import os
from tornado.options import define, options

import environment
import logconfig

from tornado_jinja2 import Jinja2Loader
import jinja2

path = lambda root, *a: os.path.join(root, *a)
ROOT = os.path.dirname(os.path.abspath(__file__))

define("port", default=8888, help="run on the given port", type=int)
define("config", default=None, help="tornado config file")
define("debug", default=False, help="debug mode")
tornado.options.parse_command_line()

MEDIA_ROOT = path(ROOT, "static")
TEMPLATE_ROOT = path(ROOT, "templates")

class DeploymentType:
    PRODUCTION = "PRODUCTION"
    DEV = "DEV"
    SOLO = "SOLO"
    STAGING = "STAGING"
    dict = {
        SOLO: 1,
        PRODUCTION: 2,
        DEV: 3,
        STAGING: 4
    }

if "DEPLOYMENT_TYPE" in os.environ:
    DEPLOYMENT = os.environ['DEPLOYMENT_TYPE'].upper()
else:
    DEPLOYMENT = DeploymentType.SOLO


jinja2_env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_ROOT), autoescape=False)
jinja2_loader = Jinja2Loader(jinja2_env)

settings = {}
settings['debug'] = DEPLOYMENT != DeploymentType.PRODUCTION or options.debug
settings['static_path'] = MEDIA_ROOT
settings['cookie_secret'] = "q1w2E#R$"
settings['xsrf_cookie'] = True
settings['template_loader'] = jinja2_loader

SYSLOG_TAG = "wechat_app_backend"
SYSLOG_FACILITY = logging.handlers.SysLogHandler.LOG_LOCAL2

LOGGERS = {
   'loggers': {
        SYSLOG_TAG: {},
    },
}

if settings['debug']:
    LOG_LEVEL = logging.DEBUG
else:
    LOG_LEVEL = logging.INFO
USE_SYSLOG = DEPLOYMENT != DeploymentType.SOLO

logconfig.initialize_logging(SYSLOG_TAG, SYSLOG_FACILITY, LOGGERS,
        LOG_LEVEL, USE_SYSLOG)

if options.config:
    tornado.options.parse_config_file(options.config)
