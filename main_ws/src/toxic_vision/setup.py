from setuptools import find_packages, setup

package_name = 'toxic_vision'

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
    maintainer_email='pumas@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'kinect_publisher = toxic_vision.kinect_publisher:main',
            'async_kinect_publisher = toxic_vision.async_kinect_publisher:main',
            'kinect_subscriber = toxic_vision.kinect_subscriber:main',
            'webcam_subscriber = toxic_vision.webcam_sub:main',
            'webcam_publisher = toxic_vision.webcam_pub:main',
            'color_selector = toxic_vision.color_selector:main',
            'lane_detector = toxic_vision.lane_detector:main',
            'lane_tracker = toxic_vision.lane_tracker:main',
        ],
    },
)
