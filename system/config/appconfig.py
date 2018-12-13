config ={}
config['database'] = {
    'user':'root',
    'password':'shithappens',
    'database':'demosacco',
    'host':'localhost',
    'port':'3306',
    'autocommit':False,
##    'dictrows':dict(),
##    'charset':'utf-8',
##    'timezone':None,
    'raise_on_warnings':False
    }
config['server'] = {
    'host':'localhost',
    'port':'8000',
    'debug':True
    }
config['auth_method'] = 'basic'
config['enable_api_keys'] = True
config['api_users'] = {'username':'admin','password':'shithappens'}
config['format'] = 'json'
config['log'] = True
    
