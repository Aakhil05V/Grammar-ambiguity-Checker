# Grammar Ambiguity Checker

A comprehensive web development application designed to analyze and detect ambiguities in context-free grammars (CFG). This tool helps computer science students, educators, and linguists understand and identify ambiguities in their grammar definitions.

## Project Overview

The **Grammar Ambiguity Checker** is a Flask-based web application that takes a context-free grammar as input and determines whether it contains ambiguities. An ambiguous grammar allows a single string to be parsed in multiple ways, which is problematic in language processing and compiler design.

## Features

✨ **Core Features:**
- Parse and validate context-free grammars
- Detect ambiguous grammar rules
- Generate parse trees for test strings
- Identify multiple derivations for ambiguous strings
- User-friendly web interface
- Real-time analysis and results

## Tech Stack

### Backend
- **Framework:** Flask (Python micro web framework)
- **Language:** Python 3.x
- **Libraries:** 
  - NLTK (Natural Language Toolkit) - for grammar parsing and tree generation
  - Flask - for web server and routing

### Frontend
- **HTML5** - Markup structure
- **CSS3** - Styling and responsive design
- **JavaScript** - Interactive UI elements

### Deployment
- **Development Server:** Flask development server
- **Default Port:** localhost:5000

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- Git

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Aakhil05V/Grammar-ambiguity-Checker.git
   cd Grammar-ambiguity-Checker
   ```

2. **Create a Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Required Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   Dependencies include:
   - Flask
   - NLTK

4. **Download NLTK Data (if required)**
   ```bash
   python -m nltk.downloader punkt averaged_perceptron_tagger universal_tagset
   ```

## Project Structure

```
Grammar-ambiguity-Checker/
│
├── app.py                    # Main Flask application
├── requirements.txt          # Project dependencies
├── README.md                 # This file
│
├── templates/
│   ├── index.html           # Main web interface
│   └── results.html         # Results display page
│
├── static/
│   ├── css/
│   │   └── style.css        # Styling
│   └── js/
│       └── script.js        # JavaScript functionality
│
└── tests/
    └── test_grammar.py      # Unit tests
```

## How to Run the Application

### Starting the Application

1. **Activate Virtual Environment (if created)**
   ```bash
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

2. **Run the Flask Server**
   ```bash
   python app.py
   ```

3. **Access the Application**
   - Open your web browser
   - Navigate to: `http://localhost:5000`
   - The application will be ready to use

### Stopping the Application
   - Press `Ctrl + C` in your terminal

## Example Grammars

### Example 1: Ambiguous Grammar (Classic)

**Grammar Definition:**
```
S -> S + S | S * S | a
```

**Explanation:**
This grammar is ambiguous because the string "a + a * a" can be parsed in two different ways:
- (a + a) * a
- a + (a * a)

**Test String:** `a + a * a`

### Example 2: Unambiguous Grammar (Corrected)

**Grammar Definition:**
```
S -> T | S + T
T -> F | T * F
F -> a | ( S )
```

**Explanation:**
This grammar enforces operator precedence, making it unambiguous. Multiplication binds tighter than addition.

**Test String:** `a + a * a`

### Example 3: Simple Arithmetic Grammar (Ambiguous)

**Grammar Definition:**
```
E -> E + E | E - E | number
```

**Explanation:**
Ambiguous for left-recursion. The string "5 - 3 - 1" can be parsed as:
- (5 - 3) - 1 = 1
- 5 - (3 - 1) = 3

**Test String:** `5 - 3 - 1`

## Test Cases and Expected Output

### Test Case 1: Ambiguous Grammar Detection

**Input:**
- Grammar: `S -> S + S | S * S | a`
- Test String: `a + a * a`

**Expected Output:**
```
Ambiguous: YES
Number of Parse Trees: 2
Possible Derivations:
1. ((a + a) * a)
2. (a + (a * a))
```

### Test Case 2: Unambiguous Grammar

**Input:**
- Grammar:
  ```
  S -> T | S + T
  T -> F | T * F
  F -> a
  ```
- Test String: `a + a * a`

