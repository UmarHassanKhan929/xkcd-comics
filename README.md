# xkcd-comics 📚

A Python script that automatically downloads all **xkcd** comics from the web and saves them locally. Built using `requests` and `BeautifulSoup`, based on the classic project from *[Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)* by Al Sweigart.

## Features

- Downloads all xkcd comics automatically
- Navigates through every comic using pagination
- Saves images to a local `xkcd/` directory
- Handles missing comics gracefully
- Progress output in the terminal

## Prerequisites

- Python 3.x
- Required packages:
  - `requests`
  - `beautifulsoup4`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/xkcd-comics.git
   cd xkcd-comics
   ```

2. Install dependencies:
   ```bash
   pip install requests beautifulsoup4
   ```

## Usage

Run the script from the command line:

```bash
python comic.py
```

All comics will be downloaded into a newly created `xkcd/` folder in the current directory.

## How It Works

1. Starts at the latest xkcd comic (`https://xkcd.com`)
2. Parses the page to find the comic image URL
3. Downloads and saves the image to the `xkcd/` folder
4. Follows the "Previous" link to the next comic
5. Repeats until all comics have been downloaded

## Project Structure

```
xkcd-comics/
├── comic.py          # Main script
├── README.md         # Project documentation
├── .gitignore        # Git ignore rules
├── LICENSE           # MIT License
└── xkcd/             # Downloaded comics (created at runtime)
```

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [xkcd](https://xkcd.com/) — Randall Munroe
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) — Al Sweigart
