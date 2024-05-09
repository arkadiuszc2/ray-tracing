import numpy as np
import pygame
from scene import Scene
from sphere import Sphere
from light import Light

def render_scene(screen, scene, width, height):
    for x in range(width):
        for y in range(height):
            # Przeliczanie współrzędnych piksela na współrzędne sceny, czyli w scenie używam zakresu [-1, 1], tam określam kolor i dopiero na koniec wracam do realnych wymiarów sceny
            ratio = width / height
            px = (2 * (x + 0.5) / width - 1) * ratio
            py = 1 - 2 * (y + 0.5) / height

            ray_direction = np.array([px, py, -1])  # Zakładamy, że kamera patrzy w kierunku -z, i tak jest w pygame bo sprawdzilem
            ray_direction = ray_direction / np.linalg.norm(ray_direction) # znormalizowany wektor o kierunku zgodnym z padaniem promienia z "oka" kamery
            ray_origin = np.array([0, 0, 1]) # współrzędne "oka" kamery

            color = scene.trace_ray_with_phong(ray_origin, ray_direction, [light])
            color = (color * 255).astype(np.uint8)
            screen.set_at((x, y), color)

# Inicjalizacja Pygame
pygame.init()
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ray Tracing with Phong Model")

# Inicjalizacja sceny
scene = Scene()
sphere = Sphere(center=[0, 0, -1], radius=0.5, color=[1, 0.7, 0.3], ambient = np.array([0.1, 0, 0]), diffuse =  np.array([0.7, 0, 0]), specular = np.array([1, 1, 1]), shininess = 100)
scene.set_object(sphere)
light = Light(position=[5, 5, 5], ambient = np.array([1, 1, 1]), diffuse =  np.array([1, 1, 1]), specular = np.array([1, 1, 1]))

light_positions = [[5, 5, 5], [0, 0, 1], [5, 5, 3], [0, 0, 5], [5, 5, -1], [0, 0, -5]] #skos, skos bliżej, przód, bok, za kamerą
# spheres = [ Sphere(center=[0, 0, -1], radius=0.5, color=[1, 0.7, 0.3], ambient = np.array([0.1, 0, 0]), diffuse =  np.array([0.7, 0, 0]), specular = np.array([1, 1, 1]), shininess = 100),
#             Sphere(center=[0, 0, -1], radius=0.5, color=[0.5, 0.5, 0.5], ambient = np.array([0.1, 0.1, 0.1]), diffuse =  np.array([0.6, 0.6, 0.5]), specular = np.array([0.3, 0.3, 0.3]), shininess = 20), 
#             Sphere(center=[0, 0, -1], radius=0.5, color=[0.7038, 0.27048, 0.0828], ambient = np.array([0.19125, 0.0735, 0.0225]), diffuse =  np.array([0.7038, 0.27048, 0.0828]), specular = np.array([0.256777, 0.137622, 0.086014]), shininess = 12.8),
#             Sphere(center=[0, 0, -1], radius=0.5, color=[0.75164, 0.60648, 0.22648], ambient = np.array([0.24725, 0.1995, 0.0745]), diffuse =  np.array([0.75164, 0.60648, 0.22648]), specular = np.array([0.628281, 0.555802, 0.366065]), shininess = 51.2)
#            ] # eksperymentalny, plastik, miedz, złoto #metal,ściana,plastik,drewno 

spheres = [Sphere(center=[0, 0, -1], radius=0.5, color=[0.75164, 0.60648, 0.22648], ambient = np.array([0.24725, 0.1995, 0.0745]), diffuse =  np.array([0.75164, 0.60648, 0.22648]), specular = np.array([0.628281, 0.555802, 0.366065]), shininess = 51.2)]
running = True
scene_rendered = False
light_change_counter = 1
sphere_mat_change_counter = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Start scene computation") 

                render_scene(screen, scene, width, height)

                print("Computation of scene has ended")

            if event.key == pygame.K_q:
                print("Light position changed - start scene computation") 
                
                light.position = light_positions[light_change_counter % len(light_positions)]
                light_change_counter += 1
                render_scene(screen, scene, width, height)

                print("Computation of scene has ended")
                
            if event.key == pygame.K_m:
                print("Spehere material changed - start scene computation") 
                
                scene.set_object(Sphere(center=[0, 0, -1], radius=0.5, color=[0.75164, 0.60648, 0.22648], ambient = np.array([0.24725, 0.1995, 0.0745]), diffuse =  np.array([0.75164, 0.60648, 0.22648]), specular = np.array([0.628281, 0.555802, 0.366065]), shininess = 40))
                sphere_mat_change_counter += 1
                render_scene(screen, scene, width, height)

                print("Computation of scene has ended")
            #wall
            if event.key == pygame.K_s:
                    print("Spehere material changed - start scene computation") 
                    
                    #scene.set_object(Sphere(center=[0, 0, -1], radius=0.5, color=[1, 0.7, 0.3], ambient=np.array([0.3, 0.3, 0.3]), diffuse=np.array([0.8, 0.8, 0.8]), specular=np.array([0.05, 0.05, 0.05]), shininess=10))
                    scene.set_object(Sphere(center=[0, 0, -1], radius=0.5, color=[0.7, 0.5, 0.3], ambient=np.array([0.2, 0.2, 0.2]), diffuse=np.array([0.5, 0.5, 0.5]), specular=np.array([0.1, 0.1, 0.1]), shininess=20))

                    sphere_mat_change_counter += 1
                    render_scene(screen, scene, width, height)

                    print("Computation of scene has ended")
            #wood
            if event.key == pygame.K_d:
                    print("Spehere material changed - start scene computation") 
                    
                    #scene.set_object(Sphere(center=[0, 0, -1], radius=0.5, color=[0.76, 0.69, 0.5], ambient=np.array([0.2, 0.15, 0.1]), diffuse=np.array([0.76, 0.69, 0.5]), specular=np.array([0.2, 0.2, 0.2]), shininess=50))
                    scene.set_object(Sphere(center=[0, 0, -1], radius=0.5, color=[0.7038, 0.27048, 0.0828], ambient = np.array([0.19125, 0.0735, 0.0225]), diffuse =  np.array([0.7038, 0.27048, 0.0828]), specular = np.array([0.356777, 0.237622, 0.186014]), shininess = 12.8))
                    sphere_mat_change_counter += 1
                    render_scene(screen, scene, width, height)

                    print("Computation of scene has ended")
            #plastic
            if event.key == pygame.K_p:
                    print("Spehere material changed - start scene computation") 
                    
                    #scene.set_object(Sphere(center=[0, 0, -1], radius=0.5, color=[0.5, 0.5, 0.5], ambient = np.array([0.1, 0.1, 0.1]), diffuse =  np.array([0.6, 0.6, 0.5]), specular = np.array([0.3, 0.3, 0.3]), shininess = 20))
                    
                    scene.set_object(Sphere(center=[0, 0, -1], radius=0.5, color=[1, 0.7, 0.3], ambient = np.array([0.1, 0.1, 0.1]), diffuse =  np.array([0.5, 0, 0]), specular = np.array([0.7, 0.6, 0.6]), shininess = 25))
                    sphere_mat_change_counter += 1
                    render_scene(screen, scene, width, height)

                    print("Computation of scene has ended")
        pygame.display.flip()


pygame.quit()
