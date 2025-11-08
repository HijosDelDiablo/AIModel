# connection file

from mongoengine import connect, disconnect
from dotenv import load_dotenv
import os


class ConnectionMongoStandard:
    def __init__(self, db_name=None, host=None, port=None, username=None, password=None, auth_source=None):
        # Load environment variables
        load_dotenv()

        # Ensure any previous connections are closed
        disconnect()

        # Resolve values from arguments or environment (with safe defaults)
        db_name = db_name or os.getenv("DB_NAME")
        host = host or os.getenv("DB_HOST")
        port_env = port or os.getenv("DB_PORT")
        try:
            port = int(port_env)
        except (TypeError, ValueError):
            raise RuntimeError(f"DB_PORT inválido: {port_env}")

        username = username or os.getenv("MONGO_INITDB_ROOT_USERNAME")
        password = password or os.getenv("MONGO_INITDB_ROOT_PASSWORD")
        auth_source = auth_source or os.getenv("ME_CONFIG_BASICAUTH_USERNAME")

        # Connect to MongoDB
        self.connection = connect(
            db=str(db_name),
            host=str(host),
            port=port,
            username=username,
            password=password,
            authentication_source=auth_source,
        )

    def get_database(self):
        return self.connection
