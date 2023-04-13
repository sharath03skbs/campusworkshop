"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq4e02qv2dcb92obt0-a.oregon-postgres.render.com",
        database="todo_v7sh",
        user="root",
        password="qy1T7sA6pcHZLI9S3PBjuVaLrUHOfLhl")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
