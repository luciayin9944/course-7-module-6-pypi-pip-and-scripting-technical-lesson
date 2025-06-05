# Entry script that should call the reporting logic from lib/report_generator.py

# TODO: Import your report generator module
# from lib.report_generator import generate_csv_report
from lib.report_generator import generate_csv_report


def main():
    # TODO: Call generate_csv_report()
    # This script will be run using `python generate_report.py`
    # pass
    generate_csv_report()

if __name__ == "__main__":
    main()
