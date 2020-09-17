def CHSolution(winrates, tau, levels):
    payoffs = [[u for u in [(j/50.0)-1 for j in i]] for i in winrates]
    num_actions = []
    for i in range(levels):
        num_actions.append(len(payoffs))
    distribution = []
    for i in range(levels):
        if i < range(levels[-1]):
            for i in num_actions:
                if i == 0:
                    distribution.append(1/levels)
            distribution.append((exp(-tau))*(tau**levels)/(factorial(levels)))
        else:
            distribution.append(1-sum(distribution))
    for 
            
        