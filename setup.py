from setuptools import setup

setup(
    name="robot_project",
    version="0.0.1",
    description="funny robot go brrrrrrrr",
    url="https://github.com/itsactuallyluna9/EC-Robot-Project",
    author="Luna",
    author_email="itsactuallyluna9@gmail.com",
    license="none",
    packages=["robot_project"],
    install_requires=[
        "pygame",
        "setuptools",
        "loguru",
    ],
    extras_require={
        "misc": ["black", "autoflake", "isort", "pyinstrument"],
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
    ],
)
