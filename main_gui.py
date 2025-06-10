import tkinter as tk
from tkinter import filedialog, messagebox
import os
import threading

import pandas as pd
from download_instagram_reel import download_instagram_reel
from dataframes import load_dataframe, save_dataframe, get_unique_filename

import subprocess
import platform


# Function for open downloads folder button
def open_downloads_folder():
    path = os.path.abspath("downloads")
    os.makedirs(path, exist_ok=True)

    try:
        if platform.system() == "Windows":
            os.startfile(path)
        elif platform.system() == "Darwin":  # macOS
            subprocess.run(["open", path])
        else:  # Linux
            subprocess.run(["xdg-open", path])
    except Exception as e:
        messagebox.showerror("Error", f"Could not open folder: {e}")


# Function to open provided file path in excel.
def open_file_in_excel(file_path):
    if not os.path.isfile(file_path):
        messagebox.showerror("Error", "File not found!")
        return

    # Check for valid extension
    ext = os.path.splitext(file_path)[1].lower()
    if ext not in [".csv", ".xlsx"]:
        messagebox.showwarning("Invalid File", "Please select a .csv or .xlsx file.")
        return

    try:
        if platform.system() == "Windows":
            os.startfile(file_path)
        elif platform.system() == "Darwin":  # macOS
            subprocess.run(["open", file_path])
        else:  # Linux
            subprocess.run(["xdg-open", file_path])
    except Exception as e:
        messagebox.showerror("Error", f"Could not open file: {e}")


# Functions that downloads the url into a file
def process_file(file_path, output_dir="downloads", status_label=None):
    os.makedirs(output_dir, exist_ok=True)
    df, file_type = load_dataframe(file_path)
    updated = False

    for i, row in df.iterrows():
        if str(row.get("Downloaded")).strip().lower() == "true":
            continue

        name = str(row["Name"]).strip()
        url = str(row["Reel Url"]).strip()
        output_file = get_unique_filename(output_dir, name)

        if status_label:
            status_label.config(text=f"Downloading: {name}")

        success = download_instagram_reel(url, output_file)

        if success:
            df.at[i, "Downloaded"] = True
            df.at[i, "Name"] = os.path.splitext(os.path.basename(output_file))[0]
            updated = True

    if updated:
        save_dataframe(df, file_path, file_type)
        msg = f"{file_type.upper()} file updated with download status."
    else:
        msg = "No new reels were downloaded."

    if status_label:
        status_label.config(text=msg)
    messagebox.showinfo("Done", msg)


# Function for Start Downlaod button
def start_download(filepath, status_label):
    if not filepath:
        messagebox.showwarning("Missing File", "Please select a file first.")
        return
    threading.Thread(
        target=process_file, args=(filepath, "downloads", status_label), daemon=True
    ).start()


def launch_gui():
    root = tk.Tk()
    root.title("Instagram Reel Downloader")
    root.geometry("500x300")

    selected_file = tk.StringVar(value=os.path.abspath("input.csv"))

    def browse_file():
        path = filedialog.askopenfilename(
            filetypes=[("CSV or Excel files", "*.csv *.xlsx")]
        )
        selected_file.set(path)

    tk.Label(root, text="Select your CSV or XLSX file:").pack(pady=10)
    tk.Entry(root, textvariable=selected_file, width=60).pack(padx=20)
    tk.Button(root, text="Browse", command=browse_file).pack(pady=5)

    status_label = tk.Label(root, text="", fg="blue")
    status_label.pack(pady=10)

    tk.Button(
        root,
        text="Start Download",
        command=lambda: start_download(selected_file.get(), status_label),
        bg="#4CAF50",
        fg="white",
    ).pack(pady=5)

    tk.Button(root, text="View Downloads Folder", command=open_downloads_folder).pack(
        pady=2
    )

    tk.Button(
        root,
        text="Open in Excel",
        command=lambda: open_file_in_excel(selected_file.get()),
    ).pack(pady=2)

    tk.Label(root, text="Make sure to close CSV file before Start Download").pack(
        pady=10
    )

    root.mainloop()


if __name__ == "__main__":
    launch_gui()
