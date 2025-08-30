# buzzline-01-moses

![Python 3.11](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)

This project demonstrates **streaming data in Python** using generators.  
A **producer** continuously emits log messages, while a **consumer** tails the log file in real time, detecting alerts and printing simple analytics.

---

## Project Structure

- **Producer:** [`producers/basic_producer_mk.py`](producers/basic_producer_mk.py)  
  Continuously generates track-style log messages with occasional `MK-ALERT` tokens.

- **Consumer:** [`consumers/basic_consumer_mk.py`](consumers/basic_consumer_mk.py)  
  Monitors the log, flags alerts, and prints running statistics.

---

## Setup

Clone the repository and prepare a virtual environment (**Python 3.11 recommended**):

```bash
git clone https://github.com/mokeyzz1/buzzline-01-moses.git
cd buzzline-01-moses

python3 -m venv .venv
source .venv/bin/activate    # Mac/Linux
# .venv\Scripts\activate     # Windows PowerShell

pip install -r requirements.txt
Usage

Open two terminals — one for the producer and one for the consumer.

Terminal 1 – Producer
source .venv/bin/activate
python3 -m producers.basic_producer_mk     # Mac/Linux

# Windows PowerShell
.venv\Scripts\activate && py -m producers.basic_producer_mk

Terminal 2 – Consumer
source .venv/bin/activate
python3 -m consumers.basic_consumer_mk     # Mac/Linux

# Windows PowerShell
.venv\Scripts\activate && py -m consumers.basic_consumer_mk