# write your code here
def padel_court_cost(court_type):
    
    if court_type == ("indoor"):
        return 30
    elif court_type == ("outdoor"):
        return 20


def rackets_cost(racket_brand):
   if racket_brand == ("bullpadel"):
    return 100
   elif racket_brand == ("nox"):
    return 140
   elif racket_brand == ("siux"):
    return 200
    
def padel_balls_cost(ball_boxes):
   if ball_boxes == ("1"):
      return 2
   elif ball_boxes ==("2"):
      return 3.5
   elif ball_boxes == ("3"):
    return 5



  
def padel_game_cost():
    
    court_type=input("indoor / outdoor")
    racket_brand=input("bullpadel/nox/siux")
    ball_boxes= input("1/2/3")

    courttype = padel_court_cost(court_type)
    racket = rackets_cost(racket_brand)
    ballbox = padel_balls_cost(ball_boxes)

    print(f"the total cost is {courttype+racket+ballbox} kd")

padel_game_cost()


