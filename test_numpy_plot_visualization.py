import unittest
import unittest.mock as mock
import numpy as np
import matplotlib.pyplot as plt


class TestNumpyPlotVisualization(unittest.TestCase):
    """Test suite for numpy array creation and matplotlib visualization"""
    
    def setUp(self):
        """Set up test data before each test"""
        self.np_row_data_1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
        self.np_col_data_1 = np.array([10, 20, 30, 40, 50, 60, 70, 80])
        self.np_row_data_2 = np.array([2, 4, 6, 8, 10, 12, 14, 16])
        self.np_col_data_2 = np.array([10, 20, 30, 40, 50, 60, 70, 80])
    
    def tearDown(self):
        """Clean up matplotlib figures after each test"""
        plt.close('all')
    
    def test_numpy_array_creation(self):
        """Test that numpy arrays are created correctly"""
        self.assertEqual(len(self.np_row_data_1), 8)
        self.assertEqual(len(self.np_col_data_1), 8)
        self.assertTrue(np.array_equal(self.np_row_data_1, np.array([1, 2, 3, 4, 5, 6, 7, 8])))
    
    def test_array_data_types(self):
        """Test that arrays are numpy arrays with correct data types"""
        self.assertIsInstance(self.np_row_data_1, np.ndarray)
        self.assertIsInstance(self.np_col_data_1, np.ndarray)
        self.assertTrue(np.issubdtype(self.np_row_data_1.dtype, np.integer))
    
    def test_array_dimensions_match(self):
        """Test that x and y data arrays have matching dimensions"""
        self.assertEqual(len(self.np_row_data_1), len(self.np_col_data_1))
        self.assertEqual(len(self.np_row_data_2), len(self.np_col_data_2))
    
    def test_linear_progression_array(self):
        """Test array with linear progression"""
        # np_col_data_1 should have consistent intervals of 10
        differences = np.diff(self.np_col_data_1)
        self.assertTrue(np.all(differences == 10))
    
    def test_plot_object_creation(self):
        """Test that plot object is created without errors"""
        try:
            fig, ax = plt.subplots()
            ax.plot(self.np_row_data_1, self.np_col_data_1, marker='P', color='b', 
                   ls='dotted', linewidth=2.0, label="Peter")
            self.assertIsNotNone(fig)
            self.assertIsNotNone(ax)
        except Exception as e:
            self.fail(f"Plot creation failed with error: {e}")
    
    def test_plot_with_multiple_series(self):
        """Test creating plot with multiple data series"""
        try:
            fig, ax = plt.subplots()
            ax.plot(self.np_row_data_1, self.np_col_data_1, marker='P', color='b', 
                   ls='dotted', linewidth=2.0, label="Peter")
            ax.plot(self.np_row_data_2, self.np_col_data_2, marker='p', color='g', 
                   ls='dashdot', linewidth=1.8, label="Rob")
            
            # Check that both lines are in the plot
            lines = ax.get_lines()
            self.assertEqual(len(lines), 2)
        except Exception as e:
            self.fail(f"Multi-series plot creation failed with error: {e}")
    
    def test_font_dictionary_structure(self):
        """Test that font dictionaries are properly formatted"""
        bigFont = {'family': 'fantasy', 'color': 'blue', 'size': 20}
        smallFont = {'family': 'cursive', 'color': 'darkred', 'size': 15}
        
        # Check required font properties exist
        for font_dict in [bigFont, smallFont]:
            self.assertIn('family', font_dict)
            self.assertIn('color', font_dict)
            self.assertIn('size', font_dict)
            self.assertIsInstance(font_dict['size'], int)
    
    def test_plot_title_and_labels(self):
        """Test that plot title and axis labels are set correctly"""
        try:
            fig, ax = plt.subplots()
            ax.plot(self.np_row_data_1, self.np_col_data_1)
            
            bigFont = {'family': 'fantasy', 'color': 'blue', 'size': 20}
            smallFont = {'family': 'cursive', 'color': 'darkred', 'size': 15}
            
            ax.set_title("Students Learning Progress Report", fontdict=bigFont)
            ax.set_xlabel("Weekly Progress", fontdict=smallFont)
            ax.set_ylabel("Number of chapters learned", fontdict=smallFont)
            
            self.assertEqual(ax.get_title(), "Students Learning Progress Report")
            self.assertEqual(ax.get_xlabel(), "Weekly Progress")
            self.assertEqual(ax.get_ylabel(), "Number of chapters learned")
        except Exception as e:
            self.fail(f"Title and label setting failed with error: {e}")
    
    def test_xticks_configuration(self):
        """Test x-axis tick configuration"""
        try:
            fig, ax = plt.subplots()
            ax.plot(self.np_row_data_1, self.np_col_data_1)
            
            tick_val = [2, 4, 6, 8, 10, 12, 14, 16]
            tick_lab = ['week1', 'week2', 'week3', 'week4', 'week5', 'week6', 'week7', 'week8']
            ax.set_xticks(tick_val)
            ax.set_xticklabels(tick_lab)
            
            # Verify ticks are set
            ticks = ax.get_xticks()
            self.assertGreater(len(ticks), 0)
        except Exception as e:
            self.fail(f"X-axis tick configuration failed with error: {e}")
    
    def test_grid_and_legend(self):
        """Test grid and legend addition to plot"""
        try:
            fig, ax = plt.subplots()
            ax.plot(self.np_row_data_1, self.np_col_data_1, label="Peter")
            ax.plot(self.np_row_data_2, self.np_col_data_2, label="Rob")
            ax.grid(True)
            ax.legend()
            
            # Check that legend exists and has entries
            legend = ax.get_legend()
            self.assertIsNotNone(legend)
            self.assertEqual(len(legend.get_texts()), 2)
        except Exception as e:
            self.fail(f"Grid and legend setup failed with error: {e}")
    
    def test_marker_styles(self):
        """Test that different marker styles are valid"""
        valid_markers = ['P', 'p', 'o', 's', '^', 'v', '<', '>', '*', '+', 'x']
        
        for marker in valid_markers:
            try:
                fig, ax = plt.subplots()
                ax.plot(self.np_row_data_1, self.np_col_data_1, marker=marker)
                plt.close(fig)
            except Exception as e:
                self.fail(f"Marker style '{marker}' failed with error: {e}")
    
    def test_line_styles(self):
        """Test that different line styles are valid"""
        line_styles = ['dotted', 'dashdot', '-', '--', '-.', ':']
        
        for ls in line_styles:
            try:
                fig, ax = plt.subplots()
                ax.plot(self.np_row_data_1, self.np_col_data_1, ls=ls)
                plt.close(fig)
            except Exception as e:
                self.fail(f"Line style '{ls}' failed with error: {e}")
    
    def test_data_series_consistency(self):
        """Test that data series follow expected patterns"""
        # First series: simple incremental
        self.assertTrue(np.all(np.diff(self.np_row_data_1) > 0))
        
        # Second series: incremental by 2
        expected_diff_2 = np.array([2, 2, 2, 2, 2, 2, 2])
        actual_diff_2 = np.diff(self.np_row_data_2)
        self.assertTrue(np.array_equal(actual_diff_2, expected_diff_2))


if __name__ == '__main__':
    unittest.main()
