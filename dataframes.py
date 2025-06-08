import pandas as pd
import os


def load_dataframe(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".csv":
        return pd.read_csv(file_path), "csv"
    elif ext == ".xlsx":
        return pd.read_excel(file_path), "xlsx"
    else:
        raise ValueError("Unsupported file format. Use .csv or .xlsx")


def save_dataframe(df, file_path, file_type):
    if file_type == "csv":
        df.to_csv(file_path, index=False)
    elif file_type == "xlsx":
        df.to_excel(file_path, index=False)
    else:
        raise ValueError("Unsupported file format for saving.")


def get_unique_filename(directory, base_name, extension=".mp4"):
    filename = f"{base_name}{extension}"
    full_path = os.path.join(directory, filename)
    counter = 1

    while os.path.exists(full_path):
        filename = f"{base_name}_{counter}{extension}"
        full_path = os.path.join(directory, filename)
        counter += 1

    return full_path
