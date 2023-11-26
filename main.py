# main.py

from src.species_fetch import main as species_fetch

# Call the main function from species_fetch.py
def main():
    print ("fetching species and retrieving climatic data...")
    species_fetch()

# Call the main function in main.py
if __name__ == "__main__":
    main()