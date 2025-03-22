import numpy as np
from typing import List

def calculate_reactions(length, **forces):
    """
    ** Forces
        'magnitude' : [f1, f2],
        'dists' : [x1, x2]
    

    return Ra, Rb
    """
    r_a : int; r_b : int

    f_is : np.ndarray = np.array(forces['magnitudes'])
    x_is : np.ndarray = np.array(forces['dists'])


    r_b = 1 / length * f_is @ x_is.T
    r_a = f_is.sum() - r_b
    return r_a, r_b

def draw_sfd(**forces):
    x = np.linspace(0, forces['dists'][-1], 100)
    y = np.zeros_like(x)

    temp :int = 0
    for i in range(len(forces['magnitudes']) - 1):
        temp += - forces['magnitudes'][i]
        y += temp * ( x < forces['dists'][i + 1]) * (forces['dists'][i] <= x)
    return y




def draw_bmd(**forces):
    
    x = np.linspace(0, forces['dists'][-1], 100)
    
    
    return x, y

def calculate(
        length : int, 
        magnitudes: List[int],
        distances: List[int],
        r_a_start: int = None,
        r_b_start: int = None,
    ):
    x = np.linspace(0, length, 1000)

    r_a, r_b = calculate_reactions(length, magnitudes=magnitudes, dists=distances)

    magnitudes.insert(0, -r_a)
    distances.insert(0, 0)

    magnitudes.append(-r_b)
    distances.append(length)
    
    shear = draw_sfd(magnitudes=magnitudes, dists=distances)
    
    return x, shear


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    forces = {
        'mags': [1, 2, 3],
        'dist' : [2, 3, 4]
    }
    r_a, r_b = calculate_reactions(length = 9, magnitudes=forces['mags'], dists=forces['dist'])
    forces['mags'].insert(0, -r_a)
    forces['dist'].insert(0, 0)

    forces['mags'].append(-r_b)
    forces['dist'].append(9)
    print(forces)
    x, y = (draw_sfd(magnitudes=forces['mags'], dists=forces['dist']))
    plt.plot(x, y)
    plt.grid()
    plt.savefig("plot.png")