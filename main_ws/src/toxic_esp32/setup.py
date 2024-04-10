from setuptools import find_packages, setup

package_name = 'toxic_esp32'

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
    maintainer='omarironvv',
    maintainer_email='omarironvv@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'servo_controller= toxic_esp32.node_degrees:main',
            'led_controller= toxic_esp32.led_configuration_node:main',
            'esp32_controller= toxic_esp32.esp32_node:main',
        ],
    },
)
