import re

def col_check(col_type):
    print(col_type)
    if 'varchar2' in col_type.lower():
        sqlalchemy_type = f"db.String({int(col_type.split('(')[1].split(')')[0])})"
    elif 'number' in col_type.lower():
        if '(' in col_type:
            length = int(col_type.split('(')[1].split(')')[0])
            if ',' in col_type:
                decimal_places = int(col_type.split(',')[1])
                sqlalchemy_type = f"db.Numeric({length}, {decimal_places})"
            else:
                sqlalchemy_type = f"db.Integer({length})"
        else:
            sqlalchemy_type = "db.Integer"
    elif 'date' in col_type.lower():
        sqlalchemy_type = "db.Date()"
    else:
        sqlalchemy_type = ""  # default type
    return sqlalchemy_type

# Open the input file
with open('input.txt', 'r') as f:

    # Read the file content
    content = f.read()

    # Find all the column names and types using regex
    pattern = r'(\w+)\s+((?:NOT NULL\s+)?\w+\(.*?\))(?:\s+|$)'
    matches = re.findall(pattern, content)

    # Generate the column definitions
    columns = []
    for match in matches:
        col_name = match[0]
        col_type = match[1]
        nullable = 'False' if 'NOT NULL' in col_type else 'True'
        # col_def = f"{col_name.lower()} = db.column('{col_name}', db.{col_type.split('(')[0]}, nullable={nullable})"
        col_def = f"{col_name.lower()} = db.column('{col_name}', {col_check(col_type)}, nullable={nullable})"
        columns.append(col_def)

    # Print the column definitions
    for col in columns:
        print(col)
