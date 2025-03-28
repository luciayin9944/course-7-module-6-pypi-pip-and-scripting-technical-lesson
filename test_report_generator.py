from lib.report_generator import generate_csv_report
import os
import csv
from datetime import datetime

def test_report_file_is_created():
    """Test that the report CSV file is created."""
    filename = f"report_{datetime.now().strftime('%Y%m%d')}.csv"
    generate_csv_report()
    assert os.path.exists(filename)

def test_report_file_has_headers():
    """Test that the CSV file has the correct headers."""
    filename = f"report_{datetime.now().strftime('%Y%m%d')}.csv"
    generate_csv_report()

    with open(filename, "r") as file:
        reader = csv.reader(file)
        headers = next(reader)
    
    assert headers == ["ID", "Status"]

def test_report_contains_at_least_one_data_row():
    """Test that the report contains at least one row of data."""
    filename = f"report_{datetime.now().strftime('%Y%m%d')}.csv"
    generate_csv_report()

    with open(filename, "r") as file:
        reader = list(csv.reader(file))
    
    assert len(reader) > 1  # Header + at least one data row

def test_generated_filename_is_correct_format():
    """Ensure the filename format is correct (e.g., report_YYYYMMDD.csv)."""
    filename = f"report_{datetime.now().strftime('%Y%m%d')}.csv"
    generate_csv_report()
    
    assert os.path.exists(filename)
