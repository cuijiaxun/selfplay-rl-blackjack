# Basic dealer policy for blackjack in las vegas style

# Dealer Policy:

# Hit < 17

# Stand ≥ 17

# (Maybe hit soft 17)

# No splitting, no doubling, no surrender

# Act after all players

# Reveal blackjack early (if peek rule)

class BasicDealerPolicy:
    """
    Las Vegas dealer policy:
    - Hit until reaching 17 or above
    - Stand on soft 17 (A+6)
    """

    def choose_action(self, hand):
        hard, soft = hand.values()

        # Soft 17 = soft == 17 and hard == 7
        soft_17 = (soft == 17 and hard != 17)

        if soft_17:
            return "stand"

        if soft < 17:
            return "hit"

        return "stand"