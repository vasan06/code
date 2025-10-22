
import numpy as np
import skfuzzy as fuzz

def main():
    x = np.linspace(0, 10, 100)
    A = fuzz.trimf(x, [0, 2, 5])
    B = fuzz.trimf(x, [3, 5, 8])
    
    print("AND:", np.fmin(A, B)[:5])
    print("OR:", np.fmax(A, B)[:5])

if __name__ == "__main__":
    main()