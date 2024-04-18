# Abyssal and Incursion Tracker

This program is designed to help users track their profits and time spent during Abyssal runs and Incursions in a massively multiplayer online role-playing game (MMORPG). It provides a user-friendly interface for inputting relevant data and automatically calculates profits based on initial and final ISK amounts and time spent in each activity.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Abyssal Money Tracker](#abyssal-money-tracker)
  - [Incursion Tracker](#incursion-tracker)
- [Contributing](#contributing)
- [License](#license)

## Features

**Abyssal Money Tracker:**
  - Input starting ISK, ending ISK, and time spent to calculate profit for each Abyssal run.
  - Automatically keeps track of total profits, number of runs, and total time spent.
  - Allows users to track multiple Abyssal runs and provides an option to stop tracking when finished.

**Incursion Tracker:**
  - Similar to Abyssal Money Tracker, but tailored for tracking Incursions.
  - Users can input profit per incursion and time spent per incursion.
  - Provides an option to track multiple incursions and stops when the user chooses to finish.

## Getting Started

### Prerequisites

To run this program, you need to have Python installed on your system. You can download and install Python from the official website: [python.org](https://www.python.org/).

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/abyss-incursion-tracker.git

2. Navigate to the project directory:
   ```bash
   cd abyss-incursion-tracker

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

## Usage
To use the Abyssal and Incursion Tracker, follow the instructions below:

Abyssal Money Tracker
1. Run the program:
    ```bash
    python main.py
2. Select option 1 to track Abyssal runs.
3. Enter the starting ISK amount, ending ISK amount, and time spent for each Abyssal run.
4. Choose whether to track another Abyssal run (1 for Yes, 0 for No).
5. Once finished, the program will write session details to a text file (Sessions.txt) and display total profits, runs, and time spent.
##Incursion Tracker
1. Run the program:
    ```bash
    python main.py
2. Select option 2 to track Incursions.
3. Enter the profit per incursion and time spent per incursion.
4. Follow the same steps as the Abyssal Money Tracker to track multiple incursions.
##Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.
# Todo:
- Function to average out profits hourly in both the abyss and incursion functions
- ~~error input for the Incursion Module~~
- add session details into file for Incursion Module

# 4/5/24 TextFile Functionality
Adding to File branch created to work on the functionality to add 
end of session reports to a text file for more advanced storage

# 4/10/2024
implemented adding the session details to a Txt file at the end to keep long-term
track of profits and time spent. + Getting the hang of using branches to work on specific info and then
pulling to the main.

# 4/18/2024 
Got back into doing incursion with a cool group of people in WTM
I now have an abyssal tracker that prompt for profit which should always remain a stable 31m 
and then asks for time. I am going to focus now on making an average tracker at the end of the session that shows up to tell you how 
much you made per hour.
