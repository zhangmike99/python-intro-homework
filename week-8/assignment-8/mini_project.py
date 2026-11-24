"""
Part 2: Mini-Project — Defensive CSV Reader
The file ../data/messy_data.csv contains a mix of valid and invalid rows. Each row should have three fields — name, category, and amount — but some rows have problems: missing values, non-numeric amounts, or extra columns.

Write a script that reads this file defensively and produces a clean summary. Your program must:

    Wrap the file opening in try/except FileNotFoundError. If the file is missing, print an error message and stop.
    Read the file with csv.DictReader.
    Process each row inside a try/except block. Catch at minimum:
        ValueError — when amount can't be converted to float
        KeyError — in case a row is missing an expected column. Include this clause even if it never runs while you test: csv.DictReader usually fills a missing column with None instead of raising, so a KeyError may not come up with this data. Catching it is still good defensive practice.
    Collect successfully parsed rows into a list of dictionaries.
    Print a summary at the end:

=== CSV Report ===
Rows attempted:  14
Rows parsed:      9
Rows skipped:     5

Skipped rows:
  Row 3: ValueError — could not convert '' to float
  Row 5: ValueError — could not convert 'not_a_number' to float
  Row 7: extra column detected — skipped
  Row 11: ValueError — could not convert '' to float
  Row 13: ValueError — could not convert 'fifteen' to float

Clean data:
  Alice | Food | $12.50
  Bob | Transport | $8.75
  ...

    Hint 1: You can track skipped rows by storing a description of each failure, then printing them at the end. Use enumerate(reader, start=1) to get row numbers as you loop, so your first data row is row 1 like the example above.

    Hint 2: csv.DictReader handles extra fields by storing them under a None key rather than raising an exception, so you will need to check if None in row as a separate guard before the try/except.

Save as: mini_project.py

"""
import csv
import sys

FILE_PATH = "../data/messy_data.csv"


def main():
    # 1. Open the file defensively
    try:
        csv_file = open(FILE_PATH, newline="", encoding="utf-8")
    except FileNotFoundError:
        print(f"Error: could not find '{FILE_PATH}'. Check the path and try again.")
        sys.exit(1)

    clean_rows = []     # list of dicts that parsed successfully
    skipped = []        # descriptions of each failure
    attempted = 0

    with csv_file:
        # 2. Read with DictReader
        reader = csv.DictReader(csv_file)

        for row_num, row in enumerate(reader, start=1):
            attempted += 1

            # Extra columns land under the None key, so guard before the try/except
            if None in row:
                skipped.append(f"Row {row_num}: extra column detected — skipped")
                continue

            # 3. Process each row defensively
            try:
                name = (row["name"] or "").strip()
                category = (row["category"] or "").strip()
                raw_amount = row["amount"]

                if not name or not category:
                    raise ValueError("missing name or category")

                # A short/blank row gives None or '' here; both mean "can't convert"
                try:
                    amount = float(raw_amount)
                except (ValueError, TypeError):
                    raise ValueError(f"could not convert {raw_amount!r} to float") from None

                # 4. Keep the good row
                clean_rows.append({"name": name, "category": category, "amount": amount})

            except ValueError as e:
                skipped.append(f"Row {row_num}: ValueError — {e}")
            except KeyError as e:
                skipped.append(f"Row {row_num}: KeyError — missing column {e}")

    # 5. Summary
    print("=== CSV Report ===")
    print(f"{'Rows attempted:':<17}{attempted:>2}")
    print(f"{'Rows parsed:':<17}{len(clean_rows):>2}")
    print(f"{'Rows skipped:':<17}{len(skipped):>2}")

    print("\nSkipped rows:")
    if skipped:
        for message in skipped:
            print(f"  {message}")
    else:
        print("  (none)")

    print("\nClean data:")
    if clean_rows:
        for r in clean_rows:
            print(f"  {r['name']} | {r['category']} | ${r['amount']:.2f}")
    else:
        print("  (none)")


if __name__ == "__main__":
    main()