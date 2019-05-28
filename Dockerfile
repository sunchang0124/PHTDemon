FROM sophia921025/fairhealth_demon

COPY run.py /run.py
COPY myStages.py /myStages.py
COPY myFunctions.py /myFunctions.py

CMD ["python", "run.py"]