#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    storage = {}
    route = [None] * length
    
    for ticket in tickets:
        storage[ticket.source] = ticket.destination
    
    # * REQUIRED DESTINATION FOR FIRST
    next = storage["NONE"]
    
    for index in range(0, length):
        route[index] = next
        next = storage[next]

    return route
