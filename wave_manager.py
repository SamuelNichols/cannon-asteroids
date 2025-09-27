import pygame

# the goal of this class is to run the game in waves and scale the difficulty each time
# 
# track waves and lives
# 
# the first wave starts with 12 asteroid score (large = 3, medium = 2, small = 1)
#   spawn an asteroid of random size from large to small every second and decrement score
#   increase score by 4 every turn
# 
# at the beginning of a new wave print that on the center of the screen and give dont spawn
# before or or after the message for a second or 2
# 
# at wave multiples yet to be decided start spawning ufo's (not yet implemented)
# early waves large, later small
#
# functionality to reset game / waves / and stats
