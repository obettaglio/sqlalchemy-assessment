"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?

# There is no execution (e.g. ".all()", ".first()"), so the returned
# value will be an SQL query. It will look like:
#       SELECT *
#       FROM brands
#       WHERE name = 'Ford';

# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?

# An association table is a table created for the sole purpose of
# bridging the gap between two meaningful tables. It is used when
# a 'many to many' relationship does not have a clearly defined
# middle table. Association tables have no meaningful data other
# than the values that connect the outer two tables.


# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the ``id`` of "ram."
q1 = "SELECT * FROM brands WHERE brand_id = 'ram';"

# Get all models with the name "Corvette" and the brand_id "che."
q2 = "SELECT * FROM models WHERE name = 'Corvette' AND brand_id = 'che';"

# Get all models that are older than 1960.
q3 = "SELECT * FROM models WHERE year < 1960;"

# Get all brands that were founded after 1920.
q4 = "SELECT * FROM brands WHERE founded > 1920;"

# Get all models with names that begin with "Cor."
q5 = "SELECT * FROM models WHERE name LIKE 'Cor%';"

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = "SELECT * FROM brands WHERE founded = 1903 AND discontinued IS NULL;"

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = "SELECT * FROM brands WHERE founded < 1950 OR discontinued IS NOT NULL;"

# Get any model whose brand_id is not "for."
q8 = "SELECT * FROM models WHERE brand_id != 'for';"


# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    pass


def get_brands_summary():
    """Prints out each brand name and each model name with year for that brand
    using only ONE database query."""

    pass


def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    pass


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    pass
