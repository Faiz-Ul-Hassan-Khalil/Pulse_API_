"""
Database connection setup for PulseAPI.

Creates the SQLAlchemy engine and session factory that the rest
of the application uses to talk to PostgreSQL.
"""

import os  # os is used to access environment variables, it exactly refers to the operating system's environment variables
from dotenv import load_dotenv # load_dotenv is used to load environment variables from a .env file into the operating system's environment variables
from sqlalchemy import create_engine # create_engine is used to create a new SQLAlchemy engine instance that will be used to connect to the PostgreSQL database
from sqlalchemy.orm import sessionmaker, DeclarativeBase # sessionmaker is used to create a new SQLAlchemy session factory that will be used to create new database sessions

load_dotenv() # Load environment variables from a .env file into the operating system's environment variables

DATABASE_URL = os.getenv("DATABASE_URL") # Get the database URL from the environment variables. This URL is used to connect to the PostgreSQL database.

if not DATABASE_URL:  # If the DATABASE_URL environment variable is not set, raise a ValueError with a message indicating that the .env file may be missing or misconfigured.
    
    raise ValueError(  
        "DATABASE_URL environment variable is not set. "
        "Make sure your .env file exists and contains DATABASE_URL."
    )

engine = create_engine(DATABASE_URL) # Create a new SQLAlchemy engine instance using the database URL. This engine will be used to connect to the PostgreSQL database.

SessionLocal = sessionmaker(bind=engine) # Create a new SQLAlchemy session factory that is bound to the engine. This session factory will be used to create new database sessions.


class Base(DeclarativeBase):
    """
    Base class for all database models.
    Every table definition will inherit from this.
    """
    pass