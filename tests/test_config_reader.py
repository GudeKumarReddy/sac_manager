import pytest
import os
import json

from config_reader.config_reader import ConfigReader

YAML_CONTENT = """
database:
  host: localhost
  port: 5432
  user: admin
  password: secret

logging:
  level: DEBUG
  file: app.log
"""

CFG_CONTENT = """
[database]
host = localhost
port = 5432
user = admin
password = secret

[logging]
level = DEBUG
file = app.log
"""

CONF_CONTENT = """
database.host=localhost
database.port=5432
database.user=admin
database.password=secret

logging.level=DEBUG
logging.file=app.log
"""

@pytest.fixture
def yaml_file(tmp_path):
    d = tmp_path / "config.yaml"
    d.write_text(YAML_CONTENT)
    return d

@pytest.fixture
def cfg_file(tmp_path):
    d = tmp_path / "config.cfg"
    d.write_text(CFG_CONTENT)
    return d

@pytest.fixture
def conf_file(tmp_path):
    d = tmp_path / "config.conf"
    d.write_text(CONF_CONTENT)
    return d

def test_read_yaml(yaml_file):
    reader = ConfigReader(yaml_file)
    reader.read_config()
    expected = {
        'database.host': 'localhost',
        'database.port': 5432,
        'database.user': 'admin',
        'database.password': 'secret',
        'logging.level': 'DEBUG',
        'logging.file': 'app.log'
    }
    print(f"YAML Config Dict: {reader.config_dict}")
    assert reader.config_dict == expected

def test_read_cfg(cfg_file):
    reader = ConfigReader(cfg_file)
    reader.read_config()
    expected = {
        'database.host': 'localhost',
        'database.port': '5432',
        'database.user': 'admin',
        'database.password': 'secret',
        'logging.level': 'DEBUG',
        'logging.file': 'app.log'
    }
    print(f"CFG Config Dict1: {reader.config_dict}")
    assert reader.config_dict == expected

def test_read_conf(conf_file):
    reader = ConfigReader(conf_file)
    reader.read_config()
    expected = {
        'database.host': 'localhost',
        'database.port': '5432',
        'database.user': 'admin',
        'database.password': 'secret',
        'logging.level': 'DEBUG',
        'logging.file': 'app.log'
    }
    print(f"CONF Config Dict2: {reader.config_dict}")
    assert reader.config_dict == expected

def test_write_to_env(tmp_path, conf_file):
    reader = ConfigReader(conf_file)
    reader.read_config()
    env_file = tmp_path / ".env"
    reader.write_to_env(env_file)
    with open(env_file) as f:
        content = f.read()
    assert 'database.host=localhost' in content
    assert 'logging.file=app.log' in content

def test_write_to_json(tmp_path, conf_file):
    reader = ConfigReader(conf_file)
    reader.read_config()
    json_file = tmp_path / "config.json"
    reader.write_to_json(json_file)
    with open(json_file) as f:
        content = json.load(f)
    assert content['database.host'] == 'localhost'
    assert content['logging.file'] == 'app.log'

def test_set_os_env(conf_file):
    reader = ConfigReader(conf_file)
    reader.read_config()
    reader.set_os_env()
    assert os.getenv('database.host') == 'localhost'
    assert os.getenv('logging.file') == 'app.log'





# from config_reader.config_reader import ConfigReader
#
# # Test .yaml file
# yaml_reader = ConfigReader('config.yaml')
# yaml_reader.read_config()
# print("YAML Config Dictionary:")
# print(yaml_reader.config_dict)
# yaml_reader.write_to_env('.env.yaml')
# yaml_reader.write_to_json('config.yaml.json')
# yaml_reader.set_os_env()
#
# # Test .cfg file
# cfg_reader = ConfigReader('config.cfg')
# cfg_reader.read_config()
# print("CFG Config Dictionary:")
# print(cfg_reader.config_dict)
# cfg_reader.write_to_env('.env.cfg')
# cfg_reader.write_to_json('config.cfg.json')
# cfg_reader.set_os_env()
#
# # Test .conf file
# conf_reader = ConfigReader('config.conf')
# conf_reader.read_config()
# print("CONF Config Dictionary:")
# print(conf_reader.config_dict)
# conf_reader.write_to_env('.env.conf')
# conf_reader.write_to_json('config.conf.json')
# conf_reader.set_os_env()
#
# # Print environment variables to verify
# import os
# print("Environment Variables:")
# for key in yaml_reader.config_dict.keys():
#     print(f"{key}={os.getenv(key)}")
