def CHSolution(winrates, tau, levels):
    payoffs = [[u for u in [(j/50.0)-1 for j in i]] for i in winrates]
    num_actions = []
    for i in range(levels):
        num_actions.append(len(payoffs))
    #List of distribution by level
    distribution = []
    for i in range(levels):
        if i < range(levels[-1]):
            distribution.append((exp(-tau))*(tau**i)/(factorial(i)))
        else:
            distribution.append(1-sum(distribution))
    #strategies
    for i in range(levels):
        if i == 0:
            distribution.append(1/levels)
        else:
            exppayoffperaction = []
            for j in levels:
                denom = distribution

        