#!/bin/bash

for f in $(bash -c ls); do masscan -c $f; done
