# Config Reader

A Python module for reading configuration files in `.yaml`, `.cfg`, and `.conf` formats. It converts configuration data into a flat dictionary, writes the data to `.env` and `.json` files, and sets environment variables.


### Installation

Follow these steps to set up and run the project:

## SetUp Virtual Environment and Clone the Project

```bash
#Create virtual environment
virtualenv sacvenv

#Activate virtualenv
source sacvenv/bin/activate


#Clone the repository from GitHub:
git clone https://github.com/GudeKumarReddy/sac_manager.git


#install dependencies
pip install -r requirements.txt


#Install the package locally:
pip install .

## Run Tests with Coverage Report in HTML
pytest --cov=config_reader --cov-report=html

Open htmlcov/index.html in a web browser.

This process will give you a detailed HTML report with coverage statistics, including which lines of code are covered and which are not.


