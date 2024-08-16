# Credit Ratings Scraper

This project scrapes the credit ratings of corporations from [Wikirating](https://www.wikirating.com/list-of-corporations-by-credit-rating/) and stores the data in a CSV file.

## Files
- `scraping_script.py`: Python script to scrape data from the website and store it in `credit_ratings.csv`.
- `credit_ratings.csv`: Contains the scraped data including ID, Corporate, Headquarter, Credit Ratings, and more.

## Requirements
- Python 3.x
- Libraries:
  - pandas
  - requests
  - BeautifulSoup

## How to Use
1. Run the `scraping_script.py` to scrape the latest data.
2. The data will be stored in `credit_ratings.csv`.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
