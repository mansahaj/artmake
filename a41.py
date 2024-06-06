#!/usr/bin/env python
"""Assignment 4 Part 1 Version 3 template"""
print(__doc__)

from typing import IO

class HtmlDocument:
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


class HtmlComponent:
    def __init__(self, tag: str, fname: IO[str]):
        """HtmlComponent constructor"""       
        self.tag: str = tag
        self.file: IO[str] = fname

    def __repr__(self):
        """Returns a string representation of the HtmlComponent"""
        return f"opening tag {self.tag}"
    
class SvgCanvas(HtmlComponent):
    def __init__(self, tag: str, fname: IO[str], width: int, height: int):
        super().__init__(tag, fname)
        self.width: int = width
        self.height: int = height
    
    def open_tag(self):
        self.file.write(f'  <{self.tag} width="{self.width}" height="{self.height}">\n')

    def close_tag(self):
        self.file.write(f"  </{self.tag}>\n")

    """generates the ast necessary"""
    def genArt(self):
        circle_list = [CircleShape((50, 50, 50), (255, 0, 0, 1.0)),
        CircleShape((150, 50, 50), (255, 0, 0, 1.0)),
        CircleShape((250, 50, 50), (255, 0, 0, 1.0)),
        CircleShape((350, 50, 50), (255, 0, 0, 1.0)),
        CircleShape((450, 50, 50), (255, 0, 0, 1.0)),
        CircleShape((50, 250, 50), (0, 0, 255, 1.0)),
        CircleShape((150, 250, 50), (0, 0, 255, 1.0)),
        CircleShape((250, 250, 50), (0, 0, 255, 1.0)),
        CircleShape((350, 250, 50), (0, 0, 255, 1.0)),
        CircleShape((450, 250, 50), (0, 0, 255, 1.0))]

        for c in circle_list: 
            c.write_circle(self.file)
        
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
    """Circle shape, inherits from Shape."""
    def __init__(self, cir: tuple, col: tuple) -> None:
        super().__init__(col)
        self.cx: int = cir[0]
        self.cy: int = cir[1]
        self.rad: int = cir[2]

    def write_circle(self, file):
        style = self.shape_style()
        file.write(f'       <circle cx="{self.cx}" cy="{self.cy}" r="{self.rad}" {style}></circle>\n')

class RectangleShape(Shape):
    """Rectangle shape, inherits from Shape."""
    def __init__(self, rect: tuple, col: tuple) -> None:
        super().__init__(col)
        self.x: int = rect[0]
        self.y: int = rect[1]
        self.width: int = rect[2]
        self.height: int = rect[3]
    
    def write_rectangle(self, file):
        style = self.shape_style()
        file.write(f'<rect x="{self.x}" y="{self.y}" width="{self.width}" height="{self.height}" {style}></rect>\n')

class EllipseShape(Shape):
    """Ellipse shape, inherits from Shape."""
    def __init__(self, ellipse: tuple, col: tuple) -> None:
        super().__init__(col)
        self.cx: int = ellipse[0]
        self.cy: int = ellipse[1]
        self.rx: int = ellipse[2]
        self.ry: int = ellipse[3]
    
    def write_ellipse(self, file):
        style = self.shape_style()
        file.write(f'<ellipse cx="{self.cx}" cy="{self.cy}" rx="{self.rx}" ry="{self.ry}" {style}></ellipse>\n')


def main():
    # Create an instance of HtmlDocument with the file name "test.html" and title "Example Title"
    html_doc = HtmlDocument("a41.html", "a41")

    # Create an instance of SvgCanvas with the tag "svg", the file from html_doc, width 500, and height 300
    svg_test = SvgCanvas("svg", html_doc.file, 500, 300)

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
