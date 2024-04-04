FROM quay.io/jupyter/base-notebook
WORKDIR /tmp
COPY requirements.txt .
RUN pip install -r requirements.txt
