from beamngpy import BeamNGpy, Scenario, Vehicle
from beamngpy.sensors import Camera
import matplotlib.pyplot as plt
import numpy as np

bng = BeamNGpy('localhost', 64256, home='C:\\Users\\hrmha\\Documents\\BeamNG.tech\\BeamNG.tech.v0.21.3.0')
bng.open()

scenario = Scenario(
    'smallgrid',
    'multishot',
    description='Demo of the camera sensor used like a multishot camera'
)


scenario.make(bng)

bng.load_scenario(scenario)
bng.start_scenario()

vehicle = Vehicle(
    'demo_vehicle',
    model = 'etk800',
    colour='green',
    licence='H290601'
)

scenario.add_vehicle(
                        vehicle,
                        pos=(0, 0, 0),
                        rot=(0, 0, 0)
                    )

capPos = np.array([0, 0, 0])
capDir = np.array([0, 0, 0])
capFov = 70
capRes = (512, 512)

cap = Camera(capPos, capDir, capFov, capRes, colour=True)

vehicle.attach_sensor('camara', cap)

img = []

imag = ""

image = cap.decode_image(imag, 512, 512, 3, np.uint8)
img.append(image)

fig, ax = plt.subplots(3, 3, figsize=(30, 30))
for x, row in enumerate(img):
    for y, image in enumerate(row):
        ax[y, x].imshow(np.asarray(image.convert('RGB')))
        ax[y, x].set_aspect('equal', 'datalim')
plt.show()

vehicle.ai_set_mode('span')
input('Hit enter when done...')
