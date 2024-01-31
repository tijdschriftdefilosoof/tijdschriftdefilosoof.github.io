"""
A module to find the highest numbered PDF file in a directory.

This module provides a function that scans a specific directory ('./pdf')
for PDF files named with a natural number (like '1.pdf', '2.pdf', etc.),
and finds the one with the highest number in its filename.

Dependencies:
    os: To interact with the file system.
    re: To use regular expressions for pattern matching in filenames.

Functions:
    find_highest_numbered_pdf(): Returns the highest number found in the
                                 filenames of the PDF files within the './pdf'
                                 directory. Returns 0 if no matching files are found.
"""
import os
import re


def find_highest_numbered_pdf() -> int:
    """
    Scan './pdf' directory for the highest number in files named 'number.pdf'.

    This function searches for files in './pdf' that match the pattern where
    'number' is a natural number (e.g., '1.pdf', '2.pdf', etc.). It finds the
    file with the highest number in its name.

    Returns:
        int: The highest number found among the PDF files. Returns 0 if no
             matching files are found.
    """
    # Regular expression for 'number.pdf' format
    regex = re.compile(r'^(\d+)\.pdf$')

    max_number = 0  # Initialize to 0 if no files are found
    # Iterate over files in './pdf'
    for filename in os.listdir("./pdf"):
        # Check for 'number.pdf' format
        if match := regex.match(filename):
            # Update max_number to the larger value
            max_number = max(max_number, int(match.group(1)))

    return max_number

