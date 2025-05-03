import pdfplumber
import pandas as pd
import re

pdf_path = "./fourYear.pdf"
transactions = []

# Step 1: Read PDF and collect all lines
with pdfplumber.open(pdf_path) as pdf:
    index = 0
    for page in pdf.pages:
        text = page.extract_text()
        lines = text.split("\n")

        # Remove header/footer lines
        lines = lines[1:-2]
        if index == 0:
            lines = lines[2:-2]
        if index == len(pdf.pages) - 1:
            lines = lines[1:-6]
        index += 1

        # Define regex patterns to capture date, paid to, amount, time, and paid by
        date_pattern = r"([A-Za-z]{3} \d{1,2}, \d{4}) Paid to"
        paid_to_pattern = (
            r"([A-Za-z]{3} \d{2}, \d{4}) (Transfer to|Paid to) (.+?) (?:Debit|INR)"
        )
        amount_pattern = r"INR\s?([\d,]+(?:\.\d{1,2})?)"
        time_pattern = r"(\d{2}:\d{2} [ap]m)"
        paid_by_pattern = r"Debited from (XX\d+)"

        one_transaction_data = {}
        for line in lines:

            date_match = re.search(date_pattern, line)
            if date_match:
                date = date_match.group(1)
                one_transaction_data["Date"] = date

            paid_to_match = re.search(paid_to_pattern, line)
            if paid_to_match:
                paid_to = paid_to_match.group(3)
                one_transaction_data["Paid to"] = paid_to

            amount_match = re.search(amount_pattern, line)
            if amount_match:
                amount = amount_match.group(1)
                one_transaction_data["Amount"] = amount

            time_match = re.search(time_pattern, line)
            if time_match:
                time = time_match.group(1)
                one_transaction_data["Time"] = time

            paid_by_match = re.search(paid_by_pattern, line)
            if paid_by_match:
                paid_by = paid_by_match.group(1)
                one_transaction_data["Paid by"] = paid_by

            if len(one_transaction_data) >= 3:
                transactions.append(one_transaction_data)
                one_transaction_data = {}


# Step 2: Group every 4 lines into one transaction
# transactions = []
# for i in range(0, len(all_lines), 4):
#     if i + 3 < len(all_lines):  # ensure we have 4 lines
#         line1 = all_lines[i]  # e.g., "May 01, 2025 Paid to X DEBIT ₹50"
#         line2 = all_lines[i + 1]  # e.g., "03:56 pm Transaction ID ..."
#         line3 = all_lines[i + 2]  # UTR line
#         line4 = all_lines[i + 3]  # Paid by line

#         # Extract components
#         print("line1", line1)
#         print("line2", line2)
#         print("line3", line3)
#         print("line4", line4)

#         # transactions.append(
#         #     {
#         #         "Date & Description": date_and_desc,
#         #         "Type": txn_type,
#         #         "Amount": amount,
#         #         "Time": time,
#         #         "Transaction ID": txn_id,
#         #         "UTR": utr,
#         #         "Paid By": paid_by,
#         #     }
#         # )

# Step 3: Save to CSV and Excel
df = pd.DataFrame(transactions)
df.to_csv("PhonePe_Yearly_Transactions.csv", index=False)
df.to_excel("PhonePe_Yearly_Transactions.xlsx", index=False)

print(f"Extracted {len(df)} transactions and saved to CSV and Excel.")
