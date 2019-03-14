# Investigating San Francisco food health using SQL

This repository uses a relational dataset about food health investigations carried out in San Francisco and their outcomes.

The fictional scenario is a prospective new restaurant in San Francisco, wanting to find a good location. Criteria for our imaginary owner are:
 - staying away from big restaurant owners who own multiple restaurants.
 - picking an area that is trending (has a lot of restaurants).

The Jupyter notebook `sf_food_investigations_notebook.ipynb` goes through a series of SQL queries to find out the best area and answer these business intelligence questions.

The files `pt1_essentials.py`, `pt2_groupby.py`, and `pt3_subqueries_joins.py` implement the solutions from the notebook as python functions.

The database is stored in an sqlite database, `data/sfscores.sqlite`, and consists of *3 tables*.
The schemas are:
 - * `businesses` *: information relating to restaurant businesses
 - * `inspections` *: information about individual inspection events
 - * `violations` *: information about violation events

The queries increase in complexity. By the end, the focus will be on multipart business questions using multistep queries or multiple tables.

## businesses
```
CREATE TABLE businesses (
    business_id INTEGER NOT NULL,
    name VARCHAR(64),
    address VARCHAR(50),
    city VARCHAR(23),
    postal_code VARCHAR(9),
    latitude FLOAT,
    longitude FLOAT,
    phone_number BIGINT,
    "TaxCode" VARCHAR(4),
    business_certificate INTEGER,
    application_date DATE,
    owner_name VARCHAR(99),
    owner_address VARCHAR(74),
    owner_city VARCHAR(22),
    owner_state VARCHAR(14),
    owner_zip VARCHAR(15)
)
```

## violations
```
CREATE TABLE violations (
    business_id TEXT NOT NULL,
    date INTEGER NOT NULL,
    ViolationTypeID TEXT NOT NULL,
    risk_category TEXT NOT NULL,
    description TEXT NOT NULL
)
```

## inspections
```
CREATE TABLE inspections (
    business_id TEXT NOT NULL,
    Score INTEGER,
    date INTEGER NOT NULL,
    type VARCHAR (33) NOT NULL
)

```

# Requirements
To install using conda:
`conda create -n sfrestaurants-sql python=3 jupyter numpy pandas matplotlib seaborn ipython-sql`

Then, if not installed previously, 
`pip install "ipython-cypher==0.2.6"`

