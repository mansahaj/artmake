#!/usr/bin/env python
"""Assignment 4 Part 1 Version 3 template"""
print(__doc__)

"""importing the necessary libraries"""
from typing import IO
import random

class HtmlDocument:
    """HtmlDocument class"""
    def __init__(self, fname: IO[str], title: str):
        """HtmlDocument constructor"""
        self.file: IO[str] = open(fname, "w")
        self.title: str = title


    def heading(self):
        """adds the heading and opening tag of body"""
        self.file.write(f"""<html>
<head>
    <title>{self.title}</title>
</head>
<body>
""")

    def closing(self):
        """closes the html code and the file"""
        self.file.write(f"""</body>
</html>""")
        self.file.close()

class PyArtConfig:
    """PyArtConfig class containing all the shape configurations"""
    def __init__(self) -> None:
        self.shape_choices: list[int] = [0,3]
        self.x_min: int = 0
        self.x_max: int = 1650
        self.y_min: int = 0
        self.y_max: int = 1040
        self.radius_min: int = 0
        self.radius_max: int = 100
        self.rx_min: int = 10
        self.rx_max: int = 30
        self.ry_min: int = 10
        self.ry_max: int = 30
        self.width_min: int = 10
        self.width_max: int = 100
        self.height_min: int = 10
        self.height_max: int = 100
        self.red_min: int = 100
        self.red_max: int = 255
        self.green_min: int = 100
        self.green_max: int = 255
        self.blue_min: int = 100
        self.blue_max: int = 255
        self.op_min: float = 0
        self.op_max: float = 1
        
    
