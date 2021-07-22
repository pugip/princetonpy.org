from psycogreen.gevent import patch_psycopg     # use this if you use gevent workers


def post_fork(server, worker):
    patch_psycopg()
    worker.log.info("Made Psycopg2 Green")
