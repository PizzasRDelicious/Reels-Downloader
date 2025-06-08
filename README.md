# Instagram Reels Downloader

## Requirements

- Python 3.7+
- Internet connection (to download reels)
- Instagram reel URLs to download

## Installation

1. Clone the repository or download the source code.
2. (Optional but recommended) Create and activate a Python virtual environment:

```
python -m venv venv

# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

Usage
Prepare your input file (.csv or .xlsx) with the following columns (case sensitive):

Name	Reel Url	Downloaded	Uploaded
Reel_Name1, https://instagram.com/...	, 
Reel_Name2, https://instagram.com/...	, True	

The "Downloaded" column should be empty or set to anything other than "True" to download.

The "Uploaded" column is not used by the downloader but can be maintained for your own purposes.

Run the downloader script:

```
python main.py input_file.csv
```

Downloaded reels will be shown in the 'downloads' folder
