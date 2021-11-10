# Advance Draw - Stephen Watson 11/9/2021

# Import statements


# Rectangle class
# Defines a rectangle object and provides functions to draw it, e.g. print a rectangle to the screen
class Rectangle:
    # Tracks how many rectangles have been made - static variable
    count = 1

    def __init__(self, length = None, width = None):
        """
        Initializes a rectangle object, and tracks how many have been made
        """

        # Print rectangle info
        #print(f'Rectangle {self.count} reporting for duty')

        # Rectangle ID
        self.id = Rectangle.count
        # Increment count
        Rectangle.count += 1
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

    # __str__() method - print the rectangle object's ID, length, and width
    def __str__(self):
        return 'Rectangle {} reporting -- Length: {} -- Width: {}'.format(self.id, self.length, self.width)

    # Returns the number of Rectangles created
    def getNumRect(self):
        return Rectangle.count

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
    def drawFillRectRpt(self, drawAmt, padding):
        for k in range(self.width):
            for i in range(drawAmt):
                for j in range(self.length):
                    print('*', end = '')
                for p in range(padding):
                    print(' ', end = '')
            print('\n', end = '')


# Begin main script
rect1 = Rectangle(4, 5)

rect1.drawRectRpt(20, 3)
print()
rect1.drawRectRpt(10, 10)
rect1.drawFillRectRpt(20,3)
print()
rect1.drawFillRectRpt(10,10)

# while(True):
#     rect1.drawRectRpt(20, 3)
#     print()
#     rect1.drawRectRpt(10, 10)
#     rect1.drawFillRectRpt(20,3)
#     print()
#     rect1.drawFillRectRpt(10,10)
