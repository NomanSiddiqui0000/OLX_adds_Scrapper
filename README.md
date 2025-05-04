# OLX Scraper  

## Description  

This project is a **web scraper** built using **Scrapy** to extract listing details from the OLX Pakistan website. It collects key data such as **title, price, seller name, location, brand, condition, and description** from multiple pages.  

The scraper is designed to work for **any category** dynamically, allowing you to extract listings without being restricted to a specific category.  

## Table of Contents  
- [Description](#description)  
- [Features](#features)  
- [Prerequisites](#prerequisites)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Configuration](#configuration)  
- [Notes](#notes)  
- [License](#license)  
- [Author](#author)  

## Features  

- Extracts listing details such as **title, price, seller name, location, brand, and condition**.  
- Supports **pagination**, ensuring data is collected from multiple pages automatically.  
- Works **for any category**, not limited to a specific one.  
- Optimized for speed using Scrapy’s asynchronous request handling.  

## Prerequisites  

Ensure you have the following installed before running the scraper:  

- **Python** (>=3.7)  
- **Scrapy** (latest version)  

To install Scrapy, run:  

```bash
pip install scrapy
```

## Installation  

1. Clone this repository:  

    ```bash
    git clone https://github.com/NomanSiddiqui0000/OLX_adds_Scrapper
    ```

2. Navigate to the project directory:  

    ```bash
    cd olx-scraper
    ```

3. Install the required dependencies:  

    ```bash
    pip install scrapy
    pip install requests
    ```

## Usage  

1. Run the scraper with the following command:  

    ```bash
    scrapy crawl olx_scraper -o listings.csv
    ```

2. The data will be saved in a **CSV file** named `listings.csv`.  

## Configuration  

- To scrape a **specific category**, update the `start_urls` in `olx_spider.py`.  
- The **pagination** automatically follows the "Next" button, ensuring full coverage of listings.  

## Notes  

- The scraper is designed for **OLX Pakistan**, and structural changes to the site may require adjustments. 
- If the scraper stops working, check for **updated CSS selectors** and modify them accordingly.  

## License  

This project is licensed under the **MIT License**.  

## Author  

**Muhammad Noman**  
[GitHub Profile](https://github.com/NomanSiddiqui0000)
