def hello_name(user_name):
    return "hello " + user_name

def first_odds():
    for number in range(1, 101, 2):
        print(number)
    return None
def max_num_in_list(a_list):
 return max(a_list) if a_list else None

def is_leap_year(a_year):
   return (a_year % 4 == 0 and a_year % 100 != 0) or (a_year % 400 == 0)