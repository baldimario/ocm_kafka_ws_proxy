FROM python:3

WORKDIR /ocm

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["sh", "-c", "tail -f /dev/null"]