def generate_sales_report(transactions, enriched_transactions, output_file='output/sales_report.txt'):
    """
    Generates a comprehensive formatted text report

    Report Must Include (in this order):

    1. HEADER
       - Report title
       - Generation date and time
       - Total records processed

    2. OVERALL SUMMARY
       - Total Revenue (formatted with commas)
       - Total Transactions
       - Average Order Value
       - Date Range of data

    3. REGION-WISE PERFORMANCE
       - Table showing each region with:
         * Total Sales Amount
         * Percentage of Total
         * Transaction Count
       - Sorted by sales amount descending

    4. TOP 5 PRODUCTS
       - Table with columns: Rank, Product Name, Quantity Sold, Revenue

    5. TOP 5 CUSTOMERS
       - Table with columns: Rank, Customer ID, Total Spent, Order Count

    6. DAILY SALES TREND
       - Table showing: Date, Revenue, Transactions, Unique Customers

    7. PRODUCT PERFORMANCE ANALYSIS
       - Best selling day
       - Low performing products (if any)
       - Average transaction value per region

    8. API ENRICHMENT SUMMARY
       - Total products enriched
       - Success rate percentage
       - List of products that couldn't be enriched

    Expected Output Format (sample):
    ============================================
           SALES ANALYTICS REPORT
         Generated: 2024-12-18 14:30:22
         Records Processed: 95
    ============================================

    OVERALL SUMMARY
    --------------------------------------------
    Total Revenue:        ₹15,45,000.00
    Total Transactions:   95
    Average Order Value:  ₹16,263.16
    Date Range:           2024-12-01 to 2024-12-31

    REGION-WISE PERFORMANCE
    --------------------------------------------
    Region    Sales         % of Total  Transactions
    North     ₹4,50,000     29.13%      25
    South     ₹3,80,000     24.60%      22
    ...

    (continue with all sections...)
    """

def main():
    """
    Main execution function

    Workflow:
    1. Print welcome message
    2. Read sales data file (handle encoding)
    3. Parse and clean transactions
    4. Display filter options to user
       - Show available regions
       - Show transaction amount range
       - Ask if user wants to filter (y/n)
    5. If yes, ask for filter criteria and apply
    6. Validate transactions
    7. Display validation summary
    8. Perform all data analyses (call all functions from Part 2)
    9. Fetch products from API
    10. Enrich sales data with API info
    11. Save enriched data to file
    12. Generate comprehensive report
    13. Print success message with file locations

    Error Handling:
    - Wrap entire process in try-except
    - Display user-friendly error messages
    - Don't let program crash on errors

    Expected Console Output:
    ========================================
    SALES ANALYTICS SYSTEM
    ========================================

    [1/10] Reading sales data...
    ✓ Successfully read 95 transactions

    [2/10] Parsing and cleaning data...
    ✓ Parsed 95 records

    [3/10] Filter Options Available:
    Regions: North, South, East, West
    Amount Range: ₹500 - ₹90,000

    Do you want to filter data? (y/n): n

    [4/10] Validating transactions...
    ✓ Valid: 92 | Invalid: 3

    [5/10] Analyzing sales data...
    ✓ Analysis complete

    [6/10] Fetching product data from API...
    ✓ Fetched 30 products

    [7/10] Enriching sales data...
    ✓ Enriched 85/92 transactions (92.4%)

    [8/10] Saving enriched data...
    ✓ Saved to: data/enriched_sales_data.txt

    [9/10] Generating report...
    ✓ Report saved to: output/sales_report.txt

    [10/10] Process Complete!
    ========================================
    """

if __name__ == "__main__":
    main()

