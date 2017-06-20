# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random
import util

from game import Agent


class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(
            gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[
            index] == bestScore]
        # Pick randomly among the best
        chosenIndex = random.choice(bestIndices)

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [
            ghostState.scaredTimer for ghostState in newGhostStates]

        basicScore = successorGameState.getScore()

        distanceToFood = map(lambda x: 1.0 / manhattanDistance(x, newPos), newFood.asList())
        foodScore = max([0] + distanceToFood) # foodScore should be more than
        0

        ghostScore = 0

        for ghost in newGhostStates:
          ghostScaredTime = ghost.scaredTimer
          distanceToGhost = util.manhattanDistance(newPos, ghost.getPosition())

          if ghostScaredTime <= 0: # When agent didn't have the pellet.
            ghostScore -= pow(max(7 - distanceToGhost, 0), 2)
          else:
            ghostScore += pow(max(8 - distanceToGhost, 0), 2)

        return basicScore + foodScore + ghostScore



def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)
        self.expanded = 0


class MinimaxAgent(MultiAgentSearchAgent):

    def getAction(self, gameState):
        score_max = -1000
        actionIteration = gameState.getLegalActions()
        for action in actionIteration:
            newGameState = gameState.generateSuccessor(0, action)
            score = self.minValue(newGameState, 0,  1)
            # for the best action that action can generate
            if (score > score_max):
                score_max = score
                bestaction = action
        return bestaction

    def minValue(self, gameState, currentDepth, ghostIndex):
        # terminate state if win, lose, of depth is currentdepth
        if gameState.isLose() or self.depth == currentDepth or gameState.isWin():
            return self.evaluationFunction(gameState)

        # generate needed variables
        LegalActions = gameState.getLegalActions(ghostIndex)
        score_min = 1000
        ghostnumber = gameState.getNumAgents() - 1

        for action in LegalActions:
            # game state for ghosts
            newGameState = gameState.generateSuccessor(ghostIndex, action)
            # for all the ghost agents
            if(ghostIndex < ghostnumber):
                score = self.minValue(newGameState, currentDepth, ghostIndex + 1)
            # for pacman agent
            else:
                score = self.maxValue(newGameState, currentDepth + 1)
            if(score < score_min):
                score_min = score
        return score_min

    def maxValue(self, gameState, currentDepth):
        # terminate state if win, lose, of depth is currentdepth
        if gameState.isLose() or self.depth == currentDepth or gameState.isWin():
            return self.evaluationFunction(gameState)

        # generate needed variables
        LegalActions = gameState.getLegalActions()
        score_max = -1000

        for action in LegalActions:
            if not (action == 'STOP'):
                # game state for pacman
                newGameState = gameState.generateSuccessor(0, action)
                score = self.minValue(newGameState, currentDepth, 1)
                if(score > score_max):
                    score_max = score
        return score_max

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """
    def getAction(self, gameState):
        alpha = -1000
        beta = 1000
        score = -1000

        #generate needed variables    
        legalActions = gameState.getLegalActions()
        score_max = -1000

        for action in legalActions:
            # game state for pacman
            newGameState = gameState.generateSuccessor(0, action)
            # store minValue to score
            score = self.minValue(newGameState, 0,  1, alpha, beta)
            # update the maximum value and best action
            if (score > score_max):
                score_max = score
                bestaction = action
            alpha = max(alpha, score_max)
        return bestaction

    def minValue(self, gameState, currentDepth, ghostIndex, alpha, beta):
        # terminate state if win, lose, of depth is currentdepth
        if gameState.isLose() or self.depth == currentDepth or gameState.isWin():
            return self.evaluationFunction(gameState)

        #generate needed variables    
        score_min = 1000
        LegalActions = gameState.getLegalActions(ghostIndex)
        ghostnumber = gameState.getNumAgents() - 1

        for action in LegalActions:
            # game state for ghosts
            newGameState = gameState.generateSuccessor(ghostIndex, action)
            if(ghostIndex < ghostnumber):
                score = self.minValue(newGameState, currentDepth, ghostIndex + 1, alpha, beta)
            else:
                score = self.maxValue(newGameState, currentDepth + 1, alpha, beta)
            # alpha pruning
            if(score < alpha):
                return score
            elif(score < score_min):
                score_min = score
            beta = min(beta, score)
        return score_min

    def maxValue(self, gameState, currentDepth, alpha, beta):
        # terminate state if win, lose, of depth is currentdepth
        if gameState.isLose() or self.depth == currentDepth or gameState.isWin():
            return self.evaluationFunction(gameState)

        #generate needed variables    
        LegalActions = gameState.getLegalActions()
        score_max = -1000

        for action in LegalActions:
            if not (action == 'STOP'):
                newGameState = gameState.generateSuccessor(0, action)
                pacmanScore = self.minValue(newGameState, currentDepth, 1, alpha, beta)
                if(pacmanScore > beta):
                    return pacmanScore
                elif(pacmanScore > score_max):
                    score_max = pacmanScore
                alpha = max(alpha, pacmanScore)
        return score_max

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        def expectedvalue(gameState, agentindex, depth):
            if gameState.isWin() or gameState.isLose() or depth == 0:
                return self.evaluationFunction(gameState)
            numghosts = gameState.getNumAgents() - 1
            legalActions = gameState.getLegalActions(agentindex)
            numactions = len(legalActions)
            totalvalue = 0
            for action in legalActions:
                nextState = gameState.generateSuccessor(agentindex, action)
                if (agentindex == numghosts):
                    totalvalue += maxvalue(nextState, depth - 1)
                else:
                    totalvalue += expectedvalue(nextState,
                                                agentindex + 1, depth)
            return totalvalue / numactions

        def maxvalue(gameState, depth):
            if gameState.isWin() or gameState.isLose() or depth == 0:
                return self.evaluationFunction(gameState)
            legalActions = gameState.getLegalActions(0)
            bestAction = Directions.STOP
            score = -(float("inf"))
            for action in legalActions:
                prevscore = score
                nextState = gameState.generateSuccessor(0, action)
                score = max(score, expectedvalue(nextState, 1, depth))
            return score
        if gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)
        legalActions = gameState.getLegalActions(0)
        bestaction = Directions.STOP
        score = -(float("inf"))
        for action in legalActions:
            nextState = gameState.generateSuccessor(0, action)
            prevscore = score
            score = max(score, expectedvalue(nextState, 1, self.depth))
            if score > prevscore:
                bestaction = action
        return bestaction


def betterEvaluationFunction(currentGameState):

  """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
  """


  basicScore = currentGameState.getScore()   
  newPos = currentGameState.getPacmanPosition() 
  newGhostStates = currentGameState.getGhostStates()
  newFood = currentGameState.getFood()         
  newCapsule = currentGameState.getCapsules()  

  distanceToFood = map(lambda x: 1.0 / manhattanDistance(x, newPos), newFood.asList())
  foodScore = max(distanceToFood + [0])   

  ghostScore = 0

  for ghost in newGhostStates:
    ghostScaredTime = ghost.scaredTimer
    distanceToGhost = util.manhattanDistance(newPos, ghost.getPosition())

    if ghostScaredTime <= 0: # When agent didn't have the pellet.
      ghostScore -= pow(max(7 - distanceToGhost, 0), 2)
    else:
      ghostScore += pow(max(8 - distanceToGhost, 0), 2)

  return foodScore + ghostScore + basicScore


class ContestAgent(MultiAgentSearchAgent):
    """
      Your agent for the mini-contest
    """

    def getAction(self, gameState):
        """
          Returns an action.  You can use any method you want and search to any depth you want.
          Just remember that the mini-contest is timed, so you have to trade off speed and computation.

          Ghosts don't behave randomly anymore, but they aren't perfect either -- they'll usually
          just make a beeline straight towards Pacman (or away from him if they're scared!)
        """
        util.raiseNotDefined()