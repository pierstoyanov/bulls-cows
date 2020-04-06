# stronger-than-ever
import re


def main():
    scans = int(input())
    cookie_cutter = r"(@#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(@#+)"

    for _ in range(scans):
        barcode = input()
        match = re.search(cookie_cutter, barcode)
        if match:
            code = match.group(2)
            digits = "".join(filter(lambda i: i.isdigit(), code))
            if digits == "":
                digits = "00"

            print(f"Product group: {digits}")
        else:
            print("Invalid barcode")


if __name__ == "__main__":
    main()