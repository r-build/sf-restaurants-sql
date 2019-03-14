# Part 1: Essentials


def business_ids_count():
    """
    Write a SQL query that finds the number of business ids in the
    businesses table
    :return: a string representing the SQL query
    :rtype: str
    """
    sqlite_query = 'SELECT COUNT(business_id) FROM businesses'
    return sqlite_query


def unique_business_names_count():
    """
    Write a SQL query that finds out how many unique business names
    are registered
    with San Francisco Food health investigation organization
    and name the column as unique restaurant name count.
    :return: a string representing the SQL query
    :rtype: str
    """

    # the question assumes all businesses are reg. w San Francisco,
    # so you don't have to worry about the (very) dirty city name data!
    sqlite_query = """
    SELECT
    COUNT(DISTINCT(name)) as "unique resturant name count" FROM businesses
    """
    return sqlite_query


def first_and_last_investigation():
    """
    Write a SQL query that finds out what is the earliest and latest date
    a health investigation is recorded in this database.
    :return: a string representing the SQL query
    :rtype: str
    """

    sqlite_query = 'SELECT MIN(date), MAX(date) FROM inspections'
    return sqlite_query


def business_local_owner_count():
    """
    How many businesses are there in San Francisco where their owners live
    in the same area (postal code/ zip code) as the business is located?
    :return: a string representing the SQL query
    :rtype: str
    """

    sqlite_query = """
    SELECT COUNT(business_id) from businesses WHERE postal_code = owner_zip
    """
    return sqlite_query


def business_local_owner_reg_count():
    """
    Out of those businesses, how many of them has a registered business
    certificate?
    :return: a string representing the SQL query
    :rtype: str
    """

    sqlite_query = """
    SELECT COUNT(business_id) FROM businesses WHERE
    (postal_code = owner_zip) AND (business_certificate <> 'none')
    """
    return sqlite_query
