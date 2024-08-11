import os
import json
import yaml
import configparser


class ConfigReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.config_dict = {}

    def read_config(self):
        ext = os.path.splitext(self.file_path)[1]

        if ext == '.yaml':
            self.config_dict = self._read_yaml()
        elif ext == '.cfg':
            self.config_dict = self._read_cfg()
        elif ext == '.conf':
            self.config_dict = self._read_conf()
        else:
            raise ValueError("Unsupported file extension")

    def _read_yaml(self):
        with open(self.file_path, 'r') as file:
            data = yaml.safe_load(file)
        return self._flatten_dict(data)

    def _read_cfg(self):
        config = configparser.ConfigParser()
        config.read(self.file_path)
        data = {section: dict(config.items(section)) for section in config.sections()}
        return self._flatten_dict(data)

    def _read_conf(self):
        data = {}
        with open(self.file_path, 'r') as file:
            for line in file:
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    data[key] = value
        return self._flatten_dict(data)

    def _flatten_dict(self, data, parent_key='', sep='.'):
        items = []
        for k, v in data.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(self._flatten_dict(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    def write_to_env(self, file_path):
        with open(file_path, 'w') as file:
            for key, value in self.config_dict.items():
                file.write(f"{key}={value}\n")

    def write_to_json(self, file_path):
        with open(file_path, 'w') as file:
            json.dump(self.config_dict, file, indent=4)

    def set_os_env(self):
        for key, value in self.config_dict.items():
            os.environ[key] = str(value)


