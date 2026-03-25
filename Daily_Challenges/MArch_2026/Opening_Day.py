def streak_counter(games):
  # Write code below 💖
  if len(games)>0:          # check for null/no input 
      longest_streak =[]    # list to store longest running streaks
      win_streak = 0        # current winning streak    
      for game in games:
        if game =='W':
          win_streak+=1
        elif game=='L':
           longest_streak.append(win_streak)    # updating longest streak on LOSS 
           win_streak=0
        else:
          win_streak=win_streak
      longest_streak.append(win_streak)         # updating longest streak if no LOSS encountered 
      # print(longest_streak)
      return max(longest_streak)                # returning max of the longest_streak
    else:
        return 0

print(streak_counter(["W", "W", "L", "W", "W", "W", "L", "W", "W"]))
print(streak_counter(["W", "W", "R", "W", "W", "L", "W"]))
print(streak_counter(["R", "R", "W", "R", "R", "W", "W", "R", "R", "W", "W", "W", "R"]))
