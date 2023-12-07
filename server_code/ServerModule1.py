import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def submit(NAME,AGE,NUMBER,ADDRESS,PERSONAL_TRAINER,SPORT_YOU_LIKE):
  app_tables.sport.add_row(NAME=NAME,AGE=AGE,NUMBER=NUMBER,ADDRESS=ADDRESS,PERSONAL_TRAINER=PERSONAL_TRAINER,SPORT_YOU_LIKE=SPORT_YOU_LIKE)
  anvil.email.send(to="chambial10752@gmail.com", subject="Response from anvil app", 
                   text=f"Feedback from {NAME}: Age is {AGE} and They Live at : {ADDRESS} . Personal Traning required : {PERSONAL_TRAINER} . Sport You Selected {SPORT_YOU_LIKE}")
  
  