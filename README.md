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

Run the downloader script:

```
python .\main_gui.py
```

Usage
Prepare your input file (.csv) with the following columns (case sensitive):

```
Name, Reel Url,	Downloaded,	Uploaded
Reel_Name1, https://instagram.com/...	, 
Reel_Name2, https://instagram.com/...	, True	
```
The "Downloaded" column determines if it had been downloaded before. If you want to add new download, just leave it blank

The "Uploaded" column is not used by the downloader yet

Downloaded reels will be shown in the 'downloads' folder
