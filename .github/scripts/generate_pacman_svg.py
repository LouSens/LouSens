import svgwrite
import random

# Constants
GRID_WIDTH = 52
GRID_HEIGHT = 7
NUM_GHOSTS = 4
COMMIT_DAYS = []  # TODO: Populate this with actual commit days

# Function to create a basic Pacman maze
def create_maze():
    maze = [[' ' for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    # TODO: Implement maze structure
    return maze

# Function to place Pacman and ghosts randomly
def place_characters(maze):
    pacman_pos = (random.randint(0, GRID_HEIGHT - 1), random.randint(0, GRID_WIDTH - 1))
    maze[pacman_pos[0]][pacman_pos[1]] = 'P'  # P for Pacman
    
    ghosts = []
    for _ in range(NUM_GHOSTS):
        while True:
            ghost_pos = (random.randint(0, GRID_HEIGHT - 1), random.randint(0, GRID_WIDTH - 1))
            if ghost_pos != pacman_pos and ghost_pos not in ghosts:
                ghosts.append(ghost_pos)
                maze[ghost_pos[0]][ghost_pos[1]] = 'G'  # G for Ghost
                break
    return maze, pacman_pos, ghosts

# Function to generate SVG output
def generate_svg(maze):
    dwg = svgwrite.Drawing('.github/pacman/pacman.svg', profile='tiny')
    cell_size = 10
    
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            fill_color = 'black'
            if cell == 'P':
                fill_color = 'yellow'  # Pacman color
            elif cell == 'G':
                fill_color = 'red'  # Ghost color
            elif (y, x) in COMMIT_DAYS:
                fill_color = 'blue'  # Commit days color
            
            dwg.add(dwg.rect(insert=(x * cell_size, y * cell_size), size=(cell_size, cell_size), fill=fill_color))
    
    dwg.save()

def main():
    maze = create_maze()
    maze, pacman_pos, ghosts = place_characters(maze)
    generate_svg(maze)

if __name__ == "__main__":
    main()