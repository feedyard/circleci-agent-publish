#!/usr/bin/env bash
circleci config pack src > orb.yml
circleci orb validate orb.yml
rm orb.yml
