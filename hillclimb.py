import numpy as np
from pymep.realParser import eval

def Continuous_Space_Hill_Climbing(f, v, l, u, a, e):
    
    """
    hill climbing algorithm has the following inputs:

    f=A string that represents a continuous mathematical function of one variable, like "x^2 + 1".
    v=A string that contains the name of the variable in the mathematical function, like "x".
    l=A numerical lower bound.
    u=A numerical upper bound.
    a=The acceleration for the search.
    e=The difference value that terminates the search, like 0.0001.
    """
    
    
    currentPoint = np.random.randint(l,u,10)
    epsilon = e
    stepSize = [1, 1, 1, 1]
    acceleration = a
    candidate=[0,0,0,0]
    candidate[0] = -acceleration
    candidate[1] = -1 / acceleration
    candidate[2] = 1 / acceleration
    candidate[3] = acceleration
    #if s==None:
    #    bestScore = eval(f, 0)
    #else:
    #    bestScore = eval(f, currentPoint)
    bestScore = eval(f, 0)
    
    while True:
        beforeScore = bestScore
        for i in range(len(currentPoint)):
            beforePoint = currentPoint[i]
            bestStep = 0
            for j in range(0,3):
                step = stepSize[i] * candidate[j]
                currentPoint[i] = beforePoint + step
                score = eval(f,currentPoint)
                if score > bestScore:
                    bestScore = score
                    bestStep = step
            if bestStep == 0:
                currentPoint[i] = beforePoint
                stepSize[i] = stepSize[i] / acceleration
            else:
                currentPoint[i] = beforePoint + bestStep
                stepSize[i] = bestStep
        if (bestScore - beforeScore) < epsilon:
            return currentPoint


def main():
    f="x^2 + 1"
    v=x
    l=0
    u=10
    a=1.2
    e=0.0001

    Continuous_Space_Hill_Climbing(f, v, l, u, a, e)

if __name__ == "__main__":
    main()