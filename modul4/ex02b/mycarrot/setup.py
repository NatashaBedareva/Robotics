from setuptools import find_packages, setup
import os
from glob import glob


package_name = 'mycarrot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
         (os.path.join('share', package_name, 'launch'), glob('launch/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='natalia',
    maintainer_email='bedarevanatasa966@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            
            'turtle_tf2_broadcaster = mycarrot.turtle_tf2_broadcaster:main',
            'carrot_tf2_broadcaster = mycarrot.carrot_tf2_broadcaster:main',
            
            
            'static_target_broadcaster = mycarrot.static_target_broadcaster:main',
            'target_switcher = mycarrot.target_switcher:main',
            'turtle_controller = mycarrot.turtle_controller:main',
            'keyboard_input = mycarrot.keyboard_input:main',
            'turtle_spawner = mycarrot.turtle_spawner:main',
            ],
    },
)
