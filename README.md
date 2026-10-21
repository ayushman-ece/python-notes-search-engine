📂 Python Notes Search Engine

**A modular Python utility that searches text files for keywords and displays matching lines with their line numbers.**

---

## 📌 Overview

Finding specific information in lengthy notes or text files can be time-consuming. Python Notes Search Engine simplifies this process by searching a file for a keyword and displaying every matching line.

The application uses Python's `pathlib` for file handling and case-insensitive string matching to find results regardless of capitalization. Its modular structure separates search logic from user interaction.

## ✨ Features

- Search text files for specific keywords
- Perform case-insensitive searches
- Display matching lines with their line numbers
- Show the total number of matches
- Handle missing files and invalid keywords
- Process files line by line
- Preserve the original text file
- Keep the application modular and easy to extend

## 🛠️ Tech Stack

- Python 3
- `pathlib` — filesystem path handling
- String methods — case-insensitive searching
- File handling, loops, functions, and exception handling

No third-party packages are required.

## 📁 Project Structure

```text
python-notes-search-engine/
├── main.py
├── search_engine.py
└── README.md
```

- **`main.py`** handles user input and displays search results.
- **`search_engine.py`** contains file validation and keyword-search logic.

## 🚀 Getting Started

### Prerequisites

Python 3.8 or newer.

### Run the application

1. Download or clone the repository.
2. Open the project folder in your terminal.
3. Run:

```bash
python main.py
```

4. Enter the text file path.
5. Enter the keyword you want to search for.

## 💻 Example

Input file, `sample.txt`:

```text
Python is easy to learn.
I am building Python projects.
Java is another programming language.
PYTHON is useful for automation.
I practise coding every day.
```

Search keyword: `python`

Expected output:

```text
Search results for: python
Matches found: 3
Line 1: Python is easy to learn.
Line 2: I am building Python projects.
Line 4: PYTHON is useful for automation.
```

## 🧠 Concepts Learned

- Reading files line by line
- Working with `pathlib`
- Case-insensitive string matching
- Using `enumerate()` for line numbers
- Storing search results in lists and dictionaries
- Input validation and exception handling
- Modular programming

## ⚠️ Notes

- The search is case-insensitive.
- Matching is based on whether the keyword appears anywhere in a line.
- The original file is never modified.
- The program searches one text file per execution.

## 🔮 Future Improvements

- Search across multiple files
- Support regular expressions
- Highlight matching keywords
- Add a graphical user interface
- Export results to a text or CSV report
- Support file-type filters

## 👨‍💻 Author

**Ayushman Tiwari**

GitHub: [@ayushman-ece](https://github.com/ayushman-ece)

---

*Built with Python to practise file processing, string searching, and modular programming.*