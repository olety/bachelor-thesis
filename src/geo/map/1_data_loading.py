con = sqlite3.connect(os.path.join('wdi', 'database.sqlite'))
df = pd.read_sql_query(
    'SELECT * FROM Country c '
    'INNER JOIN Indicators i ON c.CountryCode = i.CountryCode '
    'WHERE i.IndicatorCode="IT.CEL.SETS.P2"', con)
