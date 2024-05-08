import numpy as np

class Sphere:
    def __init__(self, center, radius, color, ambient, diffuse, specular, shininess):
        self.center = np.array(center)
        self.radius = radius
        self.color = np.array(color) * 255  # Skalowanie kolorów do Pygame

        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess

    def intersect(self, ray_origin, ray_direction):
        #stosuję analityczne rozwiązanie problemu znajdowania punktu przecięcia (można też geometrycznie)
        #https://www.scratchapixel.com/lessons/3d-basic-rendering/minimal-ray-tracer-rendering-simple-shapes/ray-sphere-intersection.html
        oc = ray_origin - self.center
        a = np.dot(ray_direction, ray_direction)
        b = 2.0 * np.dot(oc, ray_direction)
        c = np.dot(oc, oc) - self.radius * self.radius
        delta = b*b - 4*a*c
        if delta < 0:
            return np.inf  # Brak przecięcia
        else:
            return (-b - np.sqrt(delta)) / (2.0 * a) # jest git ale można by też dla jasności zrobić min(t1,t2) czyli wybrać mniejsze z rozwiazan w bardziej widoczny sposób