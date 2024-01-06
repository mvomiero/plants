# main.py

from src.species_fetch import main as species_fetch
from src.scatter_plot import main as scatter_plot

# Call the main function from species_fetch.py
def main():
    print ("fetching species and retrieving climatic data...")
    species_fetch()
    scatter_plot()
    print("succsessfully finished!")

# Call the main function in main.py
if __name__ == "__main__":
    main()