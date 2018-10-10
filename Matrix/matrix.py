import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        det = 0
        if self.h == 1:
            det = self.g[0][0]
        elif self.h == 2:
            det = self.g[0][0]*self.g[1][1]-self.g[0][1]*self.g[1][0]
        return det

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
        # TODO - your code here
        tr = sum([self.g[row][row] for row in range(self.w)])
        return tr

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        det = self.determinant()
        tr  = self.trace()
        inv = 0
        if self.w == 1:
            inv = Matrix([[1/self.g[0][0]]])
        else:
            inv = (1/det)*(tr*identity(self.w)-self)
        return inv

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        transpose = []
        #for col in range(self.h):
        #    transpose.append([])
        #for row in range(self.w):
        #    for col in range(self.h):
        #        transpose[col].append(self.g[row][col])
        #return Matrix(transpose)
        
        transpose = list(zip(*self.g))
        return Matrix(transpose)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        result = [[(self.g[row][col] + other.g[row][col]) for col in range(self.h)] for row in range(self.w)]
        return Matrix(result)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        result = [[(-self.g[row][col]) for col in range(self.h)] for row in range(self.w)]
        return Matrix(result)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be sub if the dimensions are the same") 
        result = [[(self.g[row][col] - other.g[row][col]) for col in range(self.h)] for row in range(self.w)]
        return Matrix(result)
    
    def get_row(matrix, row):
        return matrix[row]
    
    def get_col(matrix, col):
        return [matrix[row][col] for row in range(len(matrix))]
    
    def dot_product(v1, v2):
        if len(v1) is not len(v2):
            raise(ValueError, "Vector can only be dot if the length are the same") 
        return sum([v1[i]*v2[i] for i in range(len(v1))])
    
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        if len(self.g[0]) is not len(other.g):
            raise(ValueError, "Matrix can only be mul if the A's col and B's row are the same") 
        result = []
        new_row = len(self.g)
        new_col = len(other.g[0])
        
        for row in range(new_row):
            temp = []
            row_value = Matrix.get_row(self.g, row)
            for col in range(new_col):
                col_value = Matrix.get_col(other.g, col)
                temp.append(Matrix.dot_product(row_value, col_value))
            result.append(temp)
        return Matrix(result)
    
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        result = None
        if isinstance(other, numbers.Number):
            
            #   
            # TODO - your code here
            #
            result = [[self.g[i][j]*other for j in range(self.h)] for i in range(self.w)]
        return Matrix(result)