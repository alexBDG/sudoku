# System imports.
import numpy as np

GRID_1 = np.array([
    [0, 0, 0,   2, 0, 9,   4, 3, 1],
    [8, 1, 0,   0, 6, 0,   0, 0, 0],
    [9, 2, 0,   5, 4, 0,   8, 0, 0],

    [0, 6, 0,   9, 0, 2,   0, 4, 0],
    [0, 0, 0,   4, 1, 0,   5, 0, 0],
    [0, 0, 0,   0, 0, 0,   0, 0, 0],

    [0, 0, 0,   1, 0, 0,   0, 0, 8],
    [2, 0, 0,   0, 0, 7,   0, 0, 0],
    [0, 5, 0,   0, 2, 0,   9, 7, 0],
])

GRID = np.array([
    [5, 1, 0,   2, 0, 0,   0, 3, 6],
    [0, 0, 0,   9, 0, 0,   0, 0, 8],
    [8, 0, 9,   0, 1, 0,   0, 4, 0],

    [2, 5, 0,   0, 0, 0,   0, 9, 0],
    [0, 4, 0,   0, 0, 0,   3, 0, 0],
    [0, 0, 1,   7, 6, 0,   0, 0, 2],

    [0, 6, 3,   0, 0, 4,   0, 0, 9],
    [0, 0, 0,   0, 9, 7,   0, 0, 0],
    [0, 0, 5,   6, 2, 0,   0, 0, 0],
])

FULL_GRID = np.array([
    [5, 1, 4,   2, 7, 8,   9, 3, 6],
    [6, 3, 2,   9, 4, 5,   1, 7, 8],
    [8, 7, 9,   3, 1, 6,   2, 4, 5],

    [2, 5, 6,   4, 3, 1,   8, 9, 7],
    [9, 4, 7,   8, 5, 2,   3, 6, 1],
    [3, 8, 1,   7, 6, 9,   4, 5, 2],

    [7, 6, 3,   1, 8, 4,   5, 2, 9],
    [4, 2, 8,   5, 9, 7,   6, 1, 3],
    [1, 9, 5,   6, 2, 3,   7, 8, 4],
])

IDX = np.array([
    [0, 0, 0,   0, 0, 0,   0, 0, 0],
    [0, 0, 0,   0, 0, 0,   0, 0, 0],
    [0, 0, 0,   0, 0, 0,   0, 0, 0],

    [0, 0, 0,   0, 0, 0,   0, 0, 0],
    [0, 0, 0,   0, 1, 0,   0, 0, 0],
    [0, 0, 0,   0, 0, 0,   0, 0, 0],

    [0, 0, 0,   0, 0, 0,   0, 0, 0],
    [0, 0, 0,   0, 0, 0,   0, 0, 0],
    [0, 0, 0,   0, 0, 0,   0, 0, 0],
])

GRID_1 = np.concatenate([
    np.concatenate([
        GRID_1.reshape(1, 9, 9) == k for k in range(10)
    ], axis=0),
    IDX.reshape(1, 9, 9)
], axis=0).astype("float32")
GRID_1 = np.moveaxis(GRID_1, 0, 2)

GRID = np.concatenate([
    np.concatenate([
        GRID.reshape(1, 9, 9) == k for k in range(10)
    ], axis=0),
    IDX.reshape(1, 9, 9)
], axis=0).astype("float32")
GRID = np.moveaxis(GRID, 0, 2)

FULL_GRID = np.concatenate([
    np.concatenate([
        FULL_GRID.reshape(1, 9, 9) == k for k in range(10)
    ], axis=0),
    IDX.reshape(1, 9, 9)
], axis=0).astype("float32")
FULL_GRID = np.moveaxis(FULL_GRID, 0, 2)
