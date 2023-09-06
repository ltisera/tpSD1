
#modo = 'produccion'
modo = 'desarrollo'


def getConfigDB():
    configDB = {}
    if (modo == 'desarrollo'):
        configDB['host'] = 'localhost'
        configDB['user'] = 'root'
        configDB['port'] = '3306'       
        configDB['password'] = '1234'
        configDB['database'] = 'bdrecetas'
        configDB['auth_plugin']='mysql_native_password'
    print("===== CONFIGURACION DE BASE DE DATOS (REVISAR QUE SEAN LOS LOCALES) =====")
    print(configDB)
        
    return configDB