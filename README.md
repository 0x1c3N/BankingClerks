# Banking Clerks

This Python script simulates a customer service scenario where customers of different types (casual, commercial, loan) arrive during different shifts, and clerks provide service to them based on certain criteria. The simulation runs for three shifts: 09:00, 12:00, and 15:00.

## Features
- **Customer Class:**
  - Represents a customer with attributes such as name, arrival time, customer type, process time, etc.
  - Provides methods to reset and display customer information.

- **Clerk Class:**
  - Represents a clerk with attributes such as index, current customer, availability status, etc.
  - Provides methods to reset clerk information.

- **Simulation Algorithm:**
  - Utilizes a simulation algorithm (`min_clerk_algo`) to assign customers to clerks based on minimum wait time.
  - The simulation is run for a fixed total time, and clerks serve customers based on their arrival times.

- **Random Customer Generation:**
  - Generates a list of random customers based on the number given to the application with random arrival times, customer types, and process times. So, every new run is new test case for the program.

- **Output Logging:**
  - Outputs information about customers and clerks during each shift to the "output.txt" file.

## Usage
1. Clone the repository:

    ```bash
    git clone https://github.com/0x1c3N/BankingClerks.git
    cd BankingClerks
    ```

2. Run the script:

    ```bash
    python main.py # Can be used for Linux, MacOS, Windows
    ```

    Run the compiled exe:
  
    ```bash
    main.exe #Just for Windows
    ```


3. View the simulation results in the terminal and "output.txt" file.

## Configuration
- Modify the `maxWaitTimes` list to adjust default maximum waiting times for casual, commercial, and loan customers.
- Adjust the shift times (`firstShift`, `secondShift`, `thirdShift`) based on your business requirements.
- Customize the `outputFileName` to change the name of the output file.

## Notes
- The script assumes a fixed total time (`totalTime = 160`) for each shift.
- The simulation stops if any customer's wait time exceeds their maximum allowed wait time.

