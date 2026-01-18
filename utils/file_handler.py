def read_sales_data(filename):
    """
    Reads sales data from file handling encoding issues

    Returns: list of raw lines (strings)

    Expected Output Format:
    ['T001|2024-12-01|P101|Laptop|2|45000|C001|North', ...]

    Requirements:
    - Use 'with' statement
    - Handle different encodings (try 'utf-8', 'latin-1', 'cp1252')
    - Handle FileNotFoundError with appropriate error message
    - Skip the header row
    - Remove empty lines
    """

def parse_transactions(raw_lines):
    """
    Parses raw lines into clean list of dictionaries

    Returns: list of dictionaries with keys:
    ['TransactionID', 'Date', 'ProductID', 'ProductName',
     'Quantity', 'UnitPrice', 'CustomerID', 'Region']

    Expected Output Format:
    [
        {
            'TransactionID': 'T001',
            'Date': '2024-12-01',
            'ProductID': 'P101',
            'ProductName': 'Laptop',
            'Quantity': 2,           # int type
            'UnitPrice': 45000.0,    # float type
            'CustomerID': 'C001',
            'Region': 'North'
        },
        ...
    ]

    Requirements:
    - Split by pipe delimiter '|'
    - Handle commas within ProductName (remove or replace)
    - Remove commas from numeric fields and convert to proper types
    - Convert Quantity to int
    - Convert UnitPrice to float
    - Skip rows with incorrect number of fields
    """

def validate_and_filter(transactions, region=None, min_amount=None, max_amount=None):
    """
    Validates transactions and applies optional filters

    Parameters:
    - transactions: list of transaction dictionaries
    - region: filter by specific region (optional)
    - min_amount: minimum transaction amount (Quantity * UnitPrice) (optional)
    - max_amount: maximum transaction amount (optional)

    Returns: tuple (valid_transactions, invalid_count, filter_summary)

    Expected Output Format:
    (
        [list of valid filtered transactions],
        5,  # count of invalid transactions
        {
            'total_input': 100,
            'invalid': 5,
            'filtered_by_region': 20,
            'filtered_by_amount': 10,
            'final_count': 65
        }
    )

    Validation Rules:
    - Quantity must be > 0
    - UnitPrice must be > 0
    - All required fields must be present
    - TransactionID must start with 'T'
    - ProductID must start with 'P'
    - CustomerID must start with 'C'

    Filter Display:
    - Print available regions to user before filtering
    - Print transaction amount range (min/max) to user
    - Show count of records after each filter applied
    """

