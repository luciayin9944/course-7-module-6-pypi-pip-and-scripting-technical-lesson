# TODO: This function should generate a CSV report named "report_YYYYMMDD.csv"
# It should contain a header row ["ID", "Status"]
# It should include at least one row of mock data
import csv
from datetime import datetime

def generate_csv_report():
    """Generate a CSV report and write mock content."""
    # Placeholder for student implementation
    # pass

    # Generate report
    filename = f"report_{datetime.now().strftime('%Y%m%d')}.csv"
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Status"])
        writer.writerow([1, "Complete"])

    print(f"Report saved as {filename}")

#generate_csv_report()