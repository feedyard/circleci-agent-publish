"""local invoke scripts"""
from invoke import task

@task
def validate(ctx):
    ctx.run('circleci config pack src > orb.yml')
    ctx.run('circleci orb validate orb.yml')
    ctx.run('rm orb.yml')
