import numpy as np

# Define the GRANTHAM DISTANCE matrix as a dictionary
GRANTHAM_DISTANCE_MATRIX = {
    'A': {'A': 0,   'R': 0.5, 'N': 1.0, 'D': 1.0, 'C': 0.5, 'Q': 1.0, 'E': 1.0, 'G': 0.5, 'H': 1.0, 'I': 1.0, 'L': 1.0, 'K': 0.5, 'M': 1.0, 'F': 1.5, 'P': 1.0, 'S': 0.5, 'T': 0.5, 'W': 1.5, 'Y': 1.5, 'V': 0.5},
    'R': {'A': 0.5, 'R': 0,   'N': 0.5, 'D': 1.0, 'C': 1.0, 'Q': 0.5, 'E': 0.5, 'G': 1.0, 'H': 0.5, 'I': 1.0, 'L': 1.0, 'K': 0.5, 'M': 1.0, 'F': 1.5, 'P': 1.0, 'S': 1.0, 'T': 1.0, 'W': 1.5, 'Y': 1.5, 'V': 1.0},
    'N': {'A': 1.0, 'R': 0.5, 'N': 0,   'D': 0.5, 'C': 1.0, 'Q': 0.5, 'E': 0.5, 'G': 1.0, 'H': 1.0, 'I': 1.0, 'L': 1.0, 'K': 1.0, 'M': 1.0, 'F': 1.5, 'P': 1.0, 'S': 0.5, 'T': 0.5, 'W': 1.5, 'Y': 1.5, 'V': 1.0},
    'D': {'A': 1.0, 'R': 1.0, 'N': 0.5, 'D': 0,   'C': 1.0, 'Q': 1.0, 'E': 0.5, 'G': 1.0, 'H': 1.0, 'I': 1.5, 'L': 1.5, 'K': 1.0, 'M': 1.5, 'F': 1.5, 'P': 1.0, 'S': 0.5, 'T': 0.5, 'W': 1.5, 'Y': 1.5, 'V': 1.0},
    'C': {'A': 0.5, 'R': 1.0, 'N': 1.0, 'D': 1.0, 'C': 0,   'Q': 1.5, 'E': 1.5, 'G': 1.0, 'H': 1.5, 'I': 1.5, 'L': 1.5, 'K': 1.5, 'M': 1.0, 'F': 1.5, 'P': 1.0, 'S': 1.0, 'T': 1.0, 'W': 1.5, 'Y': 1.5, 'V': 1.5},
    'Q': {'A': 1.0, 'R': 0.5, 'N': 0.5, 'D': 1.0, 'C': 1.5, 'Q': 0,   'E': 0.5, 'G': 1.0, 'H': 1.0, 'I': 1.0, 'L': 1.0, 'K': 0.5, 'M': 1.0, 'F': 1.5, 'P': 1.0, 'S': 1.0, 'T': 1.0, 'W': 1.5, 'Y': 1.5, 'V': 1.0},
    'E': {'A': 1.0, 'R': 0.5, 'N': 0.5, 'D': 0.5, 'C': 1.5, 'Q': 0.5, 'E': 0,   'G': 1.0, 'H': 1.0, 'I': 1.0, 'L': 1.0, 'K': 0.5, 'M': 1.0, 'F': 1.5, 'P': 1.0, 'S': 1.0, 'T': 1.0, 'W': 1.5, 'Y': 1.5, 'V': 1.0},
    'G': {'A': 0.5, 'R': 1.0, 'N': 1.0, 'D': 1.0, 'C': 1.0, 'Q': 1.0, 'E': 1.0, 'G': 0,   'H': 1.0, 'I': 1.5, 'L': 1.5, 'K': 1.0, 'M': 1.0, 'F': 1.5, 'P': 1.0, 'S': 0.5, 'T': 0.5, 'W': 1.5, 'Y': 1.5, 'V': 1.0},
    'H': {'A': 1.0, 'R': 0.5, 'N': 1.0, 'D': 1.0, 'C': 1.5, 'Q': 1.0, 'E': 1.0, 'G': 1.0, 'H': 0,   'I': 1.5, 'L': 1.5, 'K': 0.5, 'M': 1.0, 'F': 1.5, 'P': 1.0, 'S': 1.0, 'T': 1.0, 'W': 1.5, 'Y': 1.5, 'V': 1.0},
    'I': {'A': 1.0, 'R': 1.0, 'N': 1.0, 'D': 1.5, 'C': 1.5, 'Q': 1.0, 'E': 1.0, 'G': 1.5, 'H': 1.5, 'I': 0,   'L': 0,   'K': 1.0, 'M': 0,   'F': 0,   'P': 1.0, 'S': 1.0, 'T': 1.0, 'W': 1.5, 'Y': 1.5, 'V': 0},
    'L': {'A': 1.0, 'R': 1.0, 'N': 1.0, 'D': 1.5, 'C': 1.5, 'Q': 1.0, 'E': 1.0, 'G': 1.5, 'H': 1.5, 'I': 0,   'L': 0,   'K': 1.0, 'M': 0,   'F': 0,   'P': 1.0, 'S': 1.0, 'T': 1.0, 'W': 1.5, 'Y': 1.5, 'V': 0},
    'K': {'A': 0.5, 'R': 0.5, 'N': 1.0, 'D': 1.0, 'C': 1.5, 'Q': 0.5, 'E': 0.5, 'G': 1.0, 'H': 0.5, 'I': 1.0, 'L': 1.0, 'K': 0,   'M': 1.0, 'F': 1.5, 'P': 1.0, 'S': 1.0, 'T': 1.0, 'W': 1.5, 'Y': 1.5, 'V': 1.0},
    'M': {'A': 1.0, 'R': 1.0, 'N': 1.0, 'D': 1.5, 'C': 1.0, 'Q': 1.0, 'E': 1.0, 'G': 1.0, 'H': 1.0, 'I': 0,   'L': 0,   'K': 1.0, 'M': 0,   'F': 0,   'P': 1.0, 'S': 1.0, 'T': 1.0, 'W': 1.5, 'Y': 1.5, 'V': 0},
    'F': {'A': 1.5, 'R': 1.5, 'N': 1.5, 'D': 1.5, 'C': 1.5, 'Q': 1.5, 'E': 1.5, 'G': 1.5, 'H': 1.5, 'I': 0,   'L': 0,   'K': 1.5, 'M': 0,   'F': 0,   'P': 1.0, 'S': 1.5, 'T': 1.5, 'W': 0,   'Y': 0,   'V': 1.0},
    'P': {'A': 1.0, 'R': 1.0, 'N': 1.0, 'D': 1.0, 'C': 1.0, 'Q': 1.0, 'E': 1.0, 'G': 1.0, 'H': 1.0, 'I': 1.0, 'L': 1.0, 'K': 1.0, 'M': 1.0, 'F': 1.0, 'P': 0,   'S': 1.0, 'T': 1.0, 'W': 1.5, 'Y': 1.5, 'V': 1.0},
    'S': {'A': 0.5, 'R': 1.0, 'N': 0.5, 'D': 0.5, 'C': 1.0, 'Q': 1.0, 'E': 1.0, 'G': 0.5, 'H': 1.0, 'I': 1.0, 'L': 1.0, 'K': 1.0, 'M': 1.0, 'F': 1.5, 'P': 1.0, 'S': 0,   'T': 0.5, 'W': 1.5, 'Y': 1.5, 'V': 1.0},
    'T': {'A': 0.5, 'R': 1.0, 'N': 0.5, 'D': 0.5, 'C': 1.0, 'Q': 1.0, 'E': 1.0, 'G': 0.5, 'H': 1.0, 'I': 1.0, 'L': 1.0, 'K': 1.0, 'M': 1.0, 'F': 1.5, 'P': 1.0, 'S': 0.5, 'T': 0,   'W': 1.5, 'Y': 1.5, 'V': 1.0},
    'W': {'A': 1.5, 'R': 1.5, 'N': 1.5, 'D': 1.5, 'C': 1.5, 'Q': 1.5, 'E': 1.5, 'G': 1.5, 'H': 1.5, 'I': 1.5, 'L': 1.5, 'K': 1.5, 'M': 1.5, 'F': 0,   'P': 1.5, 'S': 1.5, 'T': 1.5, 'W': 0,   'Y': 1.0, 'V': 1.5},
    'Y': {'A': 1.5, 'R': 1.5, 'N': 1.5, 'D': 1.5, 'C': 1.5, 'Q': 1.5, 'E': 1.5, 'G': 1.5, 'H': 1.5, 'I': 1.5, 'L': 1.5, 'K': 1.5, 'M': 1.5, 'F': 0,   'P': 1.5, 'S': 1.5, 'T': 1.5, 'W': 1.0, 'Y': 0,   'V': 1.5},
    'V': {'A': 0.5, 'R': 1.0, 'N': 1.0, 'D': 1.0, 'C': 1.5, 'Q': 1.0, 'E': 1.0, 'G': 1.0, 'H': 1.0, 'I': 0,   'L': 0,   'K': 1.0, 'M': 0,   'F': 1.0, 'P': 1.0, 'S': 1.0, 'T': 1.0, 'W': 1.5, 'Y': 1.5, 'V': 0}
}