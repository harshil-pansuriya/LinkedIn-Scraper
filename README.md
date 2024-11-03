# LinkedIn Profile Scraper

This is a Python-based tool that automates LinkedIn profile searches using Browser-Automation with Selenium. The tool searches for profiles based on first and last names, extracts basic information like name,job,location etc. and saves the results to a CSV file.

## Features
- Automated LinkedIn login
- Profile search by first and last name
- Extracts name, job title, and location
- Saves results to CSV file
- Detailed logging, Error Handling

## Installation

1. Create and activate a virtual environment:
   ```
   python -m venv env_name
   env_name\Scripts\activate
   ```
2. Clone the repository:
   ```
   git clone https://github.com/harshil-pansuriya/LinkedIn-Scraper/tree/main
   ```
3. Install required packages:
   ```
   pip install -r requirements.txt
   ```
4. Create necessary directories:
   ```
   mkdir output
   mkdir logs
   ```
5. create .env file to store personal details:
   ```
   LINKEDIN_USERNAME=linkedin_email_id
   LINKEDIN_PASSWORD=linkedin_password
   ```
## Usage

Run the script with first and last name arguments:
```
python app.py firstname lastname
```

The script will:
1. Open Chrome in incognito mode
2. Log into LinkedIn
3. Search for profiles matching the name
4. Extract information from up to 5 profiles
5. Save results to a CSV file in the `output` folder

   
The CSV file contains the following columns:
- name
- job_title
- location

## Dependencies
- selenium
- beautifulsoup4
- webdriver_manager
- pandas

## Contributing

Feel free to: Suggest features, Submit pull requests

## License
This project is licensed under the MIT License - see the LICENSE file for details.

Note: Put your confidential details in .env file and use it in config files