from abc import ABC, abstractmethod

class LlmProvider(ABC):
    @abstractmethod
    async def solve_tsp(self, coordinates: list) -> list:
        """Returns the ordered list of node IDs"""
        pass