**Expected Output:**
```
Ambiguous: NO
Number of Parse Trees: 1
Unique Derivation:
1. (S (S (T (F a))) + (T (T (F a)) * (F a)))
```

### Test Case 3: Invalid String

**Input:**
- Grammar: `S -> a b | b a`
- Test String: `a c b`

**Expected Output:**
```
Parsing Failed: NO
String cannot be generated by the given grammar.
No valid derivation exists.
```

## Usage Guide

### Step-by-Step Instructions

1. **Navigate to Application**
   - Open `http://localhost:5000` in your browser

2. **Input Grammar Rules**
   - Enter grammar rules in the format: `S -> a | b c`
   - Use `|` to separate alternatives
   - Use `->` to separate non-terminal from production
   - Each rule should be on a new line

3. **Define Test String**
   - Enter the string you want to test
   - String tokens should be space-separated (optional)

4. **Analyze**
   - Click the "Analyze" button
   - Wait for results

5. **View Results**
   - Check if grammar is ambiguous
   - Review parse trees
   - See multiple derivations if they exist

## Features in Detail

### Grammar Validation
- Validates syntax of input grammar
- Checks for proper formatting
- Reports syntax errors clearly

### Ambiguity Detection
- Generates all possible parse trees
- Identifies multiple derivations
- Counts alternative parse trees

### Parse Tree Visualization
- Displays parse trees in readable format
- Shows hierarchical structure
- Highlights alternative paths

## Troubleshooting

### Common Issues

**Issue: "ModuleNotFoundError: No module named 'flask'"**
- **Solution:** Install Flask using `pip install flask`

**Issue: "Port 5000 is already in use"**
- **Solution:** Change the port in app.py or kill the process using port 5000

**Issue: "Grammar parsing error"**
- **Solution:** Check your grammar syntax. Ensure each rule is properly formatted.

**Issue: Application not opening at localhost:5000**
- **Solution:** Make sure Flask server is running. Check for error messages in terminal.

## File Descriptions

- **app.py**: Contains Flask routes, grammar parsing logic, and ambiguity detection algorithms
- **index.html**: Main user interface with input forms
- **results.html**: Displays analysis results and parse trees
- **style.css**: CSS styling for responsive design
- **script.js**: JavaScript for form validation and dynamic UI
- **requirements.txt**: Lists all Python dependencies

## API Endpoints

```
GET  /                    - Main page
POST /analyze            - Submit grammar for analysis
GET  /results            - Display results
```

## Performance Considerations

- Grammar complexity affects analysis time
- Very complex grammars may take longer to analyze
- Recommended: Keep grammar size moderate for web interface

## Future Enhancements

- 🎯 Support for CNF (Chomsky Normal Form) conversion
- 🎯 LL and LR parsing visualization
- 🎯 Grammar comparison tool
- 🎯 Export results to PDF
- 🎯 Batch analysis capability
- 🎯 Visual grammar editor

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Author

**Aakhil05V**
- GitHub: [@Aakhil05V](https://github.com/Aakhil05V)

## Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/Aakhil05V/Grammar-ambiguity-Checker/issues) section
2. Create a new issue with detailed description
3. Include:
   - Grammar definition
   - Test string
   - Expected vs actual output
   - Error messages

## References and Resources

- [NLTK Documentation](https://www.nltk.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Context-Free Grammars Explained](https://en.wikipedia.org/wiki/Context-free_grammar)
- [Parse Trees and Ambiguity](https://en.wikipedia.org/wiki/Parse_tree)

## Changelog

### Version 1.0.0 (Initial Release)
- ✅ Basic grammar parsing
- ✅ Ambiguity detection
- ✅ Parse tree generation
- ✅ Web interface
- ✅ Documentation

## Quick Links

- 📚 [Full Documentation](./docs/DOCUMENTATION.md)
- 🐛 [Report a Bug](https://github.com/Aakhil05V/Grammar-ambiguity-Checker/issues)
- ⭐ Please star this repository if you find it useful!

---

**Note:** This is a educational tool designed for learning purposes. For production-level compiler work, consider using industrial-grade parser generators like ANTLR or Yacc.

**Last Updated:** November 2025
**Status:** Active Development
