# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9

EXPOSE 8080

ENV LISTER_PORT=8080
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1


# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

COPY ./entrypoint.sh /


RUN chmod g+w /app
RUN chmod g+w /app/db.sqlite3
RUN chmod +w /app/static
RUN chmod +wr /app/media


# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser
RUN chown -R appuser /app/
RUN chmod -R 777 /app/static/

ENTRYPOINT [ "sh", "/entrypoint.sh" ]
# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "3", "main.wsgi:application"]