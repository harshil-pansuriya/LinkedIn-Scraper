import pandas as pd
from datetime import datetime
import argparse

from scripts.browser_automation import search_profiles
from utils.logger import setup_logger
logger = setup_logger(__name__)

def main():
    parser = argparse.ArgumentParser(description='LinkedIn Profile Scraper')
    parser.add_argument('first_name', help='First name of the person to search')
    parser.add_argument('last_name', help='Last name of the person to search')
    args = parser.parse_args()

    try:
        print(f"\nSearching for: {args.first_name} {args.last_name}")
        results = search_profiles(args.first_name, args.last_name)
        if results:
            save_results(results) #save result in csv format
            print(f"\nFound {len(results)} profiles!")
        else:
            print("\nNo profiles found!")
    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        
def save_results(results):
    if not results:
        logger.warning("No results to save")
        return
        
    timestamp = datetime.now().strftime("%y%m%d_%H%M%S")
    file = f"output/Result_{timestamp}.csv"
    df = pd.DataFrame(results)
    df.to_csv(file, index=False)
    logger.info(f"Results saved to {file}")

if __name__ == "__main__":
    main()