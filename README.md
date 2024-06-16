# UEFA Euro Match Predictor

This project is a comprehensive tool for analyzing past UEFA European Championship results, extracting current tournament tables, and predicting future match outcomes using statistical models.

## Table of Contents
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
  - [1. Extracting Past Results](#1-extracting-past-results)
  - [2. Getting Current Tables](#2-getting-current-tables)
  - [3. Predicting Match Outcomes](#3-predicting-match-outcomes)
- [Data Sources](#data-sources)
- [License](#license)

## Project Structure

The project consists of the following main components:

1. `get_pastresults.py`: A script to scrape historical match data from Wikipedia.
2. `get_tables.ipynb`: A Jupyter notebook to extract the current tournament tables from Wikipedia.
3. `predict_euros.ipynb`: A Jupyter notebook to predict the outcomes of future matches based on historical data.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/uefa-euro-match-predictor.git
    cd uefa-euro-match-predictor
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure you have Jupyter installed to run the notebooks:
    ```bash
    pip install notebook
    ```

## Usage

### 1. Extracting Past Results

The `get_pastresults.py` script scrapes historical match data from Wikipedia for the UEFA European Championships from 1980 to 2020.

#### Running the Script

```bash
python get_pastresults.py

This script will fetch data and save it in a structured format (e.g., CSV or DataFrame).

### 2. Getting Current Tables

The `get_tables.ipynb` notebook extracts the current tournament tables from the Wikipedia page of UEFA Euro 2024.

#### Running the Notebook
Open the notebook:
```bash
jupyter notebook get_tables.ipynb

Run all cells to fetch and process the current tables.

### 3. Predicting Match Outcomes

The `predict_euros.ipynb` notebook uses historical data and statistical models to predict the outcomes of future matches.

#### Running the Notebook
Open the notebook:
````bash
jupyter notebook predict_euros.ipynb

Run all cells to load data, train the prediction model, and output the predictions.

## Data Sources

- Historical match data: Wikipedia pages of past UEFA European Championships.
- Current tournament tables: Wikipedia page of UEFA Euro 2024.
