#!/usr/bin/python3
# Copyright (c) 2021 Mikayla Cohen, All rights reserved
# BSD License

import argparse
import json
import subprocess

""" terrapod.py """

class Cluster:
  """ Pods Abstraction """
  def __init__(self, filename):
    """ Cluster Constructor """
    self.pods = []
    self.read(filename)

  def build(self):
    """ Build container images """
    for pod in self.pods:
      print('Building & Pulling {0} containers...'.format(pod['name']))
      pod.build()

  def push(self):
    """ Push the images in the cluster to the specified container repository """
    # TODO
    pass

  def read(self, filename):
    """ Read in a cluster config """
    print("Reading '{0}'...".format(filename))
    with open(filename) as pod_file:
      config = json.load(pod_file)
    print(json.dumps(self.pods, indent=2))
    for pod in config:
      pod = Pod(pod['name'])
      
      self.pods.append(pod)

  def restart(self):
    """ Restart the pods """
    self.stop()
    self.start()

  def save(self):
    """ Save the images in the cluster """

  def start(self):
    """ Start the pods in the cluster """
    for pod in self.pods:
      pod.start()

  def stop(self):
    """ Stop the pods in the cluster """
    for pod in self.pods:
      pod.stop()

  def up(self):
    """ Create and start the pods """
    for pod in self.pods['pods']:
      cmd = 'podman pod create --name {0}'.format(pod['name'])
      stdout, stderr = subprocess.Popen(cmd,
              stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()
      print(stdout.decode())
      if stderr:
        print(stderr.decode())

      print('Starting {0} containers...'.format(pod['name']))
      for container in pod['containers']:
        options = '--pod {0}'.format(pod['name'])
        options += ' -h {0}'.format(container['hostname'])
        options += ' -p {0}'.format(container['ports'])

        # TODO: Build volumes up a little better
        options += ' -v {0}'.format(container['volumes'])

        options += ' {0}'.format(container['image'])
        cmd = 'podman -dt {0}'.format(options)
        print(cmd)
        '''
        stdout, stderr = subprocess.Popen(cmd,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()
        print(stdout.decode())
        if stderr:
          print(stderr.decode())
        '''

def Container:
  """ Container Class """
  def __init__(self, name):
    """ Container Constructor """
    self _name = name

  def save(self):
    pass

  def start(self):
    pass

  def stop(self):
    pass

class Pod(name):
  """ Pod Class """
  def __init__(self, name, containers):
    """ Pod Constructor """
    self._name = name
    self.containers = []

  def build():
    """ Build or Pull the containers in the pod """
    print('Building & Pulling {0} containers...'.format(pod['name']))
    for container in self.containers:
      if container['dockerfile']:
        cmd = 'buildah bud {0}'.format(
                container['image'],
                container['containerfile'])
      else:
        cmd = 'podman pull {0}'.format(container['image'])
      print(cmd)
      # TODO: Multi-thread the building of containers
      stdout, stderr = subprocess.Popen(cmd,
              stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()
      print(stdout.decode())
      if stderr:
        print(stderr.decode())

  def save(self):
    """ Save the images of all the containers in the pod """
    pass

  def start(self):
    """ Start all containers in the pod """
    cmd = 'podman start {0}'.format(pod[self.name])

  def stop(stop):
    """ Stop all containers in the pod """
    cmd = 'podman stop {0}'.format(pod[self.name])

def main(args):
  """ Main entry point """
  cluster = Cluster(args.filename)
  cluster.build()

  if args.options('container'):
    cluster.up()

def parse_args():
  """ CLI argument parser """
  parser = argparse.ArgumentParser(description='A podman orechestration CLI client.')
  parser.add_argument('-b', '--build', dest='image')
  parser.add_argument('-f', '--file', dest='filename', required=True)
  parser.add_argument('-p', '--push', dest='repo', required=True)
  parser.add_argument('--restart')
  parser.add_argument('--start')
  parser.add_argument('--stop')
  parser.add_argument('-u', '--up', dest='container')
  return parser.parse_args()

if __name__ == '__main__':
  args = parse_args()
  main(args)

