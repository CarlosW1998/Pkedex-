FROM ubuntu:latest
RUN apt-get update && apt-get -y update
RUN apt-get install -y build-essential python3.6 python3-pip python3-dev

RUN mkdir src
WORKDIR src/
COPY . .
RUN pip3 install -r requirements.txt
RUN pip3 install jupyter
RUN python3 src/pakags.py
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]