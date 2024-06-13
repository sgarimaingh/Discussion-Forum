import os
from peewee import PostgresqlDatabase
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

DATABASE_URL = os.getenv("DATABASE_URL")

import urllib.parse as urlparse
urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(DATABASE_URL)

db = PostgresqlDatabase(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)
