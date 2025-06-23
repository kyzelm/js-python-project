import json

class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_JSON_file(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"File {self.file_path} not found.")
            return None
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file {self.file_path}.")
            return None
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return None

    def write_JSON_file(self, data):
        try:
            with open(self.file_path, 'w') as file:
                json.dump(data, file, indent=4)
            # print(f"Data successfully written to {self.file_path}.")
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")