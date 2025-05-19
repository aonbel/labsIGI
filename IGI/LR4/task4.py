# Lab Work 4: Task 4
# Version: 1.0
# Developer: Belavusau Anton
# Date: May 10, 2025

from abc import ABC, abstractmethod
import matplotlib.pyplot as plt

class GeometricFigure(ABC):
    """Abstract base class for geometric figures."""
    def __init__(self, label: str):
        self.label = label

    @abstractmethod
    def area(self) -> float:
        """Calculate the area of the figure."""
        pass

class Color:
    """Class to represent the color of a figure."""
    VALID_COLORS = {"red", "green", "blue", "yellow", "black", "white"}
    
    def __init__(self, color: str):
        self._color = None  
        self.color = color  

    def get_color(self) -> str:
        """Get the color value."""
        return self._color

    def set_color(self, value: str) -> None:
        """Set and validate the color."""
        if value.lower() not in self.VALID_COLORS:
            raise ValueError(f"Invalid color. Allowed colors: {', '.join(self.VALID_COLORS)}")
        self._color = value.lower()

    def del_color(self) -> None:
        """Delete the color (reset to default)."""
        self._color = "black"

    color = property(
        fget=get_color,
        fset=set_color,
        fdel=del_color,
        doc="Property for managing color with validation"
    )

class Rhombus(GeometricFigure):
    """Class representing a rhombus."""
    shape_name = "Rhombus"

    def __init__(self, d1: float, d2: float, color: str, label: str):
        super().__init__(label)
        self.d1 = d1
        self.d2 = d2
        self.color = Color(color)

    def area(self) -> float:
        """Calculate the area of the rhombus."""
        return (self.d1 * self.d2) / 2

    def get_info(self) -> str:
        """Return string with rhombus parameters."""
        return f"{self.shape_name} with diagonals {self.d1} and {self.d2}, color {self.color.color}, area {self.area():.2f}"

    @classmethod
    def get_name(cls) -> str:
        """Get the name of the shape."""
        return cls.shape_name

    def draw(self):
        """Draw a rhombus using Matplotlib."""
        try:
            vertices = [(-self.d1/2, 0), (0, self.d2/2), (self.d1/2, 0), (0, -self.d2/2), (-self.d1/2, 0)]  # Closing the shape
            x_coords, y_coords = zip(*vertices)
            
            plt.figure(figsize=(8, 6))
            
            plt.plot(x_coords, y_coords, color='black')
            
            plt.fill(x_coords, y_coords, color=self.color.color)
            
            plt.text(0, -self.d2/2 - 20, self.label, ha='center', va='center', fontsize=12)
            
            plt.gca().set_aspect('equal', adjustable='box')
            
            margin_x = 20
            margin_y = 30
            plt.xlim(-self.d1/2 - margin_x, self.d1/2 + margin_x)
            plt.ylim(-self.d2/2 - margin_y, self.d2/2 + margin_x)
            
            plt.axis('off')
            
            plt.savefig('rhombus.png')
            
            plt.show()
        
        except Exception as e:
            print(f"Error drawing rhombus with Matplotlib: {e}")