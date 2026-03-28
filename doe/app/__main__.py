#from .bot import main
from crawler.app.search import search_wiki


def main():
    print(search_wiki("poewiki", "Determination"))

if __name__ == "__main__":
    main()