import mysql.connector


def get_connection():
    connection=mysql.connector.connect(
        host='yh-db.clidqfc4u35c.ap-northeast-2.rds.amazonaws.com',
        database = 'streamlit_db',
        user = 'python_user',
        password = '2105'
    )
    return connection