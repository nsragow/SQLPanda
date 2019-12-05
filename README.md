
# SQLPanda

If you want to read an sqlite file with a pandas dataframe in two lines of python this is the package for you.

### From the documentation: 

Wraps SQLite3 instance to streamline the SQL query to Pandas DataFrame process.

Any DataFrames produced by this object are detached from the sqlite database (so
mutating the df's will not have an effect on the source table)

Warning: Can be slow with large database files. In such a case use the _lite_load_
method inplace of the _load_ method.


    Setup:

        from SQLPanda import load

        sdf = load("data.sqlite")
        #where data.splite is the SQLite DB file
