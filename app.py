import streamlit as st
import pandas as pd
import os
import importlib.util
from selenium import webdriver

# Dynamically import StocksScraper from '02. restructured-stocks-scraper.py'
spec = importlib.util.spec_from_file_location("StocksScraperModule", "02. restructured-stocks-scraper.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
StocksScraper = module.StocksScraper

st.set_page_config(page_title="StockBite - Yahoo Finance Scraper", layout="wide")
st.title("StockBite: Yahoo Finance Most Active Stocks Scraper")

st.write("""
This app scrapes the most active stocks from Yahoo Finance and lets you download the data as an Excel file.
""")

if 'data' not in st.session_state:
    st.session_state['data'] = None
if 'excel_file' not in st.session_state:
    st.session_state['excel_file'] = None

scrape = st.button("Scrape Most Active Stocks")

if scrape:
    st.info("Launching browser and starting scraping. Please wait...")
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        url = "https://finance.yahoo.com/"
        scraper = StocksScraper(driver, 5)
        scraper.access_url(url)
        scraper.access_most_active_stocks()
        scraper.extract_stocks_data()
        filename = "yahoo_finance-stocks"
        scraper.clean_and_save_data(filename)
        driver.quit()
        st.session_state['data'] = pd.read_excel(f"{filename}.xlsx")
        st.session_state['excel_file'] = f"{filename}.xlsx"
        st.success("Scraping complete!")
    except Exception as e:
        st.error(f"Error during scraping: {e}")
        try:
            driver.quit()
        except:
            pass

if st.session_state['data'] is not None:
    st.subheader("Scraped Data")
    st.dataframe(st.session_state['data'])
    with open(st.session_state['excel_file'], "rb") as f:
        st.download_button(
            label="Download Excel File",
            data=f,
            file_name=os.path.basename(st.session_state['excel_file']),
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        ) 