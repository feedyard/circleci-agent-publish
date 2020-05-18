<div align="center">
	<p>
		<img alt="CircleCI Logo" src="https://raw.githubusercontent.com/ThoughtWorks-DPS/di-circleci-remote-docker/master/img/circle-circleci.svg?sanitize=true" width="75" />
	</p>
  <h3>feedyard orbs</h3>
  <h1>orb-executor-tools</h1>
  ![feedyard](https://circleci.com/gh/feedyard/orb-executor-tools.svg?style=shield) ![CircleCI Orb Version](https://img.shields.io/badge/endpoint.svg?url=https://badges.circleci.io/orb/feedyard/executor-tools)  ![Software License](https://img.shields.io/badge/license-MIT-blue.svg)  
  <h5>an sdlc orb for circleci docker image executors </h5>
</div>
<br />

Example private registry workflow: (see [orb registry](https://circleci.com/orbs/registry/orb/feedyard/executor-tools) for detailed examples)

```yaml
---
version: 2.1

orbs:
  executor-tools: feedyard/executor-tools@0.4.1
  snyk: snyk/snyk@0.0.10

on-push-master: &on-push-master
  branches:
    only: /master/
  tags:
    ignore: /.*/

on-tag-master: &on-tag-master
  branches:
    ignore: /.*/
  tags:
    only: /.*/

workflows:
  version: 2

  my-circleci-executor-image-pipeline:
    jobs:
      - executor-tools/dev-release:
          registry: quay.io
          registry-login: QUAY_ROBOT_USERNAME
          registry-password: QUAY_ROBOT_TOKEN
          image: myorg/my-circleci-executor
          after_build:
            - snyk/scan:
                docker-image-name: myorg/my-circleci-executor:$CIRCLE_SHA1
                organization: myorg
                fail-on-issues: true
                monitor-on-build: false
          filters: *on-push-master
      - executor-tools/publish:
          registry: quay.io
          registry-login: QUAY_ROBOT_USERNAME
          registry-password: QUAY_ROBOT_TOKEN
          image: myorg/my-circleci-executor
          filters: *on-tag-master
```

Workflows assume:

* Trunk based development (TBD)
* Versioned released are triggered/managed by tagging

_Incorporates concepts from circleci/docker-publish@0.1.2_
