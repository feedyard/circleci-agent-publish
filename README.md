<div align="center">
	<p>
		<img alt="CircleCI Logo" src="https://raw.githubusercontent.com/ThoughtWorks-DPS/di-circleci-remote-docker/master/img/circle-circleci.svg?sanitize=true" width="75" />
	</p>
  <h3>feedyard orbs</h3>
  <h1>orb-executor-tools</h1>
  <a href="https://app.circleci.com/pipelines/github/feedyard/orb-executor-tools"><img src="https://circleci.com/gh/feedyard/orb-executor-tools.svg?style=shield"></a> <a href="https://circleci.com/orbs/registry/orb/feedyard/executor-tools"><img src="https://img.shields.io/badge/endpoint.svg?url=https://badges.circleci.io/orb/feedyard/executor-tools"></a> <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/github/license/feedyard/orb-executor-tools"></a>
  <h5>an sdlc orb for circleci docker image executors </h5>
</div>
<br />

Example workflow: (see [orb registry](https://circleci.com/orbs/registry/orb/feedyard/executor-tools) for detailed examples)

```yaml
---
version: 2.1

orbs:
  executor-tools: feedyard/executor-tools@dev:2.0.0

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
  di-circleci-base-image-pipeline:
    jobs:
      - executor-tools/dev-release:
          shell: secrethub run -- /bin/sh -eo pipefail
          name: "dev-build"
          context: team-context
          image: org/base-image
          tag: edge
          docker-cve-scan: true
          snyk-organization: org
          cis-docker-image-scan: true
          bats-test: true
          container-name: base-image-test
          filters: *on-push-master
          
      - executor-tools/publish:
          shell: secrethub run -- /bin/sh -eo pipefail
          name: Release
          context: team-context
          image: org/base-image
          release: stable
          filters: *on-tag-master      

```

Workflows assume:

* Trunk based development (TBD)
* Versioned released are triggered/managed by tagging

_Incorporates concepts from circleci/docker-publish@0.1.2_
