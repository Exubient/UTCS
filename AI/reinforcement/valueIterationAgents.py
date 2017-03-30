# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        for loop in range(self.iterations):
            value_dict = util.Counter()
            mdp_list = mdp.getStates()
            for state in mdp_list:
                #check if the agents isTerminal
                if not mdp.isTerminal(state):
                    #make counter_dict and tuple for possible actions
                    counter_dict = util.Counter()
                    actions_tuple = mdp.getPossibleActions(state)
                    #iterate and get qValue
                    for action in actions_tuple:
                        counter_dict[action] = self.computeQValueFromValues(state, action)
                    #get max of the counter_dict values
                    value_dict[state] = max(counter_dict.values())
            #make a copy and update values
            self.values = value_dict.copy()  


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        state_tuple=self.mdp.getTransitionStatesAndProbs(state,action)
        return_count=0

        # iterate over the state_tuple
        for index in state_tuple:
            # get probability, reward, value and discount
            probability = index[1]
            reward = self.mdp.getReward(state,action,index[0])
            value = self.values[index[0]]
            discount = self.discount
            # simple substitution
            return_count += probability * (discount * value + reward)
        # return the count
        return return_count

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        actions=self.mdp.getPossibleActions(state)
        values_dict = util.Counter()
        
        # check conditions and return None if len == 0 or state is Terminal
        if len(actions) == 0 or self.mdp.isTerminal(state):
            return None
  
        #iterate and get qvalues
        for action in actions:
            values_dict[action] = self.computeQValueFromValues(state, action)
        #return max with argMax() from util.py
        return values_dict.argMax() 

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
