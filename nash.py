# function make_p_combos isn't fully implemented?? check old laptop

import numpy as np

def nash(A_payoffs, B_payoffs, iterations=10000):
    """
    Approximate Nash equilibrium for a two-player game.
    
    Each player's payoffs take the form of an N-by-M numpy array,
    where N is the number of actions the player can take, and
    M is the number of actions their opponent can take. 
    
    All of each player's actions must be assigned a unique, arbitrary
    number from the set {0, 1, ..., N-1}. Entry [i, j] in a player's
    payoff matrix represents the payoff to that player if they choose 
    action i and their opponent chooses action j.
    """
  
    A_actions, B_actions = A_payoffs.shape
    
    # initialize uniform strategies for both players
    A_strategy = [1/float(A_actions)] * A_actions
    B_strategy = [1/float(B_actions)] * B_actions
    
    def get_action(strategy):
        x = np.random.rand()
        a = 0
        while np.sum(strategy[:a+1]) < x:
            a += 1
        return a
    
    #test this (make sure order of strategy matrices is right)
    def EV(own_strategy, opp_strategy, payoffs):
        p_matrix = np.outer(own_strategy, opp_strategy)
        return np.sum(np.multiply(p_matrix, payoffs))
    
    def make_p_combos(actions):
        test_points = np.arange(0, 1.01, 0.01)
        dims = np.meshgrid(*[testpoints for i in range(actions)])
        
    
    [0, 1, 2]
    [0, 1, 2]
    [0, 1, 2]
    
    [0, 0, 0]
    [1, 1, 1]
    [2, 2, 2]
    
    for i in range(iterations):
        A = get_action(A_strategy)
        B = get_action(B_strategy)
        
        A_regret = A_payoffs[:, B] - A_payoffs[A, B]
        A_regret[A_regret < 0] = 0
        A_cumulative_regrets += A_regret
        A_strategy = A_cumulative_regrets / np.sum(A_cumulative_regrets)
        
        B_regret = B_payoffs[:, A] - B_payoffs[B, A]
        B_regret[B_regret < 0] = 0
        B_cumulative_regrets += B_regret
        B_strategy = B_cumulative_regrets / np.sum(B_cumulative_regrets)
        
    return A_strategy, B_strategy
