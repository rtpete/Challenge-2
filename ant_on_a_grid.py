import turtle
import sys


class AntOnAGrid:
    def __init__(self, K):
        """
        Initializes the AntOnAGrid class and defines all functionality necessary to run the simulation

        Args:
            K (int): The number of steps the ant will take
        """
        self.k = int(K)

        # Initialize the screen window
        self.window = turtle.Screen()
        self.window.bgcolor('white')
        self.window.screensize(600, 600)

        # Initialize the grid to track square colors
        self.grid = {}

        # Initialize the turtle representing the ant on the square
        self.ant_on_square = turtle.Turtle()
        self.ant_on_square.shape('square')
        self.ant_on_square.shapesize(1)
        self.ant_on_square.speed('fastest')

        # Set the step size for each move of the ant
        self.ant_step = 20

        # Initialize the position variable to track the ant's coordinates on the grid
        self.position = self.get_ant_coordinates(self.ant_on_square)

        # Start the ant's movement
        self.move_ant(self.k, self.position, self.grid, self.ant_on_square, self.ant_step)

    def move_ant(self, k: int, position: tuple, grid: dict, ant: turtle.Turtle, step: int):
        """
        Move the ant on the grid for a specified number of steps

        Args:
            k (int): Number of steps for the ant to take
            position (tuple): Current coordinates of the ant
            grid (dict): Dictionary to track square colors on the grid
            ant (turtle.Turtle): Turtle representing the ant
            step (int): Size of each step the ant takes
        """
        # Only move K number of steps
        for _ in range(k):
            if position not in grid or grid[position] == 'white':

                # If the ant is on a white square, change the square to black
                ant.fillcolor('black')

                # Add the black square to the window screen
                ant.stamp()
                # Update the grid dictionary to keep track of which squares are black
                self.change_square_color(grid, ant, 'black')

                # If the ant is on a white square, turn clockwise 90 degrees and move forward
                ant.right(90)
                ant.forward(step)

                # Update the position variable to evaluate the next step
                position = self.get_ant_coordinates(ant)

            elif grid[position] == 'black':

                # If the ant is on a black square, change the square to white
                ant.fillcolor('white')

                # Add the white square to the window screen
                ant.stamp()
                # Update the grid dictionary to keep track of which squares are white
                self.change_square_color(grid, ant, 'white')

                # If the ant is on a black square, turn counter-clockwise 90 degrees and move forward
                ant.left(90)
                ant.forward(step)

                # Update the position variable to evaluate the next step
                position = self.get_ant_coordinates(ant)

    def change_square_color(self, grid: dict, ant: turtle.Turtle, color: str):
        """
        Updates the grid dictionary to keep track of which coordinates have black or white squares

        Args:
            grid (dict): Dictionary to track square colors on the grid
            ant (turtle.Turtle): Turtle representing the ant
            color (str): Color to set the square
        """
        grid[self.get_ant_coordinates(ant)] = color

    def get_ant_coordinates(self, ant: turtle.Turtle) -> tuple:
        """
        Get the current coordinates of the ant.

        Args:
            ant (turtle.Turtle): Turtle representing the ant

        Returns:
            tuple: Current coordinates of the ant
        """
        ant_coordinates = (round(ant.xcor()), round(ant.ycor()))
        return ant_coordinates


if __name__ == "__main__":
    # Get the number of steps from the command line input
    try:

        number_of_steps = int(sys.argv[1])
    except Exception as e:
        print(f"Error: {e}")
        print("Enter a positive integer k in the following format: python ant_on_a_grid.py {k}")
        sys.exit(1)

    # Begin the simulation
    ant = AntOnAGrid(number_of_steps)

    # Keep the window open at the end of the simulation
    turtle.done()
