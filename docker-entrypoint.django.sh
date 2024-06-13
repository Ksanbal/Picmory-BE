echo "- Collect static files"
poetry run python manage.py collectstatic --no-input

echo "- RUN Server"
poetry run gunicorn --bind 0.0.0.0:8000 config.wsgi:application