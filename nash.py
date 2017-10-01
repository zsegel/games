import numpy as np

def nash(A_payoffs, B_payoffs, iterations=20000):
  """
  Approximate Nash equilibrium for a normal-form, two-player game.
  
  Each player's payoffs take the form of an N-by-M numpy array,
  where N is the number of actions the player can take, and
  M is the number of actions their opponent can take. 
  
  All of each player's actions must be assigned a unique, arbitrary
  number from the set {0, 1, ..., N-1}. Entry [i, j] in a player's
  payoff matrix represents the payoff to that player if they choose 
  action i and their opponent chooses action j."""
  
  A_actions, B_actions = A_payoffs.shape
  
  # initialize strategies for both players
  A_strategy = [1/float(A_actions)] * A_actions
  B_strategy = [1/float(B_actions)] * B_actions
  
  def get_action(strategy):
    x = np.random.rand()
    
    a = 0
    while np.sum(strategy[:a+1]) < x:
      a += 1
      
    return a
    
    A_cumulative_regrets = np.zeros
    A_norm_sum = 0
    
    B_cumulative_regrets = [0] * B_actions
    B_norm_sum = 0
    
    for i in range(iterations):
      A = get_action(A_strategy)
      B = get_action(B_strategy)
      
      A_regret 
    
    
                 
  
  # regret = what you could have gotten - what you got
