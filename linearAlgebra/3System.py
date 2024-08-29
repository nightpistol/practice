import numpy as np

A = np.array([[-1,0,2],[3,1,1,],[1,-4,0]])
B=np.array([1,-2,2])

solution = np.linalg.solve(A,B)
print('the solution is :')
print(f'x={solution[0]}')
print(f'y={solution[1]}')
print(f'z={solution[2]}')