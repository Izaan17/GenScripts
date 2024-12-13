import argparse
import webbrowser

parser = argparse.ArgumentParser(
    prog='Browser Search',
    description='Does a search query in your default browser')

parser.add_argument("query", nargs="+")

arguments = parser.parse_args()

if arguments.query:
    full_query = ' '.join(arguments.query)
    if "http" in full_query:
        url = f"{full_query}"
    else:
        url = f"https://www.google.com/search?q={full_query}"
    print(f"Searching the web for '{full_query}'")
    webbrowser.open(url)
