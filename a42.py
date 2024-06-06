#!/usr/bin/env python
"""Assignment 4 part 2, makes a table of random integers"""
print(__doc__)

import random

class PyArtConfig:
    def __init__(self) -> None:
        """PyArtConfig class containing all the shape configurations"""
        self.shape_choices: list[int] = [0,1,3]
        self.x_min: int = 0
        self.x_max: int = 500
        self.y_min: int = 0
        self.y_max: int = 500
        self.radius_min: int = 0
        self.radius_max: int = 100
        self.rx_min: int = 10
        self.red_max: int = 30
        self.ry_min: int = 10
        self.ry_max: int = 30
        self.width_min: int = 10
        self.width_max: int = 100
        self.height_min: int = 10
        self.height_max: int = 100
        self.red_min: int = 0
        self.red_max: int = 255
        self.green_min: int = 0
        self.green_max: int = 255
        self.blue_min: int = 0
        self.blue_max: int = 255
        self.op_min: float = 0
        self.op_max: float = 1
    
class RandomShape:
    def __init__(self, shape: PyArtConfig) -> None:
        """RandomShape class to create random shapes to add to the html"""
        self.shape = shape

    def random_gen(self):
        """random_gen() method that creates the random shape numbers"""
        shape: int = random.choice(self.shape.shape_choices)
        x_point: int = random.randrange(self.shape.x_min, self.shape.x_max+1)
        y_point: int = random.randrange(self.shape.y_min, self.shape.y_max+1)
        radius: int = random.randrange(self.shape.radius_min, self.shape.radius_max+1)
        rx: int = random.randrange(self.shape.rx_min, self.shape.red_max+1)
        ry: int = random.randrange(self.shape.ry_min, self.shape.ry_max+1)
        width: int = random.randrange(self.shape.width_min, self.shape.width_max+1)
        height: int = random.randrange(self.shape.height_min, self.shape.height_max+1)
        red: int = random.randrange(self.shape.red_min, self.shape.red_max+1)
        green: int = random.randrange(self.shape.green_min, self.shape.green_max+1)
        blue: int = random.randrange(self.shape.blue_min, self.shape.blue_max+1)
        #rand float between 0.0 and 0.1
        op: float = random.random()
        config_dict = {
            "shape": shape,
            "x_point": x_point,
            "y_point": y_point,
            "radius": radius,
            "rx": rx,
            "ry": ry,
            "width": width,
            "height": height,
            "red": red,
            "green": green,
            "blue": blue,
            "op": op
        }
        return config_dict
    
    def __str__(self) -> str:
        # Generate a random configuration
        config = self.random_gen()
        # Return a formatted string representation of the configuration
        return (
            f"Shape: {config['shape']}\n"
            f"X Point: {config['x_point']}\n"
            f"Y Point: {config['y_point']}\n"
            f"Radius: {config['radius']}\n"
            f"RX: {config['rx']}\n"
            f"RY: {config['ry']}\n"
            f"Width: {config['width']}\n"
            f"Height: {config['height']}\n"
            f"Red: {config['red']}\n"
            f"Green: {config['green']}\n"
            f"Blue: {config['blue']}\n"
            f"Opacity: {config['op']}\n"
        )
        

    def as_Part2_line(self) -> str:
        # Initialize the table header with column names
        table_rand: str = f"CNT SHA{' '*5}X{' '*5}Y{' '*3}RAD{' '*4}RX{' '*4}RY{' '*5}W{' '*5}H{' '*5}R{' '*5}G{' '*5}B{' '*4}OP\n"
        # Loop to generate and print ten rows with the random configurations
        for i in range(10):
            # Generate a random configuration
            config = self.random_gen()
            # Format the row with the generated configuration
            formatted_row = (f"{i:>3} {config['shape']:>3} "
                    f"{config['x_point']:>5} {config['y_point']:>5} "
                    f"{config['radius']:>5} {config['rx']:>5} "
                    f"{config['ry']:>5} {config['width']:>5} "
                    f"{config['height']:>5} {config['red']:>5} "
                    f"{config['green']:>5} {config['blue']:>5} "
                    f"{config['op']:>5.1f}")
            # Add the formatted row to the table
            table_rand += f'{formatted_row}\n'

        # Return the final table as a string
        return table_rand

    def as_svg(self) -> str:
        # Generate a random configuration
        config = self.random_gen()
        # Check the shape type
        if config['shape'] == 0:
            # If the shape is a circle, return the SVG representation of a circle
            return f'<circle cx="{config["x_point"]}" cy="{config["y_point"]}" r="{config["radius"]}" fill="rgb({config["red"]},{config["green"]},{config["blue"]})" fill-opacity="{config["op"]}"></circle>'
        
        elif config['shape'] == 1:
            # If the shape is a rectangle, return the SVG representation of a rectangle
            return f'<rect x="{config["x_point"]}" y="{config["y_point"]}" width="{config["width"]}" height="{config["height"]}" fill="rgb({config["red"]},{config["green"]},{config["blue"]})" fill-opacity="{config["op"]}"></rect>'

        else:
            # If the shape is an ellipse, return the SVG representation of an ellipse
            return f'<ellipse cx="{config["x_point"]}" cy="{config["y_point"]}" rx="{config["rx"]}" ry="{config["ry"]}" fill="rgb({config["red"]},{config["green"]},{config["blue"]})" fill-opacity="{config["op"]}"></ellipse>'

def main():
    config: PyArtConfig = PyArtConfig()
    shape = RandomShape(config)
    print(shape.as_Part2_line())

if __name__ == "__main__":
    main()


