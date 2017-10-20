# import default values from drupal8 engine (required)
from docker_console.web.engines.drupal8.conf.default import *

#################
# BASE SETTINGS #
#################

WEB = {
    'ENGINE': 'drupal8',
    'USE_CUSTOM_ENGINE': False, # True/False - useful when we have default and custom engine with the same name
    'APP_LOCATION': 'app',
    'APP_CONF_LOCATION': 'app_conf',
    'APP_DATA_LOCATION': 'app_data',
    'TMP_PATH': '/tmp'
}

DB = {
    'default': {
        'DRIVER': 'mysql',
        'HOST': 'mysql',
        'NAME': 'db',
        'USER': 'user',
        'PASS': 'pass',
        'ROOT_USER': 'root',
        'ROOT_PASS': '123',
        'DUMP_IMPORT_FILE': 'app_databases/database.sql.tar.gz',
        'DUMP_EXPORT_LOCATION': 'app_databases/',
    }
}

TESTS = {
    'IMAGES': {
        'selenium_image': ('selenium/standalone-chrome', None),
        'codecept_image': ('droptica/codecept', None)
    },
    'LOCATION': "tests"
}

ENV = None

####################
# DRUPAL8 SETTINGS #
####################

DEV_DOCKER_IMAGES = {
    'default': ('droptica/php-developer:con', './docker/Dockerfiles/dev'),
    'additional_images': [
#     ('vendor/image_name', None), # image from dockerhub
#     ('vendor/image_name', 'path_to_dockerfile') # custom image from Dockerfile
    ]
}

DRUPAL = {
    'default': {
        'ADMIN_USER': 'admin',
        'ADMIN_PASS': '123',
        'SITE_URI': 'con.dev',
        'SITE_DIRECTORY': 'default',
        'FILES_DST': 'sites/default/',
        'PRIVATE_FILES_DST': 'sites/default/',
        'FILES_ARCHIVE': 'app_files/files.tar.gz',
        'PRIVATE_FILES_ARCHIVE': 'app_files/private.tar.gz',
        'SETTINGS_TEMPLATE_SUBDIR': None,
        'STAGE_FILE_PROXY_URL': None
    }
}