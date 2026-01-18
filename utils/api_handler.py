def fetch_all_products():
    """
    Fetches all products from DummyJSON API

    Returns: list of product dictionaries

    Expected Output Format:
    [
        {
            'id': 1,
            'title': 'iPhone 9',
            'category': 'smartphones',
            'brand': 'Apple',
            'price': 549,
            'rating': 4.69
        },
        ...
    ]

    Requirements:
    - Fetch all available products (use limit=100)
    - Handle connection errors with try-except
    - Return empty list if API fails
    - Print status message (success/failure)
    """

def create_product_mapping(api_products):
    """
    Creates a mapping of product IDs to product info

    Parameters: api_products from fetch_all_products()

    Returns: dictionary mapping product IDs to info

    Expected Output Format:
    {
        1: {'title': 'iPhone 9', 'category': 'smartphones', 'brand': 'Apple', 'rating': 4.69},
        2: {'title': 'iPhone X', 'category': 'smartphones', 'brand': 'Apple', 'rating': 4.44},
        ...
    }
    """

def enrich_sales_data(transactions, product_mapping):
    """
    Enriches transaction data with API product information

    Parameters:
    - transactions: list of transaction dictionaries
    - product_mapping: dictionary from create_product_mapping()

    Returns: list of enriched transaction dictionaries

    Expected Output Format (each transaction):
    {
        'TransactionID': 'T001',
        'Date': '2024-12-01',
        'ProductID': 'P101',
        'ProductName': 'Laptop',
        'Quantity': 2,
        'UnitPrice': 45000.0,
        'CustomerID': 'C001',
        'Region': 'North',
        # NEW FIELDS ADDED FROM API:
        'API_Category': 'laptops',
        'API_Brand': 'Apple',
        'API_Rating': 4.7,
        'API_Match': True  # True if enrichment successful, False otherwise
    }

    Enrichment Logic:
    - Extract numeric ID from ProductID (P101 → 101, P5 → 5)
    - If ID exists in product_mapping, add API fields
    - If ID doesn't exist, set API_Match to False and other fields to None
    - Handle all errors gracefully

    File Output:
    - Save enriched data to 'data/enriched_sales_data.txt'
    - Use same pipe-delimited format
    - Include new columns in header
    """

def save_enriched_data(enriched_transactions, filename='data/enriched_sales_data.txt'):
    """
    Saves enriched transactions back to file

    Expected File Format:
    TransactionID|Date|ProductID|ProductName|Quantity|UnitPrice|CustomerID|Region|API_Category|API_Brand|API_Rating|API_Match
    T001|2024-12-01|P101|Laptop|2|45000.0|C001|North|laptops|Apple|4.7|True
    ...

    Requirements:
    - Create output file with all original + new fields
    - Use pipe delimiter
    - Handle None values appropriately
    """

