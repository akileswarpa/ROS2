from setuptools import find_packages, setup

package_name = 'pycode'

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
    maintainer='akileswar',
    maintainer_email='akileswar@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "pyextable = pycode.ir:main",   # This is correct
            "stationtable = pycode.new_robot:main",  # Add a comma here to separate the two entries
            "controltable= pycode.rob_control:main",
            "lidartable = pycode.lidar:main",
            "Autocartable= pycode.autonomousCar:main", 
            "numberPublisher = pycode.numberpublisher:main",
            "numbercounter= pycode.numbercounter:main",
        ],
    },
)
