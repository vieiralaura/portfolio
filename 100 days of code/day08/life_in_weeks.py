# Life in Weeks
# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
# Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x weeks left.
# Where x is replaced with the actual calculated number of weeks the input age has left until age 90.

def life_in_weeks(age):
    years = 90 - age
    weeks = years*52
    print(f"You have {weeks} weeks left")