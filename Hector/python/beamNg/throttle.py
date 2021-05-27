from beamngpy import BeamNGpy, Scenario, Vehicle

bng = BeamNGpy('localhost', 64256, home='C:\\Users\\hrmha\\Documents\\BeamNG.tech\\BeamNG.tech.v0.21.3.0')
bng.open()

scenario = Scenario('west_coast_usa', 'demo')


scenario.make(bng)

bng.load_scenario(scenario)
bng.start_scenario()

vehicle = Vehicle(
                    'demo_vehicle',
                    model = 'etk800',
                    colour='green',
                    licence='Hector290601'
                  )

scenario.add_vehicle(
                        vehicle,
                        pos=(-717, 101, 118),
                        rot=(0, 0, 1)
                    )

vehicle.control(throttle=0.075)
