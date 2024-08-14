FROM python:3.12
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY measurements.py measurements.py
COPY setups3.py setups3.py
COPY mapping.py mapping.py
RUN mkdir templates
CMD python mapping.py && python setups3.py && python measurements.py