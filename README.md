# StockBite

## Project Overview
StockBite is a real-time stock market data extraction tool that scrapes the most active stocks from Yahoo Finance. It automates browser actions using Selenium, parses and structures financial data with Pandas and NumPy, and provides an interactive Streamlit front end for easy access and export of data to Excel.

## Features
- Automated scraping of Yahoo Finance's most active stocks
- Handles dynamic content and multi-page navigation
- Parses and cleans financial data into structured datasets
- Interactive Streamlit web interface
- Downloadable Excel reports for further analysis

## Tech Stack
- Python
- Selenium
- Pandas
- NumPy
- OpenPyXL
- Streamlit

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/SagarNikam09/StockBite
   cd StockBite
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On macOS/Linux
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Ensure you have Chrome and ChromeDriver installed and available in your PATH.**

## Usage
### Run the Streamlit App
```bash
streamlit run app.py
```
- Click the "Scrape Most Active Stocks" button to start scraping.
- View the scraped data in the app and download it as an Excel file.

### Run the Scraper Script Directly
You can also run the scraper script without the UI:
```bash
python "02. restructured-stocks-scraper.py"
```

## Notes
- Selenium requires Chrome and ChromeDriver. Make sure both are installed and compatible with your Chrome version.
- The scraper automates a real browser session; scraping may take a few moments depending on your connection and system.
- The Excel file will be saved in the project directory.
