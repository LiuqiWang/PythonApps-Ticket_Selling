#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 19:34:04 2018

@author: lukie
"""

'''
# Create a SCRUM project management board that helps to build a ticket selling application.
# SCRUM project management tool recommendation: Trello
'''
TICKET_PRICE = 10
tickets_remaining = 100
SERVICE_CHARGE = 2
user_list = []

# User class for keeping track of users.
class User:
    def __init__ (self, name=None, age=None):
        self.name = name
        self.age = age

# Get user details and register them as an object of a class.
def start_application():
    name = input("What is your name? ")
    age = input("What is your age?")
    for user in user_list:
        if name == user.name:
            print("Welcome back ", name)
            print("There are {} tickets remaining.".format(tickets_remaining))
            num_tickets = input("How many tickets would you like? ")
            try:
                num_tickets = int(num_tickets)
                if num_tickets > tickets_remaining:
                    raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
            except ValueError as err: print("Oh no, we ran into an issue. Please try again.")
        else:
            user_list.append(User(name, age))
            print("Hello ", name)
            print("There are {} tickets remaining.".format(tickets_remaining))
            num_tickets = input("How many tickets would you like? ")
            try:
                num_tickets = int(num_tickets)
                if num_tickets > tickets_remaining:
                    raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
            except ValueError as err: print("Oh no, we ran into an issue. Please try again.")

# create calculate_price function
def calculate_price(number_of_tickets):
    ## create a new constant for the $2 service charge
    ## add service charge to our due
    return number_of_tickets * TICKET_PRICE + SERVICE_CHARGE

# run this code continuously until we run out of tickets.
## when tickets_remaining goes to 0, it will be false
while tickets_remaining >= 1:
    # Output how many tickets remaining using the tickets_remaining variable.
    print("There are {} tickets remaining.".format(tickets_remaining))

    # Gather the user's name and assign it to a new variable.
    name = input("What is your name? ")

    # I should be able to request a certain amount of tickets and be told the total cost, so i can determine if I want to purchase the tickets.
    ## Prompt the user by name and ask how many tickets they would like.
    num_tickets = input("How many tickets would you like? ")
    ## Expect a ValueError to happen and handle it appropriately... remember to test it out!
    try:
        num_tickets = int(num_tickets)
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err: print("Oh no, we ran into an issue. Please try again.")

    else:
        ## Calculate the price (#tickets * price) and assign it to a variable.
        total_price = calculate_price(num_tickets)
        ## Output the price to the screen.
        print("Hello, {}".format(name) + ", your total is {}.".format(total_price))

        # As a user, I should be able to confirm my order, so I do not accidently purchase more tickets than intended.
        ## Prompt user if they want to proceed. Y/N?
        should_proceed = input("Do you want to proceed? (Y/N) ")
        ## If they want to proceed.
        if should_proceed.lower() in ("y", "yes","y.","yes."):
            ## Print out to the screen SOLD to confirm the order.
            ## TODO: Gather credit card info and process it.
            print("SOLD!")
            ## and then decrement the tickets remaining by the number of tickets purchased.
            tickets_remaining -= num_tickets
        ## otherwise Thank them by name.
        else: print("Thank you anyway, {}.".format(name))



# Fixing the logical flow of data in the application.
if __name__ == '__main__':
    start_application()


# notify users of soldouts
print("Sorry, the tickets are all sold out.")

'''
comment: current weakness is print the ValueError. Do not understand quite well on error message.
'''
