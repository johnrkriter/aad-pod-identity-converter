FROM python:alpine

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /usr/src/app/identity_converter

CMD [ "python", "converter.py" ]