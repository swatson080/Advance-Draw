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

    middle = (low + high) // 2
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

    while lowPos < len(leftCopy) and highPos < len(rightCopy):

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

# Advance Draw
def advanceDraw(offset, padding, rectangles):
    largestWidth = 0
    largeIndex = 0
    # Used to index into the rectangle array
    lrg = 0

    # Find the rectangle with the largest width and get its index
    for rect in rectangles:
        if rect.width > largestWidth:
            largestWidth = rect.width
            largeIndex = lrg
        lrg += 1

    # Top line - offset
    for it in range(offset):
        print(' ', end='')

    # Draw top line of the widest rectangle
    for it in range(len(rectangles)):
        #print(it, end = '')
        if largeIndex == it:
            for j in range(rectangles[it].length):
                print('*', end = '')
            for j in range(padding):
                print(' ', end = '')

        elif rectangles[it].width == largestWidth:
            for j in range(rectangles[it].length):
                print('*', end = '')
            for j in range(padding):
                print(' ', end = '')

        else:
            for j in range(rectangles[it].length):
                print(' ', end = '')
            for j in range(padding):
                print(' ', end = '')

    print('\n', end = '')

    # Draw the bodies of the rectangles
    # This will include the top line of any other rectangles
    # We need to loop (largestWidth - 2) times
    # On each loop: print the offset, then loop through the rect array
    # each pass through this loop, you will draw the contents of the
    # corresponding rectangle - will need to check if the width is > i.
    # If the width of a rect in the array matches the current value of i
    # That means you found the top line of another rectangle.
    # For each rect, print the padding
    for i in range((largestWidth - 2), 0, -1): #?
        # print the offset
        for j in range(offset):
            print(' ', end = '')

        # loop through the rect array
        for j in range(len(rectangles)):
            if rectangles[j].width == (i + 1) and j != largeIndex:
                for k in range(rectangles[j].length):
                    print('*', end = '')
                for k in range(padding):
                    print(' ', end = '')

            elif rectangles[j].width > i:
                for k in range(rectangles[j].length):
                    if k == 0 or k == (rectangles[j].length - 1):
                        print('*', end = '')
                    else:
                        print(' ', end = '')
                for k in range(padding):
                    print(' ', end = '')

            else:
                for k in range(rectangles[j].length + padding):
                    print(' ', end = '')

        print('\n', end = '')

    if largestWidth == 1: # Do nothing, because you already printed the rect + newline
        pass
    else:
        for z in range(offset):
            print(' ', end = '')

        for i in range(len(rectangles)):
            for j in range(rectangles[i].length):
                print('*', end = '')
            for j in range(padding):
                print(' ', end = '')

    print('\n', end = '')


# Begin main script
rect1 = Rectangle(4, 5)
rect2 = Rectangle(4, 4)
rect3 = Rectangle()
rect4 = Rectangle(4, 3)

rectangles = []
rectangles.append(rect1)
rectangles.append(rect2)
rectangles.append(rect3)
rectangles.append(rect4)

print("ADVANCE DRAW BEFORE SORTING")
advanceDraw(0, 1, rectangles)

print("BEFORE SORTING")
for rect in rectangles:
    rect.drawRect()

sortRect(rectangles, 0, len(rectangles) - 1)

print("\n\nAFTER SORTING")

for rect in rectangles:
    rect.drawRect()

print('\n\nBEGINNING ADVANCE DRAW\n\n')

advanceDraw(0, 1, rectangles)