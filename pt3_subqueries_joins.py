# Part 3: Subqueries & Joins


def top_postcodes_for_chain_stores():
    """
    From the businesses table, selects the top 10 most popular postal_codes.
    They are filtered to only count the restaurants owned by
    people/entities that own 5 or more restaurants.
    The result returns a row (postal_code, frequency) for each 10 selections,
    sorted by descending order to get the most relevant zip codes
    :return: a string representing the SQL query
    :rtype: str
    """

    sqlite_query = """
    SELECT
        b1.postal_code, COUNT(b1.business_id) as "count"
    FROM
        businesses as b1
    WHERE
        b1.owner_name IN
    (
    SELECT
        b2.owner_name
    FROM
        businesses as b2
    GROUP BY
        b2.owner_name
    HAVING COUNT(b2.business_id) > 4
    )
    GROUP BY
        b1.postal_code
    ORDER BY
        count DESC
    LIMIT 10
    """
    return sqlite_query


def inspection_scores_in_94103():
    """
    Let's get an idea about the inspection score our competition has.
    Based on multiple inspections, this gives the minimum Score ("min_score"),
    average Score ("avg_score"), and maximum Score ("max_score"), for
    all restaurant in post code "94103".
    The average score is rounded to one decimal.
    :return: a string representing the SQL query
    :rtype: str
    """

    sqlite_query = """
    SELECT
        min(score) as "min_score"
        , round(avg(score), 1) as "avg_score"
        , max(score) as "max_score"
    FROM
        inspections
    WHERE
        business_id IN
        (select business_id from businesses where postal_code = '94103')
    AND
        score <> 'None'
    """
    return sqlite_query


def risk_categories_in_94103():
    """
    How many times restaurants in Market street (postal_code: 94103)
    have committed health violations?
    Group them based on their risk category.
    The output is (risk_category, count as frequency) sorted
    in descending order by frequency
    :return: a string representing the SQL query
    :rtype: str
    """

    sqlite_query = """
    SELECT
        risk_category, COUNT(v.business_id) as "frequency"
    FROM
        violations as v
    INNER JOIN
        businesses as b
    ON
        v.business_id = b.business_id 
    
    WHERE (postal_code = '94103')
    GROUP BY
        risk_category
    ORDER BY
        frequency DESC
    """
    return sqlite_query


