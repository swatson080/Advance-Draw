# Advance Draw - Stephen Watson 11/9/2021
# TODO: test comparison functions

# Import statements


# Rectangle class
# Defines a rectangle object and provides functions to draw it, e.g. print a rectangle to the screen
class Rectangle:
    # Tracks how many rectangles have been made - static variable
    count = 0

    def __init__(self, length = None, width = None):
        """
        Initializes a rectangle object, and tracks how many have been made
        """

        # Rectangle ID
        # Increment count
        Rectangle.count += 1

        self.id = Rectangle.count

        # Initialize rectangle dimensions
        if length != None and width != None:
            self.length = length
            self.width = width
        elif length != None:
            self.length = length
            self.width = length
        else:
            self.length = 1
            self.width = 1

        # Print rectangle info
        #print(self)

    # __str__() method - print the rectangle object's ID, length, and width
    def __str__(self):
        return 'Rectangle {} reporting -- Length: {} -- Width: {}'.format(self.id, self.length, self.width)

    # Overload comparison operators

    # Overload the < operator
    def __lt__(self, rect2):
        if (self.width < rect2.width) or (self.width == rect2.width and self.length < rect2.length):
            return True
        else:
            return False

    # Overload the <= operator
    def __le__(self, rect2):
        if (self.width <= rect2.width) or (self.width == rect2.width and self.length <= rect2.length):
            return True
        else:
            return False

    # Overload the > operator
    def __gt__(self, rect2):
        if (self.width > rect2.width) or (self.width == rect2.width and self.length > rect2.length):
            return True
        else:
            return False

    # Overload the >= operator
    def __ge__(self, rect2):
        if (self.width >= rect2.width) or (self.width == rect2.width and self.length >= rect2.length):
            return True
        else:
            return False

    # Returns the number of Rectangles created
    def getNumRect(self):
        return Rectangle.count

    # Drawing functions

    # Draws a rectangle of dimensions length and width
    def drawRect(self, includeInfo = False):
        if(includeInfo):
            print(self)
        # Top row
        for i in range(self.length):
            print('*', end='')

        # Move down if width > 1
        if self.width > 1:
            print('\n', end='')

        for i in range(self.width - 2):
            for j in range(self.length):
                if j == 0 or j == self.length - 1:
                    print('*', end='')
                else:
                    print(' ', end='')

            print('\n', end='')

        if self.width > 1:
            for i in range(self.length):
                print('*', end='')

        print('\n', end='')

    # Draws the same rectangle multiple times across the screen
    # drawAmt: number of times to draw the rectangle
    # padding: the amount of space between the rectangles
    def drawRectRpt(self, drawAmt = 1, padding = 1):
        # Draw the top row
        for k in range(drawAmt):
            for i in range(self.length):
                print('*', end='')
            for i in range(padding):
                print(' ', end = '')

        # Move down one line
        print('\n', end = '')

        # Draw the middle
        for k in range(self.width-2):
            for i in range(drawAmt):
                for j in range(self.length):
                    if j == 0 or j == self.length - 1:
                        print('*', end = '')
                    else:
                        print(' ', end = '')
                for p in range(padding):
                    print(' ', end = '')

            print('\n', end = '')

        # Draw the bottom row
        if self.width > 1:
            for k in range(drawAmt):
                for i in range(self.length):
                    print('*', end = '')
                for i in range(padding):
                    print(' ', end = '')

        print('\n', end = '')

    # Draws a filled rectangle
    def drawFillRect(self):
        for i in range(self.width):
            for j in range(self.length):
                print('*', end = '')
            print('\n', end = '')

        print('\n', end = '')

    # Draws a filled rectangle repeatedly across the screen
    # drawAmt: the number of times to draw the rectangle
    # padding: the amount of space between rectangles
    def drawFillRectRpt(self, drawAmt = 1, padding = 1):
        for k in range(self.width):
            for i in range(drawAmt):
                for j in range(self.length):
                    print('*', end = '')
                for p in range(padding):
                    print(' ', end = '')
            print('\n', end = '')

# Takes an array of rectangle objects and sorts them by size (left to right)
# Implements mergesort
def sortRect(rectangles, low, high):
    if low >= high:
        return

    middle =(low + high) // 2
    sortRect(rectangles, low, middle)
    sortRect(rectangles, middle+1, high)
    merge(rectangles, low, high, middle)

def merge(rectangles, low, high, middle):
    # Make copies of each array
    leftCopy = rectangles[low:middle+1]
    rightCopy = rectangles[middle+1:high+1]

    # Pointers
    lowPos = 0
    highPos = 0
    sortedIndex = low

    while lowPos <len(leftCopy) and highPos < len(rightCopy):

        if leftCopy[lowPos] <= rightCopy[highPos]:
            rectangles[sortedIndex] = leftCopy[lowPos]
            lowPos += 1

        else:
            rectangles[sortedIndex] = rightCopy[highPos]
            highPos += 1

        sortedIndex += 1

    while lowPos < len(leftCopy):
        rectangles[sortedIndex] = leftCopy[lowPos]
        lowPos += 1
        sortedIndex += 1

    while highPos < len(rightCopy):
        rectangles[sortedIndex] = rightCopy[highPos]
        highPos += 1
        sortedIndex += 1




# Begin main script
rect1 = Rectangle(4, 5)
rect2 = Rectangle(44, 4)
rect3 = Rectangle()

rectangles = []
rectangles.append(rect1)
rectangles.append(rect2)
rectangles.append(rect3)

print("BEFORE SORTING")
for rect in rectangles:
    rect.drawRect()

sortRect(rectangles, 0, len(rectangles) - 1)

print("\n\nAFTER SORTING")

for rect in rectangles:
    rect.drawRect()
