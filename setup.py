from setuptools import setup


def readfile(filename):
    with open(filename, 'r+') as f:
        return f.read()


setup(
    name="lightremote",
    version="1.0.0",
    packages=[""],
    url="https://github.com/Smonman/lightremote",
    license=readfile("LICENSE"),
    author="Simon Josef Kreuzpointner",
    author_email="simonkreuzpointner@gmail.com",
    description="A simple remote control that operates through changes of brightness",
    long_description=readfile("README.md"),
    install_requires=["opencv-python~=4.6.0.66", "mouse~=0.7.1"],
    scripts=["lightremote.py"],
    entry_points={
        'console_scripts': [
            'lightremote = lightremote:handle_args'
        ]
    },
)
