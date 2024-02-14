from setuptools import find_packages, setup

package_name = 'toxic_hardware'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pumas',
    maintainer_email='robletes062901@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'controller = toxic_hardware.controller:main',
            'motor_interface = toxic_hardware.motor_interface:main',
            'servo_interface = toxic_hardware.servo_interface:main',
            'oled_interface = toxic_hardware.oled_interface:main',
            'blinkers_interface = toxic_hardware.blinkers_interface:main',
            'automate = toxic_hardware.automate:main'
        ],
    },
)
