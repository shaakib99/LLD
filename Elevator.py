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

        # If no suitable elevator found, add to the first idle elevator
        for elevator in self.elevators:
            elevator.add_destination(floor, direction)
            return
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
                self.pos = heappop(self.minheap)
            else:
                self.direction = 0
                if self.maxheap:
                    self.pos = -heappop(self.maxheap)
                    self.direction = -1
        # while going down
        elif self.direction == -1:
            if self.maxheap:
                self.pos = -heappop(self.maxheap)
            else:
                self.direction = 0
                if self.minheap:
                    self.pos = heappop(self.minheap)
                    self.direction = 1