#!/bin/bash

python train_model.py

docker build -t ml-flask .
