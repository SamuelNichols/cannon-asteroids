import constants
from asteroid import Asteroid

# the goal of this class is simply to track point earned by the player for shooting asteroids and 
class StatsManager():
    def __init__(self):
        self.score = 0
    
    def hit_asteroid(self, asteroid: Asteroid):
        # getting asteroid kind the -1 for list index for asteroid score [small, med, large]
        kind = (asteroid.radius // constants.ASTEROID_MIN_RADIUS) - 1
        self.score += constants.ASTEROID_KILL_SCORES[kind]

    def print_score(self):
        print(f"current score: {self.score}\n")
