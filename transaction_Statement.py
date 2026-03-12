import pdfplumber
import re
import pandas as pd


def extract_the_pdf_data(pdf_path):
    all_data = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            all_data.append(text)
    # print(all_data)
    return all_data


import re


import re


# def extract_transaction_data(raw_text):
#     transactions = []  # List to store all transactions
#     # Define regex patterns to capture date, paid to, amount, time, and paid by
#     date_pattern = r"([A-Za-z]{3} \d{1,2}, \d{4}) Paid to"
#     paid_to_pattern = r"([A-Za-z]{3} \d{2}, \d{4}) (Transfer to|Paid to) (.+)"
#     amount_pattern = r"₹([\d,]+)"
#     time_pattern = r"(\d{2}:\d{2} [ap]m)"
#     paid_by_pattern = r"Paid by (\w+)"

#     # Process each page's raw text (assuming raw_text is a list of lines)
#     for page in raw_text:
#         pagees = page.split("\n")
#         print(pagees)
#         one_transactions = []  # List to store transactions for this page

#         one_transaction = {}  # Create a new dictionary for each transaction

#         # Extract date using regex pattern
#         date_match = re.search(date_pattern, page)
#         if date_match:
#             date = date_match.group(1)
#             one_transaction["Date"] = date

#         # Extract paid to using regex pattern
#         paid_to_match = re.search(paid_to_pattern, page)
#         if paid_to_match:
#             paid_to = paid_to_match.group(
#                 3
#             )  # The third group contains the "Paid to" value
#             one_transaction["Paid to"] = paid_to

#         # Extract amount using regex pattern
#         amount_match = re.search(amount_pattern, page)
#         if amount_match:
#             amount = amount_match.group(1)
#             one_transaction["Amount"] = amount

#         # Extract time using regex pattern
#         time_match = re.search(time_pattern, page)
#         if time_match:
#             time = time_match.group(1)
#             one_transaction["Time"] = time

#         # Extract paid by using regex pattern
#         paid_by_match = re.search(paid_by_pattern, page)
#         if paid_by_match:
#             paid_by = paid_by_match.group(1)
#             one_transaction["Paid by"] = paid_by

#         # If any transaction details are found, add the transaction to the list for this page
#         if one_transaction:
#             one_transactions.append(one_transaction)

#         # Append all transactions from this page to the main transactions list
#         transactions.extend(one_transactions)

#     return transactions


def extract_transaction_data(raw_data):
    # Output list to collect transaction records
    transactions = []

    #   Define regex patterns to capture date, paid to, amount, time, and paid by
    date_pattern = r"([A-Za-z]{3} \d{1,2}, \d{4}) Paid to"
    paid_to_pattern = r"([A-Za-z]{3} \d{2}, \d{4}) (Transfer to|Paid to) (.+)"
    amount_pattern = r"₹([\d,]+)"
    time_pattern = r"(\d{2}:\d{2} [ap]m)"
    paid_by_pattern = r"Paid by (\w+)"

    i = 0
    while i < len(raw_data):
        line = raw_data[i]
        new_line = line.split("\n")
        clear_data = new_line[1:-1]
        print(clear_data)

        print(
            "******************************************************************************************"
        )
        transactions = []

        for i in range(len(clear_data)):

            final_data = clear_data[2:i]
            grouped_data = {}
            for i in final_data:
                print(i)

                date_match = re.search(date_pattern, i)
                if date_match:
                    date = date_match.group(1)
                    grouped_data["Date"] = date

                # Extract paid to using regex pattern
                paid_to_match = re.search(paid_to_pattern, i)
                if paid_to_match:
                    paid_to = paid_to_match.group(
                        3
                    )  # The third group contains the "Paid to" value
                    grouped_data["Paid to"] = paid_to

                # Extract amount using regex pattern
                amount_match = re.search(amount_pattern, i)
                if amount_match:
                    amount = amount_match.group(1)
                    grouped_data["Amount"] = amount

                # Extract time using regex pattern
                time_match = re.search(time_pattern, i)
                if time_match:
                    time = time_match.group(1)
                    grouped_data["Time"] = time

                #    Extract paid by using regex pattern
                paid_by_match = re.search(paid_by_pattern, i)
                if paid_by_match:
                    paid_by = paid_by_match.group(1)
                    grouped_data["Paid by"] = paid_by

                if grouped_data:
                    transactions.append(grouped_data)
                    grouped_data = {}

        print("-------------------------------------------------------------------")
        print("The final Grouped Data", transactions)
        df = pd.DataFrame(transactions)
        print(df)

    return transactions


transactions = extract_transaction_data(extract_the_pdf_data("./tran.pdf"))

# df = pd.DataFrame(transactions)
# df.to_csv("transaction.csv", index=True)
# df.to_excel("transaction.xlsx", index=True)

# print(df)
