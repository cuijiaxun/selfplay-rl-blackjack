# define the training loop
# load the policy
# rollout the policy and collect learning batches
# update the policy
# repeat the process for a number of epochs
# report training metrics
from algorithms.reinforce import REINFORCEPolicy
from envs.blackjack.basic_dealer_policy import BasicDealerPolicy
from envs.blackjack.env import BlackjackEnv

policys = {
    "player_policy": REINFORCEPolicy(),
    "dealer_policy": BasicDealerPolicy(),
}

env = BlackjackEnv()

def train():
    pass

if __name__ == "__main__":
    train()