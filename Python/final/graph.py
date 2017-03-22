
from random import uniform


class MarkovChainNode(object):
    def __init__(self,  value, token = None):
        self.state = token
        self.next_states = []
        self.value = value

    def get_next_state(self):
        probability = uniform(0, 1)
        for next_states_index in self.next_states:
            if probability <= next_states_index[1]:
                return next_states_index[0]
            else:
                probability -= next_states_index[1]
                
    def set_next_state(self, node, probability):
        self.next_states.append((node, probability))
        self.next_states.sort(key = lambda probability: probability[1], reverse=True)


class MarkovChainGraph(object):
    def __init__(self):
        self.state_dict = {}

    def add_node(self, value, token):
        self.state_dict[value] = MarkovChainNode(value, token)

    def __getitem__(self, value):
        return self.state_dict[value]


