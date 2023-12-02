# Write a function that takes in the screen width and height, 
# and the window width and height, and returns a string that can be used to center the window on the screen.


def center_screen_geometry(screen_width, 
                          screen_height, 
                          win_width, 
                          win_height):
  x = int((screen_width / 2) - (win_width / 2))
  y = int((screen_height / 2) - (win_height / 2))

  return f"{win_width}x{win_height}+{x}+{y}"