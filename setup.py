from setuptools import setup

setup(
    name="lightremote",
    version="1.0.0",
    packages=[""],
    url="https://github.com/Smonman/lightremote",
    license="MIT",
    author="Simon Josef Kreuzpointner",
    author_email="simonkreuzpointner@gmail.com",
    description="A simple remote control that operates through changes of brightness",
    install_requires=["opencv-python~=4.6.0.66", "mouse~=0.7.1"],
    scripts=["lightremote.py"]
)
