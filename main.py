
import numpy as np
import math

# Toto je funkce vygenerovaná umělou funkcí
# Funkce počíta posun po Zeměkouli ze startovních souřadnic o danou vzdálenost daným směrem
def calculate_coordinates_shift(lat, lon, bearing, distance):
    R = 6371000  # Earth's radius in meters
    # Convert inputs to radians
    lat = math.radians(lat)
    lon = math.radians(lon)
    bearing = math.radians(bearing)

    # Calculate the new latitude
    new_lat = math.asin(
        math.sin(lat) * math.cos(distance / R) +
        math.cos(lat) * math.sin(distance / R) * math.cos(bearing)
    )

    # Calculate the new longitude
    new_lon = lon + math.atan2(
        math.sin(bearing) * math.sin(distance / R) * math.cos(lat),
        math.cos(distance / R) - math.sin(lat) * math.sin(new_lat)
    )

    # Convert results back to degrees
    new_lat = math.degrees(new_lat)
    new_lon = math.degrees(new_lon)

    return [new_lat, new_lon]

def calculate_bearing(vector):
    # Extract x and y components
    vx, vy = vector
    # Calculate angle in degrees
    theta = np.arctan2(vx, vy) * (180 / np.pi)
    # Convert to [0, 360] range
    theta = (theta + 360) % 360
    return theta

def main():
    print('Starting point: ')
    start_coords = np.array([float(input('Latitude [decimal]: ')), float(input('Longitude [decimal]: '))])
    print('Final point: ')
    end_coords = np.array([float(input('Latitude [decimal]: ')), float(input('Longitude [decimal]: '))])

    start_coords = np.flip(start_coords)
    end_coords = np.flip(end_coords)

    flight_time = float(input('Flight time [s]: '))
    target_time = float(input('Target time [s]: '))

    vector = end_coords - start_coords
    drone_target_coords = start_coords + vector * (target_time / flight_time)

    bearing = calculate_bearing(vector) - 90.0

    target_coords = calculate_coordinates_shift(drone_target_coords[1],
                                                drone_target_coords[0],
                                                bearing,
                                                50)

    print(f'\nThe target point GPS coordinates are:\n'
          f'Latitude: {target_coords[0]}\n'
          f'Longitude: {target_coords[1]}')

if __name__ == '__main__':
    main()
