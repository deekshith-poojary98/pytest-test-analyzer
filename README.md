
# Pytest Test Analyzer

[![PyPI version](https://badge.fury.io/py/pytest-test-analyzer.svg)](https://badge.fury.io/py/pytest-test-analyzer)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/pypi/pyversions/pytest-test-analyzer.svg)](https://pypi.org/project/pytest-test-analyzer/)
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/pytest-test-analyzer?period=total&units=international_system&left_color=gray&right_color=orange&left_text=downloads)](https://pepy.tech/project/pytest-test-analyzer)

A powerful Python tool that analyzes pytest test files and generates comprehensive reports. Get deep insights into your test suite by analyzing test structure, decorator patterns, and test organization. Perfect for understanding and maintaining large test suites, tracking test coverage patterns, and identifying areas for test optimization.

## Features

- 🔍 Analyzes pytest test files and directories
- 📊 Generates detailed statistics about test cases
- 🏷️ Tracks pytest markers and decorators
- 📝 Supports multiple output formats (HTML, Markdown, Text)
- 🎯 Filter tests by decorators
- 📈 Provides class-wise and marker-wise statistics
- 🎨 Beautiful HTML reports with charts

## Installation

```bash
pip install pytest-test-analyzer
```

## Usage

### Basic Usage

Analyze a test directory and generate an HTML report:

```bash
pytest-test-analyzer --path "path/to/tests" --output report.html --format html
```

### Command Line Options

```bash
pytest-test-analyzer --path PATH [--output OUTPUT] [--format FORMAT] [--include INCLUDE] [--exclude EXCLUDE]
```

- `--path`: Path(s) to Python test files or directories (required)
- `--output`: Output file path
- `--format`: Output format - txt, html, or md (default: html)
- `--include`: Include only tests with specific decorators
- `--exclude`: Exclude tests with specific decorators

### Examples

#### Analyzing Test Files

1. **Analyze a single test file:**
   ```bash
   pytest-test-analyzer --path "tests/test_login.py" --output login_analysis.html --format html
   ```

2. **Analyze multiple specific test files:**
   ```bash
   pytest-test-analyzer --path "tests/test_login.py" "tests/test_registration.py" --output auth_analysis.html
   ```

3. **Analyze test files with specific patterns:**
   ```bash
   pytest-test-analyzer --path "tests/test_*_api.py" --output api_analysis.html
   ```

#### Analyzing Test Directories

1. **Analyze a single test directory:**
   ```bash
   pytest-test-analyzer --path ./tests --output report.html --format html
   ```

2. **Analyze multiple test directories:**
   ```bash
   pytest-test-analyzer --path ./tests ./integration_tests --output report.html
   ```

3. **Analyze nested test directories:**
   ```bash
   pytest-test-analyzer --path ./tests/unit ./tests/integration --output nested_analysis.html
   ```

#### Filtering Tests

1. **Include only tests with specific decorators:**
   ```bash
   pytest-test-analyzer --path ./tests --include pytest.mark.sanity pytest.mark.regression
   ```

2. **Exclude tests with specific decorators:**
   ```bash
   pytest-test-analyzer --path ./tests --exclude pytest.mark.skip pytest.mark.xfail
   ```

3. **Combine file and decorator filters:**
   ```bash
   pytest-test-analyzer --path "tests/test_api.py" --include pytest.mark.smoke --output api_smoke.html
   ```

#### Output Formats

1. **Generate a markdown report:**
   ```bash
   pytest-test-analyzer --path ./tests --output report.md --format md
   ```

2. **Generate a text report:**
   ```bash
   pytest-test-analyzer --path ./tests --output report.txt --format txt
   ```

3. **Generate HTML report with custom name:**
   ```bash
   pytest-test-analyzer --path ./tests --output custom_name.html --format html
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter any issues or have questions, please open an issue on GitHub. 
