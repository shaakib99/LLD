from heapq import heappush, heappop
class ElevatorManager:
    def __init__(self, num_elevators: int):
        self.elevators = [Elevator() for i in range(num_elevators)]
    
    def request_elevator(self, floor: int, direction: int):
        for elevator in self.elevators:
            if elevator.direction == direction:
                if (direction == 1 and elevator.pos <= floor) or (direction == -1 and elevator.pos >= floor):
                    elevator.add_destination(floor, direction)
                    return
                
        for elevator in self.elevators:
            if elevator.direction == 0:
                elevator.add_destination(floor, direction)
                elevator.direction = direction
                return

        # If no suitable elevator found, assign to the first elevator
        self.elevators[0].add_destination(floor, direction)  # Default to first elevator
    
    def start(self):
        for elevator in self.elevators:
            elevator.move()

class Elevator:
    def __init__(self) -> None:
        self.pos = 0
        self.direction = 0
        self.maxheap = []
        self.minheap = []
    
    def add_destination(self, floor: int, direction: int) -> None:
        if direction == 1:
            heappush(self.minheap, floor)
        else:
            heappush(self.maxheap, -floor)
    
    def move(self) -> None:
        # while going up
        if self.direction == 1:
            if self.minheap:
                while self.minheap and self.pos > self.minheap[0]:
                    heappop(self.minheap) # Rejecting floors already passed

                if self.minheap:
                    self.pos += self.direction
                    if self.pos == self.minheap[0]: heappop(self.minheap)
                else: 
                    self.direction = 0
            else:
                self.direction = 0
               
        # while going down
        elif self.direction == -1:
            if self.maxheap:
                while self.maxheap and self.pos < -self.maxheap[0]:
                    heappop(self.maxheap) # Rejecting floors already passed
                if self.maxheap:
                    self.pos += self.direction
                    if self.pos == -self.maxheap[0]: heappop(self.maxheap)
                else: 
                    self.direction = 0
            else:
                self.direction = 0

        # while idle
        else:
            if not self.minheap and not self.maxheap: 
                self.direction = 0
                return
            if self.maxheap: 
                if self.pos >= -self.maxheap[0]:
                    self.direction = -1
                else:
                    self.direction = 1
                return
            if self.minheap:
                if self.pos <= self.minheap[0]:
                    self.direction = 1
                else:
                    self.direction = -1
                return
