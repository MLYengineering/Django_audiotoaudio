
import sys
from django.core.management.base import BaseCommand
from livekit.agents import cli, WorkerOptions, WorkerType
import logging

from livekit_app.livekit_main import entrypoint  # importieren Sie Ihre entrypoint Funktion


class Command(BaseCommand):
    help = 'Starts the Livekit worker.'

    def add_arguments(self, parser):
        # Erlaubt beliebige zusätzliche Argumente, z. B. "dev" oder "start"
        parser.add_argument('extra_args', nargs='*', help='Extra arguments passed to the livekit cli')

    def handle(self, *args, **options):
        # Hier holen wir uns die übergebenen extra Argumente wie "dev" oder "start"
        extra_args = options['extra_args']

        # sys.argv wird nun auf die Basis (manage.py) plus extra_args gesetzt,
        # damit cli.run_app() diese an click weitergeben kann.
        sys.argv = [sys.argv[0]] + extra_args

        # Startet den Worker mit den durchgereichten Argumenten (z. B. "dev" oder "start")
        cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, worker_type=WorkerType.ROOM))
