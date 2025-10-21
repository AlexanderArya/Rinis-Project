class Config:
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'  
    MYSQL_PORT = 3308
    MYSQL_PASSWORD = ''  
    MYSQL_DB = 'rinis_property_db'
    SECRET_KEY = 'yoursecretkey'  

    # Tambahin ini biar hasil SELECT jadi dict
    MYSQL_CURSORCLASS = 'DictCursor'

    # Google Drive API (tambahan)
    GOOGLE_DRIVE_CREDENTIALS = "credentials.json"  
    GOOGLE_DRIVE_FOLDER_ID = "1AbCdEfGh123456789"

    