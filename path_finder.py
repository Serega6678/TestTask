from copy import deepcopy
import typing as tp

import numpy as np

Point = tp.List[int]


class PathFinder3D:
    def __init__(self) -> None:
        pass

    def find_path(self, maze: np.ndarray, start: Point, stop: Point) -> tp.List[Point]:
        assert len(maze.shape) == 3, "Maze must have 3 dimensions"
        visited = np.zeros_like(maze).astype("bool")
        best_path = []
        cur_path = []

        def _dfs(cur_point: Point) -> None:
            cur_path.append(cur_point)

            if cur_point == stop:
                if len(best_path) == 0 or len(cur_path) < len(best_path):
                    best_path[:] = deepcopy(cur_path)
            else:
                visited[cur_point[0], cur_point[1], cur_point[2]] = True

            for next_point in self.next_possible_points(maze, cur_point):
                if not visited[next_point[0], next_point[1], next_point[2]]:
                    _dfs(next_point)

            cur_path.pop()

        _dfs(start)
        return best_path



    @staticmethod
    def next_possible_points(maze: np.ndarray, point: Point) -> tp.List[Point]:
        next_points = []
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                for z in [-1, 0, 1]:
                    if abs(x) + abs(y) + abs(z) == 1:
                        next_point = [point[0] + x, point[1] + y, point[2] + z]
                        dim_x, dim_y, dim_z = maze.shape
                        if 0 <= next_point[0] < dim_x and 0 <= next_point[1] < dim_y and 0 <= next_point[2] < dim_z \
                                and not maze[next_point[0], next_point[1], next_point[2]]:
                            next_points.append(next_point)
        return next_points
