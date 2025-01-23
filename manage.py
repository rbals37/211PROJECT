#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RGO.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "가상환경 좀 켜라"
            "명령어 : source venv/bin/activate"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
