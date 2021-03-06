class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return ((2 * self.width) + (2 * self.height))
    
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** 0.5)
    
    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return 'Too big for picture.'
        
        else:
            picture = ''
            largo_asteriscos = '*' * self.width

            for i in range(self.height):
                picture += f'{largo_asteriscos}\n'
            
            return picture
    
    def get_amount_inside(self, figura):
        cabe_width = self.width // figura.width
        cabe_heigth = self.height // figura.height
        return cabe_width * cabe_heigth

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
    def __init__(self, largo):
        self.width = largo
        self.height = largo
    
    def set_side(self, side):
        self.width = side
        self.height = side
    
    def __str__(self):
        return f'Square(side={self.width})'
