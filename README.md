# Internet Speed Twitter Bot

## Overview

This project is a Python script that automatically checks your internet speed and posts a tweet if the speed is below a specified threshold. The script uses Selenium to automate interactions with the Speedtest website and Twitter.

## Features

- **Check Internet Speed**: The bot navigates to Speedtest.net, starts the test, and retrieves the download and upload speeds.
- **Tweet at Provider**: If the internet speed is below the threshold, the bot logs into Twitter and posts a tweet about the issue.

## Prerequisites

- Python 3.x
- Google Chrome browser
- ChromeDriver (compatible with your version of Chrome)
- Required Python libraries: `selenium`, `python-dotenv`

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/AyushKanyal-me/SppedTest-TwitterPyProject.git
   cd SppedTest-TwitterPyProject
   ```

2. **Install Dependencies**

- Ensure you have Python 3.x installed. Install the required Python libraries using pip:

  ```bash
  pip install selenium python-dotenv
  ```

3. **Setup Environment Variables**

- Create a .env file in the project root directory and add your Twitter credentials:

  ```plaintext
  TWITTER_EMAIL=your_twitter_email
  TWITTER_PASS=your_twitter_password
  ```
- Replace your_twitter_email and your_twitter_password with your actual Twitter credentials.

4. Download ChromDriver
 
- Download the appropriate ChromeDriver version from [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/downloads) page.
- Ensure the chromedriver binary is in your system's PATH or specify its location in the script.


## Usage

1. **Run the Script**
   Execute the script using Python:
   ```bash
   python main.py
   ```

   The script will:
  - Open Speedtest.net, run the speed test, and retrieve the results.
  - If the download or upload speed is below 150 Mbps, it will log into Twitter and post a tweet.

## Notes

- **Security**: Ensure you do not share your .env file or hard-code your credentials in the script.
- **Compatibility**: This script is designed for use with Google Chrome and may need adjustments for other browsers or versions.

## Troubleshooting

- If you encounter issues with Selenium, ensure that ChromeDriver is compatible with your version of Chrome.
- Make sure your Twitter credentials are correct and that you have not enabled two-factor authentication, which may require additional steps.

## Acknowledgements

- **[Selenium](https://www.selenium.dev/)**: For providing the tools to automate web interactions.
- **[Speedtest.net](https://www.speedtest.net/)**: For offering a reliable service to test internet speed.
- **[Twitter](https://twitter.com/)**: For providing a platform to post updates.
- **[Python](https://www.python.org/)**: For the programming language used in this project.
- **[ChromeDriver](https://sites.google.com/chromium.org/driver/downloads)**: For enabling interaction with Google Chrome.


Feel free to contribute to this project by submitting pull requests or opening issues. For any questions, contact me at AyushKanyal-me.



