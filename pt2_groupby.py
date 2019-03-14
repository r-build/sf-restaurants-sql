# Part 2: GROUP BY


def freq_risk_per_violation():
    """
    Returns the distribution of the risk exposure of all the violations
    reported in the database
    The first column of the result is 'risk_category' and the second
    column the count.
    :return: a string representing the SQL query
    :rtype: str
    """

    sqlite_query = """
    SELECT
        risk_category, COUNT(business_id) as "count"
    FROM
        violations
    GROUP BY
        risk_category
    """
    return sqlite_query


def freq_risk_per_violation_water():
    """
    Returns the distribution of the risk exposure of all the violations
    reported in the database that are *water related*, sorted by
    frequency from high to low.
    :return: a string representing the SQL query
    :rtype: str
    """

    sqlite_query = """
    SELECT
        risk_category, COUNT(business_id) as frequency
    FROM
        violations
    WHERE
        description LIKE '%water%'
    GROUP BY
        risk_category
    ORDER BY
        risk_category = 'Low Risk' DESC,
        risk_category = 'Moderate Risk' DESC,
        risk_category = 'High Risk' DESC
    """
    return sqlite_query


def frequency_of_inspections_types():
    """
    What types of inspections does the authorities conduct and how often do
    they occur in general?
    Returns the distribution of different types of inspections with their
    frequency (type, frequency), based on inspections records.
    Sorted in ascending order based on frequency.
    :return: a string representing the SQL query
    :rtype: str
    """

    sqlite_query = """
    SELECT
        type, COUNT(business_id) as frequency
    FROM
        inspections
    GROUP BY
        type
    ORDER BY
        frequency
    """
    return sqlite_query


def avg_score_by_inspection_type():
    """
    What is the average score given to restaurants based on the type of
    inspection?
    Based on the results, identify the types of inspections that are not
    scored (NULL).
    The 'average_score' is rounded to one decimal.
    The results are sorted in ascending order based on the average score.
    Uses the function ROUND(score, 1).
    :return: a string representing the SQL query
    :rtype: str
    """

    sqlite_query = """
    SELECT
        type, ROUND(AVG(score), 1) as "average score"
    FROM
        inspections
    WHERE
       score <> 'None'
    GROUP BY
        type
    ORDER BY
        "average score"
    """
    return sqlite_query


def owner_per_restaurant_count():
    """
    Finds the restaurant owners (owner_name) that own the most restaurants,
    and the number of restaurants (num_restaurants) they own.
    Returns the top 10 owners, ordered by descending order using the
    number of restaurants.
    :return: a string representing the SQL query
    :rtype: str
    """

    sqlite_query = """
    SELECT
        owner_name, COUNT(business_id) as "num_restaurants"
    FROM
        businesses
    GROUP BY
        owner_name
    ORDER BY
        num_restaurants DESC
    LIMIT 10
    """
    return sqlite_query
