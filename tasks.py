from invoke import task


@task
def sass(ctx, watch=False):
    watch = ' --watch' if watch else ''
    ctx.run('sass lib/scss/main.scss:lib/assets/css/main.css' + watch, pty=True)


@task
def run(ctx):
    ctx.run('python manage.py runserver', pty=True)
