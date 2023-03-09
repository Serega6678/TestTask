from path_finder import PathFinder3D
import numpy as np

my_path_finder = PathFinder3D() # Feel free to add config args if needed

np.random.seed(41)

start = [0, 0, 0]
stop = [2, 3, 3]
maze_3d = np.array(
    [[[0, 0, 1, 1],
      [0, 1, 1, 1],
      [1, 1, 1, 0],
      [0, 0, 1, 0]],
     [[1, 0, 1, 0],
      [0, 1, 0, 0],
      [0, 1, 1, 0],
      [0, 1, 1, 0]],
     [[1, 0, 1, 0],
      [1, 1, 0, 1],
      [1, 0, 0, 1],
      [0, 0, 1, 0]]
     ]
)


your_output = my_path_finder.find_path(maze=maze_3d, start=start, stop=stop)

print(your_output)
