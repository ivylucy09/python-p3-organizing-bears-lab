# lib/testing/select_test.py

import sqlite3
import pytest
from sql_queries import (
    select_all_female_bears_return_name_and_age,
    select_all_bears_names_and_orders_in_alphabetical_order,
    select_oldest_bear_return_name_and_age,
    select_youngest_bear_return_name_and_age
)

# Setup in-memory database for testing
@pytest.fixture(scope='module')
def connection():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    
    # Read and execute the seed SQL file (assuming lib/seed.sql exists and seeds data)
    with open("lib/seed.sql") as f:
        cursor.executescript(f.read())
    
    yield connection
    connection.close()

def test_select_all_female_bears_return_name_and_age(connection):
    cursor = connection.cursor()
    result = cursor.execute(select_all_female_bears_return_name_and_age).fetchall()
    assert len(result) > 0  # Ensure that there are results
    assert all([row[0] and row[1] for row in result])  # Check if name and age are returned

def test_select_all_bears_names_and_orders_in_alphabetical_order(connection):
    cursor = connection.cursor()
    result = cursor.execute(select_all_bears_names_and_orders_in_alphabetical_order).fetchall()
    assert result == sorted(result)  # Ensure the result is in alphabetical order

def test_select_oldest_bear_return_name_and_age(connection):
    cursor = connection.cursor()
    result = cursor.execute(select_oldest_bear_return_name_and_age).fetchone()
    assert result  # Ensure a result is returned
    assert isinstance(result[1], int)  # Age should be an integer

def test_select_youngest_bear_return_name_and_age(connection):
    cursor = connection.cursor()
    result = cursor.execute(select_youngest_bear_return_name_and_age).fetchone()
    assert result  # Ensure a result is returned
    assert isinstance(result[1], int)  # Age should be an integer
