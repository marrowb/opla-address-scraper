# OPLA Office Address Scraper

A Python script that scrapes contact information for U.S. Immigration and Customs Enforcement (ICE) Office of the Principal Legal Advisor (OPLA) field offices from the official ICE website.

## Why?
Immigration lawyers need to file a Certificate of Service with their court filings indicating they've also sent the documents to ICE OPLA. These addresses make it easier to generate the Certificate of Service without having to look up the address.


## Requirements

```bash
pip install requests beautifulsoup4
```

## Usage

```bash
python opla_scraper.py
```

The script will:
1. Scrape all 4 pages of OPLA office listings from the ICE website
2. Extract and structure the office information
3. Save the results to `opla_office_addresses.json`
4. Launch an interactive IPython session for data exploration

## Output Format

The script generates a JSON file with the following structure:

```json
[
  {
    "locality": "Office City",
    "name": "Full Office Name", 
    "address_line_1": "Street Address",
    "suite": "Suite/Floor Info",
    "city_state_zip": "City, State ZIP"
  },
  {
    "locality": "Another City",
    "name": "Another Office Name",
    "address_line_1": "Street Address", 
    "city_state_zip": "City, State ZIP"
  }
]
```

**Note:** Offices with mailing addresses include a separate `suite` field, while offices with standard addresses combine city, state, and ZIP into a single `city_state_zip` field.

## Data Source

All data is scraped from the official ICE website: https://www.ice.gov/contact/field-offices

The script specifically targets OPLA offices (office type 12) across all states and territories.

## Legal Notice

This script is for educational and informational purposes only. The data scraped belongs to the U.S. Department of Homeland Security and is publicly available on their official website. Users should verify current contact information directly with ICE before taking any legal action.

## Contributing

Feel free to submit issues or pull requests if you find bugs or have suggestions for improvements.
