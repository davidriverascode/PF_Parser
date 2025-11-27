import pandas as pd

rows = []

print("Hello, welcome to PF_Parser!!")

print("\nPlease provide the path and filename of the file: (eg. C:/Users/myuser/Downloads/logs.txt)")
file_path = input("> ")

if file_path == "test":
    print("Opening test file...")
    file_path = r"C:\Users\david\Downloads\filter.txt"

try:
    print("Attempting to read...")
    with open(file_path, 'r') as file:
        for row in file:
            rows.append(row)

except Exception as error:
    print(f"\n!!! Error with file reading: {error}")



# FORMAT
output_csv_file = r"C:/Users/david/Downloads/formatted_logs.csv"

# Deliminate the entire file by spaces
new_data = []

most_cols = 0

for row in rows:
    cur_cols = 0
    index = 0
    new_row = row
    for char in row:
        if char == " ":
            # Slice before the space, and after, and replace the space with a semi-colon
            new_row = f"{new_row[:index]};{new_row[(index + 1):]}"
            cur_cols += 1
            # Count the largest column
            if cur_cols >= most_cols:
                most_cols = cur_cols
        if char == ",":
            # Slice before the space, and after, and replace the space with a semi-colon
            new_row = f"{new_row[:index]};{new_row[(index + 1):]}"
            # Count the largest column
            cur_cols += 1
            if cur_cols >= most_cols:
                most_cols = cur_cols
        index += 1
    new_data.append(new_row)

print("LARGEST COLUMN: ", most_cols)


try:
    print("Formatting new temp text file...")
    with open("temp_file.txt", "w") as temp:
        for row in new_data:
            temp.write(row)
except Exception as error:
    print("\n!!! Error with temp file: ", error)

columns = [
    # System/Syslog Fields (Not part of the CSV data, but precede it)
    "Month",
    "Day",
    "Time",
    "Hostname / Interface Name",
    "Process ID (PID) / Filterlog Tag",
    
    # Core Filterlog Fields (The CSV data starts here)
    "Rule Number (or Sub-Rule ID)", # In your log, this is '69' or '4'
    "blank 1",
    "blank 2",
    "Sub-Rule ID (or Rule ID)", # The secondary ID, e.g., '12014'
    "Interface", # e.g., 'em0'
    "Action", # e.g., 'match', 'block'
    "Action 2",
    "Direction", # 'in' or 'out'
    "IP Version", # '4' or '6'
    "IP Flags", # e.g., '0x0'
    "Unknown 1",
    "Time-To-Live (TTL)",
    "Unknown 2",
    "Unknown 3",
    "Unknown 4",
    "Unknown 5",
    "Protocol",
    "Unknown 6",
    "Source IP Address",
    "Desination IP Address",
    "Source Port",
    "Desination Port",

    # TCP Specific Fields (Only present for TCP protocol logs)
    "Sequence Number",
    "Acknowledgement Number",
    "Window Size",
    "Checksum", # Often not logged or is '0'
    "Options", # Additional TCP options
]

for no_name in range((most_cols + 1) - len(columns)):
    columns.append(f"No Name {no_name}")

print("Columns: ", columns)

deliminated_file = pd.read_csv(
    "temp_file.txt", 
    sep=';', 
    header=None,
    names=columns,
    )

deliminated_file.to_csv(output_csv_file, index=False, header=True)