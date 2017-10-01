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
  
  
