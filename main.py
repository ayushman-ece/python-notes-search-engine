
from search_engine import search_file


def main():
    print("=" * 42)
    print("         PYTHON NOTES SEARCH ENGINE")
    print("=" * 42)

    file_path = input("Enter text file path: ").strip().strip('"')
    keyword = input("Enter keyword to search: ").strip()

    try:
        results = search_file(file_path, keyword)

        print(f"\nSearch results for: {keyword}")
        print(f"Matches found: {len(results)}")

        if results:
            for result in results:
                print(
                    f"Line {result['line_number']}: "
                    f"{result['text']}"
                )
        else:
            print("No matching lines found.")

    except (ValueError, OSError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
