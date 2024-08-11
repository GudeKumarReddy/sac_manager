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



## Module Overview

### `ConfigReader` Class

The `ConfigReader` class provides functionality for managing configuration files. It supports various formats and offers methods to handle configurations effectively.

1. **Class Definition**:
   - Handles reading configurations from `.yaml`, `.cfg`, and `.conf` files.
   - Converts configurations into a flat dictionary.
   - Provides methods to write configurations to `.env` and `.json` files or set them as environment variables.

2. **Initialization**:
   - Initializes with a file path and prepares an empty dictionary to store configuration data.

3. **Configuration Reading**:
   - **YAML Files**: Uses `pyyaml` to parse `.yaml` files and convert them into a flat dictionary.
   - **CFG Files**: Uses `configparser` to read `.cfg` files and flatten the configuration data.
   - **CONF Files**: Manually reads `.conf` files and flattens the configuration data.

4. **Flattening Dictionary**:
   - A private method that flattens nested dictionaries into a single-level dictionary with dot-separated keys.

5. **Write to `.env`**:
   - Writes the flat dictionary to a `.env` file with each key-value pair on a new line.

6. **Write to JSON**:
   - Writes the flat dictionary to a `.json` file with pretty formatting.

7. **Set Environment Variables**:
   - Converts all values in the dictionary to strings and sets them as environment variables using `os.environ`.

### Unit Tests

The module includes unit tests to ensure its functionality:

1. **Fixtures**:
   - Create temporary configuration files (`.yaml`, `.cfg`, `.conf`) for testing.

2. **Test Reading**:
   - Verify that configurations are read correctly from each file format and converted into the expected flat dictionary.

3. **Test Writing**:
   - Ensure that writing to `.env` and `.json` files produces the correct output.

4. **Test Environment Variables**:
   - Confirm that environment variables are set correctly from the configuration data.

This description outlines the core functionalities and testing aspects of the `ConfigReader` module, making it clear how the module operates and how it is validated.

