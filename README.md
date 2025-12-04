# Data Extractor Project

This project extracts data from various sources, processes it, and displays it.

## Directory Structure & File Placement
Place your source files in the corresponding directories:

- **Excel Files**: `Data Collection/Files/` (e.g., `sample.xlsx`)
- **CSV Files**: `Data Collection/Files/` (e.g., `sample.csv`)
- **Text/Log Files**: `Data Collection/Files/` (e.g., `sample.log`)
- **JSON Files**: `Data Collection/Files/` (e.g., `sample.json`)
- **SQL Database**: `Data Collection/Database/` (e.g., `sample.db`)
- **Images**: `Data Collection/Multimedia/` (e.g., `sample.jpg`)
- **Audio**: `Data Collection/Multimedia/` (e.g., `sample.mp3`)
- **HTML for Scraping**: `Data Collection/web_scrapping/` (e.g., `index.html`)
- **Manual CSV**: `Data Collection/Manual/` (e.g., `manual.csv`)

## Setup
1. Activate virtual environment: `.\venv\Scripts\Activate`
2. Install requirements: `pip install -r requirements.txt`

## Usage
Run the main display script:
```bash
python display.py
```
Select the data source you want to view from the menu.

# Data Extraction Project Walkthrough

## Features Implemented
- **API**: Fetch weather data from Open-Meteo.
- **Manual**: Read manually entered CSV data.
- **Sensor**: Simulate accelerometer sensor data.
- **Web Scraping**: Scrape data from a local HTML file.
- **Files**: Read Excel, CSV, Text/Log, and JSON files.
- **Database**: Read from a SQLite database.
- **Multimedia**: Display images and play sound files.
- **IoT & Streaming**: Simulate IoT device data and continuous data streams.

## How to Use
1. **Navigate to the project directory**:
   \\\powershell
   cd 'C:\Users\KIIT0001\Desktop\College\Sem 6\ML\DataExtractorProject'
   \\\
2. **Activate the virtual environment**:
   \\\powershell
   .\venv\Scripts\Activate
   \\\
3. **Install dependencies**:
   \\\powershell
   pip install -r requirements.txt
   \\\
4. **Run the application**:
   \\\powershell
   python display.py
   \\\

## File Placement
Place your data files in the following directories:
- **Excel/CSV/JSON/Text**: \Data Collection/Files/\
- **Database**: \Data Collection/Database/\
- **Images/Audio**: \Data Collection/Multimedia/\
- **HTML**: \Data Collection/web_scrapping/\

## Verification Results
- **API**: Verified fetching weather data from Open-Meteo.
- **Imports**: Fixed \ModuleNotFoundError\ by adjusting \sys.path\ and imports in \display.py\.
- **Execution**: Successfully ran \display.py\ and interacted with the menu.

## How to Add Your Own Data
- **Files**: Place your \.csv\, \.xlsx\, \.txt\, or \.json\ files in \Data Collection/Files/\. The script will list them for you to select.
- **API**: Edit \Data Collection/API/apiretrieve.py\ and change the \API_URL\ variable.
- **Web Scraping**: Select option 4 and choose 'URL' to scrape a live website, or edit \Data Collection/web_scrapping/scrapingcode.py\ to change the CSS selector.
- **Sensor**: Run option 3 to generate and view sensor data.

