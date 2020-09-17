def level_k_probabilities_2(k,player,lamda=0.56, lamda2 = 0.05):
    n=len(normal_form_game_player)
    if k == 0:
        probs=[]
        for i in range(n):
            probs.append((1.0/n))
        probs=tuple(probs)
        return probs
    if player == 0:
        sum_action=[]
        for i in range(n):
            temp_sum = 0
            for j in range(n):
                temp_sum = temp_sum + level_k_probabilities_1(k-1, (player+1) % 2,lamda2)[j] * normal_form_game_player[i][j][0]
            temp_sum = np.exp(lamda * temp_sum)
            sum_action.append(temp_sum)
        probs=[]
        for i in range(n):
            temp_prob = sum_action[i]/sum(sum_action)
            probs.append(temp_prob)
        probs=tuple(probs)
        return probs
    else:
        sum_action = []
        for i in range(n):
            temp_sum = 0
            for j in range(n):
                temp_sum = temp_sum + level_k_probabilities_1(k - 1, (player + 1) % 2,lamda2)[j] * \
                           normal_form_game_player[j][i][1]
            temp_sum = np.exp(lamda * temp_sum)
            sum_action.append(temp_sum)
        probs = []
        for i in range(n):
            temp_prob = sum_action[i] / sum(sum_action)
            probs.append(temp_prob)
        probs = tuple(probs)
        return probs