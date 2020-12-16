import random
import sys

from bke import MLAgent, is_winner, opponent, validate, RandomAgent, train
 

class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
        

    random.seed(1)

for A in range(1,10):
    for B in range(1,10):
        my_agent = MyAgent(alpha=(0.1*A), epsilon=(0.1*B))
        random_agent = RandomAgent()

        train(my_agent, 3000)
        my_agent.learning = False

        validation_agent = RandomAgent()

        validation_result = validate(agent_x=my_agent, agent_o=validation_agent, iterations=1000)


        if validation_result ["X"] > 0.9:
            print(validation_result ["X"])
            print(A)
            print(B)
            sys.exit()
 

    
