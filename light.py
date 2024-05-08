import numpy as np

class Light:
    def __init__(self, position, ambient, diffuse, specular):
        self.position = np.array(position)
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
