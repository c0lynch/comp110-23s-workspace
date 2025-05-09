"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730620941"


class Simpy:
    values: list[float]

    def __init__(self, vals: list[float]) -> None:
        self.values = vals

    def __str__(self) -> str:
        """Makes things a lot easier."""
        return f"Simply({self.values})"
         
        #Having some trouble with this one
    
    def fill(self, value: float, rep: int) -> None:
        count: int = 0
        for x in self.values:
            if x == value:
                count += 1
        rep -= count
        for x in range(0, (rep - 1)):
            self.values.append(value)


    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """This creates a list with a range and step."""
        self.values = []
        
        #if not step:
            #step = 1.0
        x: float = start
        while x < stop:
            
            self.values.append(x)
            x += step
        while x > stop:
            
            
            self.values.append(x)
            x += step

        
            #trouble here as well
    
    def sum(self) -> float:
        y: float = 0.0
        for x in self.values:
            y += x
        return y
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        z: int = 0
        if isinstance(rhs, Simpy):
            x: Simpy = Simpy([])
            while z < len(self.values):
                x.values.append(rhs.values[z] + self.values[z])
                z += 1
            return x
        else:
            y: Simpy = Simpy([])
            while z < len(self.values):
                y.values.append(rhs + self.values[z])
                z += 1
            return y

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        z: int = 0
        if isinstance(rhs, Simpy):
            x: list[float] = []
            while z < len(self.values):
                x.append(rhs.values[z] ** self.values[z])
                z += 1
            return x
        else:
            y: list[float] = []
            while z < len(self.values):
                y.append(rhs ** self.values[z])
                z += 1
            return y 
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        z: int = 0
        if isinstance(rhs, Simpy):
            x: list[bool] = []
            while z < len(self.values):
                x.append(self.values[z] == rhs.values[z])
                z += 1
            return x
        else:
            y: list[bool] = []
            while z < len(self.values):
                y.append(self.values[z] == rhs)
                z += 1
            return y
        
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        z: int = 0
        if isinstance(rhs, Simpy):
            x: list[bool] = []
            while z < len(self.values):
                x.append(self.values[z] > rhs.values[z])
                z += 1
            return x
        else:
            y: list[bool] = []
            while z < len(self.values):
                y.append(self.values[z] > rhs)
                z += 1
            return y
    
    #def __getitem__(self, rhs: int) -> float:
        return self.values[rhs]
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        z: int = 0
        if isinstance(rhs, list):
            x: Simpy = Simpy([])
            while z < len(self.values):
                if rhs[z]:
                    x.values.append(self.values[z])
                z += 1
            return x
        else:
            return self.values[rhs]







    # TODO: Your constructor and methods will go here.