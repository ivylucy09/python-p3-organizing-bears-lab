# lib/sql_queries.py

# 1. Select all female bears and return their names and ages
select_all_female_bears_return_name_and_age = """
    SELECT name, age
    FROM bears
    WHERE sex = 'F';
"""

select_all_bears_names_and_orders_in_alphabetical_order = """
    SELECT name
    FROM bears
    WHERE name IS NOT NULL
    ORDER BY name;
"""


# 3. Select the oldest bear's name and age
select_oldest_bear_return_name_and_age = """
    SELECT name, age
    FROM bears
    ORDER BY age DESC
    LIMIT 1;
"""

# 4. Select the youngest bear's name and age
select_youngest_bear_return_name_and_age = """
    SELECT name, age
    FROM bears
    ORDER BY age ASC
    LIMIT 1;
"""

# Add more queries here if needed for your specific tests
