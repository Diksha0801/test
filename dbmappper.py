import sqlalchemy as DB
from sqlalchemy.orm import sessionmaker


class DbEngine:
    dbengine = "postgresql"
    user = "postgres"
    password = "docker"
    host = "127.0.0.1"
    port = "5432"
    database = "postgres"
    uri = "{}://{}:{}@{}:{}/{}".format(dbengine, user, password, host, port, database )

    try:
        engine = DB.create_engine(uri)
        session = sessionmaker(bind=engine)
        DB.echo = False  # Try changing this to True and see what happens
    except Exception:
        print("Unable to connect to database")


