from django.core.management.base import BaseCommand
from timetable.scripts.process_excel import main


class Command(BaseCommand):
    help = 'タイムテーブルをデータベースに保存するコマンド'

    def handle(self, *args, **options):
        main()
