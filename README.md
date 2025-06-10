# Instagram Reels Downloader

## Requirements

- Python 3.7 or higher
- Internet connection (to download reels)
- Instagram reel URLs to download

## Installation

1. Clone the repository or download the source code.

   ```
   git clone https://github.com/PizzasRDelicious/Reels-Downloader.git
   ```

2. Check if you have python installed.

   - **On Windows:**

   ```
   python --version
   ```

   - **On macOS/Linux:**

   ```
   python3 --version
   ```

3. Create and activate a virtual environment:

   - **On Windows:**

     ```
     python -m venv venv
     venv\Scripts\activate
     ```

   - **On macOS/Linux:**
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```

4. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

5. Running the script

   - **On Windows:**

   ```
   python main_gui.py
   ```

   - **On macOS/Linux:**

     ```
     python3 main_gui.py
     ```

## EHH can kinda ingore this part: Prepare your input CSV file with the following columns (case sensitive):

```
Name, Reel Url, Downloaded, Uploaded
Reel_Name1, https://instagram.com/..., ,
Reel_Name2, https://instagram.com/..., , True
```

The "Downloaded" column indicates if the reel has been downloaded before. To download new reels, leave this column blank.
The "Uploaded" column is not used yet by the downloader.
Downloaded reels will be saved in the downloads folder.
