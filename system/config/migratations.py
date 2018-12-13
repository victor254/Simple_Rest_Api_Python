import appconfig

DB_NAME  = appconfig.config['database']['database']

TABLES = {}

TABLES['api_keys'] = (
      "CREATE TABLE `api_key
