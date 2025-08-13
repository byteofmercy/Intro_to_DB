#!/usr/bin/env python3
"""
MySQLServer.py
Creates the database 'alx_book_store' on the local MySQL server.
"""

import os
import mysql.connector
from mysql.connector import Error

def create_database():
    # Read creds from environment (safe). Defaults: user=root, no password, host=localhost
    user = os.environ.get('MYSQL_USER', 'root')
    password = os.environ.get('MYSQL_PASSWORD', '')
    host = os.environ.get('MYSQL_HOST', 'localhost')

    connection = None
    cursor = None
    try:
        # open connection
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # create database, do not fail if it already exists
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        # print a friendly error if we cannot connect or something goes wrong
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # close cursor and connection so we tidy up after playtime
        if cursor is not None:
            try:
                cursor.close()
            except Exception:
                pass
        if connection is not None and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