class RandomShape:
    """RandomShape class to create random shapes to add to the html"""
    def __init__(self, shape: PyArtConfig) -> None:
        self.shape = shape

    def random_gen(self):
        """random_gen() method that creates the random shape numbers"""
        #making choice between 0, 1 or 3
        shape: int = random.choice(self.shape.shape_choices)
        x_point: int = random.randrange(self.shape.x_min, self.shape.x_max+1)
        y_point: int = random.randrange(self.shape.y_min, self.shape.y_max+1)
        radius: int = random.randrange(self.shape.radius_min, self.shape.radius_max+1)
        rx: int = random.randrange(self.shape.rx_min, self.shape.rx_max+1)
        ry: int = random.randrange(self.shape.ry_min, self.shape.ry_max+1)
        width: int = random.randrange(self.shape.width_min, self.shape.width_max+1)
        height: int = random.randrange(self.shape.height_min, self.shape.height_max+1)
        red: int = random.randrange(self.shape.red_min, self.shape.red_max+1)
        green: int = random.randrange(self.shape.green_min, self.shape.green_max+1)
        blue: int = random.randrange(self.shape.blue_min, self.shape.blue_max+1)
        #rand float between 0.0 and 0.1
        op: float = random.random()
        #dictionary consisting of the random attributes
        config_dict: dict = {
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

class Shape:
    """Shape superclass for common attributes and methods."""
    def __init__(self, col: tuple) -> None:
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.opacity: float = col[3]

    def shape_style(self) -> str:
        """Returns a string for the 'fill' and 'fill-opacity' SVG attributes."""
        return f'fill="rgb({self.red},{self.green},{self.blue})" fill-opacity="{self.opacity}"'

class CircleShape(Shape):
    """CircleShape class, inherits from Shape."""
    def __init__(self, cir: tuple, col: tuple) -> None:
        super().__init__(col)
        self.cx: int = cir[0]
        self.cy: int = cir[1]
        self.rad: int = cir[2]

    def write_circle(self, file):
        """write_circle(self, file) method writes the circle shape to the html file using the <circle> tag inside the <svg> tags"""
        #calling the shpae_style form Shape super class to include the colour and opaqueness
        style = self.shape_style()
        #writes the shape to the file along with 2 tabs to follow the HTML writing recommendations
        file.write(f'       <circle cx="{self.cx}" cy="{self.cy}" r="{self.rad}" {style}></circle>\n')

class RectangleShape(Shape):
    """RectangleShape class, inherits from Shape."""
    def __init__(self, rect: tuple, col: tuple) -> None:
        super().__init__(col)
        self.x: int = rect[0]
        self.y: int = rect[1]
        self.width: int = rect[2]
        self.height: int = rect[3]
    
    def write_rectangle(self, file):
        """write_rectangle(self, file) method writes the rectangle shape to the html file using the <circle> tag inside the <svg> tags"""
        style = self.shape_style()
        file.write(f'       <rect x="{self.x}" y="{self.y}" width="{self.width}" height="{self.height}" {style}></rect>\n')

class EllipseShape(Shape):
    """EllipseShape class, inherits from Shape."""
    def __init__(self, ellipse: tuple, col: tuple) -> None:
        super().__init__(col)
        self.cx: int = ellipse[0]
        self.cy: int = ellipse[1]
        self.rx: int = ellipse[2]
        self.ry: int = ellipse[3]
    
    def write_ellipse(self, file):
        """write_ellipse(self, file) method writes the ellipse shape to the html file using the <circle> tag inside the <svg> tags"""
        style = self.shape_style()
        file.write(f'       <ellipse cx="{self.cx}" cy="{self.cy}" rx="{self.rx}" ry="{self.ry}" {style}></ellipse>\n')

class HtmlComponent:
    """creating HtmlComponent super class for components later"""
    def __init__(self, fname: IO[str]):
        self.file: IO[str] = fname

class SvgCanvas(HtmlComponent):
    """SvgCanvas class inherits HtmlComponent super class, for creating an svg canvas for art generation"""
    def __init__(self, fname: IO[str], width: int, height: int):
        super().__init__(fname)
        self.width: int = width
        self.height: int = height
    
    def open_tag(self):
        "open_tag() method opens the svg canvas"
        self.file.write(f'  <svg width="{self.width}" height="{self.height}">\n')

    def close_tag(self):
        "close_tag() method closes the svg canvas"
        self.file.write(f"  </svg>\n")

    def genArt(self):
        """gen_art() method generates art based on the random shape components"""
        #number of shapes to create
        shape_count: int = 2000
        #shape attributs
        shape_config: PyArtConfig = PyArtConfig()
        
        for sc in range(shape_count):
            #generating random shape attributes using the random_gen() method
            shape_generated: RandomShape = RandomShape(shape_config)
            shape_details: dict = shape_generated.random_gen()
            #creates and writes the shape based on shape number, if 0 - circle, if 1 - rectangle, else ellipse
            if shape_details['shape'] == 0:
                circle_gen: CircleShape = CircleShape((shape_details['x_point'], shape_details['y_point'], shape_details['radius']),
                                         (shape_details['red'], shape_details['green'], shape_details['blue'], shape_details['op']))
                circle_gen.write_circle(self.file)

            elif shape_details['shape'] == 1:
                rectangle_gen: RectangleShape = RectangleShape((shape_details['x_point'], shape_details['y_point'], shape_details['width'], shape_details['height']),
                                                 (shape_details['red'], shape_details['green'], shape_details['blue'], shape_details['op']))
                rectangle_gen.write_rectangle(self.file)
                
            else:
                ellipse_gen: EllipseShape = EllipseShape((shape_details['x_point'], shape_details['y_point'], shape_details['rx'], shape_details['ry']),
                                                 (shape_details['red'], shape_details['green'], shape_details['blue'], shape_details['op']))
                ellipse_gen.write_ellipse(self.file)

def main():
    # Create an instance of HtmlDocument with the file name "test.html" and title "Example Title"
    html_doc = HtmlDocument("a433.html", "Random Art generator")

    # Create an instance of SvgCanvas with the tag "svg", the file from html_doc, width 500, and height 300
    svg_test = SvgCanvas(html_doc.file, 600, 400)

    # Add the heading and opening tag of the body to the HTML document
    html_doc.heading()

    # Write the opening tag for the SVG canvas to the file
    svg_test.open_tag()

    # Generate the SVG art and write it to the file
    svg_test.genArt()

    # Write the closing tag for the SVG canvas to the file
    svg_test.close_tag()

    # Close the HTML code and the file
    html_doc.closing()

if __name__ == "__main__":
    main()

