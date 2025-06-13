from .analyzer import TestAnalyzer
import argparse
import os

def main():
    parser = argparse.ArgumentParser(
        description='Analyze Python test files and generate reports.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  # Analyze a single directory
  pytest-test-analyzer --path ./tests --output report.html --format html

  # Analyze multiple directories
  pytest-test-analyzer --path ./tests ./integration_tests --output report.html

  # Include only tests with specific decorators
  pytest-test-analyzer --path ./tests --include pytest.mark.sanity pytest.mark.regression

  # Exclude tests with specific decorators
  pytest-test-analyzer --path ./tests --exclude pytest.mark.skip pytest.mark.xfail
'''
    )
    
    parser.add_argument(
        '--path',
        nargs='+',
        required=True,
        help='Path(s) to Python test files or directories containing test files. Can specify multiple paths.'
    )
    
    parser.add_argument(
        '--output',
        default='test_analytics.txt',
        help='Output file path for the analysis report (default: test_analytics.txt)'
    )
    
    parser.add_argument(
        '--include',
        nargs='+',
        help='Include only tests that have ALL of these decorators. Example: pytest.mark.sanity pytest.mark.regression'
    )
    
    parser.add_argument(
        '--exclude',
        nargs='+',
        help='Exclude tests that have ANY of these decorators. Example: pytest.mark.skip pytest.mark.xfail'
    )
    
    parser.add_argument(
        '--format',
        choices=['txt', 'html', 'markdown'],
        default='txt',
        help='Output format for the analysis report (default: txt)'
    )
    
    args = parser.parse_args()
    
    analyzer = TestAnalyzer()
    analyzer.set_decorator_filters(args.include, args.exclude)
    analyzer.analyze_path(args.path)
    analyzer.write_to_file(args.output, args.format)
    
    # Get absolute path for better visibility
    abs_output_path = os.path.abspath(args.output)
    print("\n✅ Analysis report generated successfully!")
    print(f"📄 Report location: {abs_output_path}")
    print(f"📊 Format: {args.format.upper()}")
    print(f"📈 Total files analyzed: {analyzer.stats['total_files']}")
    print(f"🧪 Total test cases: {analyzer.stats['total_tests']}")

if __name__ == '__main__':
    main()
