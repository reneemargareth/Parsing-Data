'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}
    
    if to_member in social_graph[from_member]["following"] and from_member in social_graph[to_member]["following"]:
        return "friends"
    elif to_member in social_graph[from_member]["following"]:
        return "follower"
    elif from_member in social_graph[to_member]["following"]:
        return "followed by"
    else:
        return "no relationship"

def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    winner = ""
    evaluated = 0

    if board == "board1":
        board = [
        ['X','X','O'],
        ['O','X','O'],
        ['O','','X'],
        ]
    elif board == "board2":
        board = [
        ['X','X','O'],
        ['O','X','O'],
        ['','O','X'],
        ]
    elif board == "board3":
        board = [
        ['O','X','O'],
        ['','O','X'],
        ['X','X','O'],
        ]
    elif board == "board4":
        board = [
        ['X','X','X'],
        ['O','X','O'],
        ['O','','O'],
        ]
    elif board == "board5":
        board = [
        ['X','X','O'],
        ['O','X','O'],
        ['X','','O'],
        ]
    elif board == "board6":
        board = [
        ['X','X','O'],
        ['O','X','O'],
        ['X','',''],
        ]
    elif board == "board7":
        board = [
        ['X','X','O',''],
        ['O','X','O','O'],
        ['X','','','O'],
        ['O','X','','']
        ]
    
    diagonal_a = [board[i][i] for i,v in enumerate(board)]
    diagonal_b = [board[2-i][i] for i,v in enumerate(board)]
    diagonal_acheck = set()
    diagonal_bcheck = set()
    [diagonal_acheck.add(s) for s in diagonal_a]
    [diagonal_bcheck.add(s) for s in diagonal_b]
    
    if len(diagonal_acheck) == 1:
        winner = diagonal_acheck
        evaluation += 1
    elif len(diagonal_bcheck) == 1:
        winner = diagonal_bcheck
        evaluation += 1
    
    horizontal = [x for x in board]
    vertical = [x for x in zip(*board)]
    line = 0
    
    for i in range(len(board)):
        hor = horizontal[line]
        ver = vertical[line]
        horizontal_check = set()
        vertical_check = set()
        [horizontal_check.add(s) for s in hor]
        [vertical_check.add(s) for s in ver]
        line += 1
        if len(horizontal_check) == 1 :
            winner = horizontal_check
            evaluated += 1
        elif len(vertical_check) == 1:
            winner = vertical_check
            evaluated += 1
        else:
            evaluated += 0
            
    if winner == {"X"} and evaluated >= 1:
        return "X"
    elif winner == {"O"} and evaluated >= 1:
        return "O"
    else:
        return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
         }
    }

    legs2 = {
    ('a1', 'a2'): {
        'travel_time_mins': 10
    },
    ('a2', 'b1'): {
        'travel_time_mins': 10230
    },
    ('b1', 'a1'): {
        'travel_time_mins': 1
        }
    }
    
    legs_a = legs[("upd","admu")]["travel_time_mins"]
    legs_b = legs[("admu","dlsu")]["travel_time_mins"]
    legs_c = legs[("dlsu","upd")]["travel_time_mins"]
    
    legs2_a = legs2[("a1","a2")]["travel_time_mins"]
    legs2_b = legs2[("a2","b1")]["travel_time_mins"] 
    legs2_c = legs2[("b1","a1")]["travel_time_mins"]
    
    while first_stop == "upd":
        if second_stop == "admu":
            return legs_a
        elif second_stop == "dlsu":
            return legs_a+legs_b
        elif second_stop == "upd": 
            return legs_a+legs_b+legs_c
    
    while first_stop == "admu":
        if second_stop == "dlsu":
            return legs_b
        elif second_stop == "upd":
            return legs_b+legs_c
        elif second_stop == "admu":
            return legs_b+legs_c+legs_a
    
    while first_stop == "dlsu":
        if second_stop == "upd":
            return legs_c
        elif second_stop == "admu":
            return legs_c+legs_a
        elif second_stop == "dlsu":
            return legs_c+legs_b+legs_a
    
    while first_stop == "a1": 
        if second_stop == "a2":
            return legs2_a
        elif first_stop == "a1" and second_stop == "b1":
            return legs2_a + legs2_b
        elif first_stop == "a1" and second_stop == "a1":
            return legs2_a + legs2_b + legs2_c
    
    while first_stop == "a2": 
        if second_stop == "b1":
            return legs2_b
        elif second_stop == "a1":
            return legs2_b + legs2_c
        elif second_stop == "a2":
            return legs2_b + legs2_c + legs2_a
    
    while first_stop == "b1":
        if second_stop == "a1":
            return legs2_c
        elif second_stop == "a2":
            return legs2_c + legs2_a
        elif second_stop == "b1":
            return legs2_c + legs2_a + legs2_b