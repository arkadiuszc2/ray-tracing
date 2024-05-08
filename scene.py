import numpy as np

class Scene:
    def __init__(self):
        self.object = None

    def set_object(self, obj):
        self.object = obj
    
    def trace_ray_with_phong(self, ray_origin, ray_direction, lights):
        nearest_object = None
        min_t = np.inf


        t = self.object.intersect(ray_origin, ray_direction)
        if t and 0 < t < min_t:
            min_t = t
            nearest_object = self.object

        if nearest_object is None:
            return np.zeros(3)  # brak przecięć z obiektem, więc kolor piksela to kolor tła, domyślnie czarny


        # Punkt przecięcia
        hit_point = ray_origin + min_t * ray_direction
        normal = (hit_point - nearest_object.center) / nearest_object.radius

        color = np.zeros(3)
        view_dir = -ray_direction
        for light in lights:
            light_dir = (light.position - hit_point)
            light_distance = np.linalg.norm(light_dir)
            light_dir /= light_distance

            # Składnik ambient
            color +=light.ambient * nearest_object.ambient
            
            # Składnik diffuse
            diff = max(np.dot(light_dir, normal), 0)
            color += light.diffuse * nearest_object.diffuse * diff
            
            # Składnik specular
            reflect_dir = 2 * normal * np.dot(light_dir, normal) - light_dir
            spec = np.dot(reflect_dir, view_dir)
            if spec > 0:
                color += light.specular * nearest_object.specular * (spec ** nearest_object.shininess)

        return np.clip(color, 0, 1)  # ogranicz wartości kolorów do [0, 1]