import yt_dlp
import pandas as pd
import os
import sys

from download_instagram_reel import download_instagram_reel
from dataframes import load_dataframe, save_dataframe, get_unique_filename


# Main running process
def process_file(file_path, output_dir="downloads"):
    os.makedirs(output_dir, exist_ok=True)
    df, file_type = load_dataframe(file_path)
    updated = False

    for i, row in df.iterrows():
        if str(row.get("Downloaded")).strip().lower() == "true":
            continue

        name = str(row["Name"]).strip()
        url = str(row["Reel Url"]).strip()
        output_file = get_unique_filename(output_dir, name)

        print(f"\nDownloading: {name} from {url}")
        success = download_instagram_reel(url, output_file)

        if success:
            df.at[i, "Downloaded"] = True
            df.at[i, "Name"] = os.path.splitext(os.path.basename(output_file))[0]
            updated = True

    if updated:
        save_dataframe(df, file_path, file_type)
        print(f"{file_type.upper()} file updated with downloaded status.")
    else:
        print("No new reels were downloaded.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py path/to/reels.csv|xlsx")
        sys.exit(1)

    input_file = sys.argv[1]
    process_file(input_file)
