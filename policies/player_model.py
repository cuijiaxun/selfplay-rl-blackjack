import torch
import torch.nn as nn

class PlayerModel(nn.Module):
    def __init__(self,
        state_dim: int,
        action_dim: int,
        hidden_dim: int = 64,
    ):
        super(PlayerModel, self).__init__()
        self.actor = nn.Sequential(
            nn.Linear(state_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, action_dim),
        )

    def forward(self, x):
        return self.actor(x)

    def to_tensor(self, state):
        return torch.tensor(state, dtype=torch.float32)

    def action(self, state, device: str = "cpu"):
        state = self.to_tensor(state).to(device)
        logits = self.forward(state)
        probs = F.softmax(logits, dim=-1)
        dist = torch.distributions.Categorical(probs)
        action = dist.sample()
        return action.item(), dist.log_prob(action)

