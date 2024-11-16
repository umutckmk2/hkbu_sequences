import csv
import json
import os

def csv_to_json(csv_file_path, json_file_path):
    try:
        # Read the CSV file
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            rows = list(csv_reader)
        
        # Write to the JSON file
        with open(json_file_path, mode='w', encoding='utf-8') as json_file:
            json.dump(rows, json_file, indent=4, ensure_ascii=False)
        
        print(f"CSV file '{csv_file_path}' has been successfully converted to JSON file '{json_file_path}'.")
    except FileNotFoundError:
        print(f"Error: The file '{csv_file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Provide paths to the input CSV file and output JSON file
    input_csv_path = "input.csv"  # Replace with your CSV file path
    output_json_path = "output.json"  # Replace with your desired JSON file path
    
    # Ensure the input file exists
    if not os.path.exists(input_csv_path):
        print(f"The input file '{input_csv_path}' does not exist. Please check the path and try again.")
    else:
        csv_to_json(input_csv_path, output_json_path)

