# Python Data Visualization & Analysis Projects - AI Agent Instructions

## Project Overview
Educational Python project repository focused on data manipulation and visualization using pandas, numpy, and matplotlib. Scripts demonstrate CSV data processing, statistical calculations, and visualization techniques with custom styling.

## Architecture & Key Patterns

### Data Processing Workflow
- **CSV Loading**: Use pandas `read_csv()` for data ingestion (see `pandas_read_csv.py`)
- **Data Selection**: Extract columns using bracket notation: `df[['col1', 'col2']]`
- **Column Normalization**: Transform column names to uppercase using `.str.upper()` for consistent display
- **Statistical Calculations**: Apply numpy functions directly to pandas Series (e.g., `np.mean(df['Age'])`)

### Visualization Practices
- **Plotting Libraries**: matplotlib.pyplot for line plots with custom markers and line styles
- **Font Styling**: Define font dictionaries with family, color, and size properties before applying to titles/labels
- **Axis Configuration**: Use `plt.xticks()` for custom tick labels aligned with data ranges
- **Visual Enhancements**: Add grid lines (`plt.grid()`), legends, and multi-line plots for comparison

Example plot pattern from `numpy_plot_data_visualization.py`:
```python
bigFont = {'family':'fantasy', 'color':'blue', 'size':20}
smallFont = {'family':'cursive', 'color':'darkred', 'size':15}
plt.plot(x_data, y_data, marker='P', color='b', ls='dotted', linewidth='2.0', label="Label")
```

## Code Conventions

### Comments & Documentation
- **Intent-focused comments**: Explain why operations are performed, not just what they do
- **Step-by-step annotations**: Use inline comments before logic blocks for clarity
- **Output formatting comments**: Note formatting decisions (e.g., "Remove the index while display values - for clear understanding")

### Code Structure
- Import statements grouped at file start (pandas, numpy, matplotlib)
- Temporary print statements for debugging included in production code
- Descriptive variable names with data type prefixes: `df_` for DataFrames, `np_` for numpy arrays

## Common Tasks & Workflows

### Loading & Processing CSV Data
1. Import pandas
2. Load CSV with absolute path
3. Select required columns using bracket notation
4. Transform column names/display format
5. Output using `to_string()` with formatting options

### Creating Multi-Series Visualizations
1. Prepare multiple numpy arrays
2. Create subplot or overlay lines with distinct markers/colors/styles
3. Define custom fonts in dictionary format
4. Apply to titles and axis labels using `fontdict` parameter
5. Configure x-axis with `xticks()` for meaningful labels
6. Add legend and grid, then show

## Important Notes

- **File Paths**: Currently use absolute paths for CSV files (e.g., `"C:/Workspace/StudentsInformation.csv"`) - consider parameterizing for portability
- **Output Style**: Extensive use of newline characters (`\n`) and print statements for console output - maintain this verbose output pattern
- **Data Assumptions**: Scripts assume well-formed CSV files with expected columns (e.g., 'Age', 'First name', 'Second name', 'Last name')

## Testing

### Test Structure
Unit tests are located in `test_*.py` files using Python's `unittest` framework:
- `test_pandas_read_csv.py`: Tests for CSV loading, data selection, transformations, and calculations
- `test_numpy_plot_visualization.py`: Tests for array creation, plot configuration, and visualization

### Key Testing Patterns
- **Setup/Teardown**: Use `setUp()` for test data and `tearDown()` for cleanup (especially `plt.close('all')` for matplotlib)
- **File Dependencies**: Tests handle missing CSV files gracefully using `self.skipTest()` for skippable assertions
- **Array Validation**: Test array dimensions, data types, and value progressions
- **Matplotlib Objects**: Verify plot objects creation, series consistency, font dictionaries, and axis configuration

### Running Tests
```bash
# Run all tests
python -m unittest discover -s . -p "test_*.py"

# Run specific test file
python -m unittest test_pandas_read_csv

# Run with verbose output
python -m unittest discover -s . -p "test_*.py" -v
```

### Test Coverage Focus
- CSV data loading and column selection
- Data transformations (uppercase conversion, formatting)
- Statistical calculations (mean age)
- Plot object creation with multiple series
- Font and styling configurations
- Axis ticks and labels
- Legend and grid setup

## When Adding New Features

- Maintain educational clarity: keep code readable with inline comments
- Follow the pattern: Import → Load/Prepare → Process → Visualize → Output
- Use consistent font/styling dictionaries for plot customization
- Include meaningful variable names and descriptive output messages
- Add corresponding unit tests in `test_*.py` files following existing patterns
