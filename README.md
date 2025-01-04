## Scientific Calculator with Persistent History
A powerful Scientific Calculator application built using Python and PyQt5, featuring a sleek user interface, support for advanced scientific functions, and persistent calculation history. This application lets you perform various mathematical operations, including trigonometric, logarithmic, and algebraic calculations. The persistent history ensures you can access previously calculated expressions and results even after restarting the app.

## Features
1. Basic Operations:
   Addition (+), subtraction (-), multiplication (*), division (/)
   Decimal point (.)
2. Scientific Functions:
3. Trigonometric functions: sin, cos, tan
4. Logarithmic functions: log (base 10), ln (natural logarithm)
5. Square root: sqrt
6. Power: ^
7. Constants: pi (π)
8. Persistent History:
   Save and Load History: All calculated expressions and results are stored in a file (calc_history.txt) and reloaded every time the app starts.
   Interactive History Panel: Double-click any history item to load the expression back into the calculator for reuse.
9. User-Friendly Design:
   Intuitive layout and responsive design.
   Easy-to-navigate history panel.
   Error handling for invalid expressions.

## Installation
Clone the Repository:
```bash
git clone https://github.com/Vikramjangid/Scientific-Calculator-with-Persistent-History.git
cd Scientific-Calculator-with-Persistent-History
```

## Install Dependencies: Ensure you have Python installed on your system. Install the required library:
```bash
pip install PyQt5
```

## Run the Application:
```bash
python scientific_calculator.py
```

## Usage
1. Perform calculations using the provided buttons for basic and scientific operations.
2. View previous calculations in the history panel on the right.
3. Double-click any history item to reload it for further computations.
4. Close and reopen the app to see that your history is still available.

## Project Structure
Scientific-Calculator-with-Persistent-History/
├── calc_history.txt       # Stores calculation history (auto-created)
├── scientific_calculator.py # Main application script
├── README.md              # Project documentation

## Contributing
Contributions are welcome! If you have suggestions or want to report bugs, please open an issue or submit a pull request.

## Author
Vikram Jangid
GitHub: https://github.com/Vikramjangid
