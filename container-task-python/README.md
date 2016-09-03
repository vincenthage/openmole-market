# Execution of Docker images using the ContainerTask #

This workflow shows how to use Docker images with OpenMOLE.

In particular, this example uses the `frolvlad/alpine-python3` Docker image (the lightest image with python3) to execute a Python script and return a result inside a text file.

## What does it work with ##

The ContainerTask works in general with Open Container Initiative images, which include Docker images.

## How to get a Docker image archive ##

Two ways: download it or build it.

### to download one: ###
Search for the image that interests you:
    $ sudo docker search <tags>

Then download it:
    $ sudo docker pull <image>

### to build one: ###
Create your own Dockerfile (look for tutorials), then:
    $ sudo docker build -t <nameimage> .

### to get the archive: ###
Once the image is loaded by Docker, get the archive using `save`:
$ sudo docker save <image> > my-docker-image.tar

You can then upload this archive to the workflow, and use it in the same way the python3 archive is used in this example.
