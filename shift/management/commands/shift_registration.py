from django.core.management.base import BaseCommand
from shift.scripts.process_excels import main


class Command(BaseCommand):
    help = 'シフトをデータベースに保存するコマンド'

    def handle(self, *args, **options):
        main()
