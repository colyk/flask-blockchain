Blockchain with Flask
=======================

## What is blockchain?

**A blockchain** –  is a continuously growing list of records, called blocks, which are linked and secured using cryptography hash. Each block typically contains a hash pointer as a link to a previous block and a timestamp. By design, blockchains are inherently resistant to modification of the data. For getting hash used _SHA-256_

## How to run project


```
pip install Flask

git clone https://github.com/colyk/flask-blockchain.git

cd flask-blockchain

python server.py
```

Now head over to http://127.0.0.1:5000/, and you should see main page of blockchain, where you can add new block, check blocks integrity and mined blocks using POW algorithm.

## POW

**POW** _( proof of work)_ is a piece of data which is difficult (costly, time-consuming) to produce but easy for others to verify and which satisfies certain requirements. Producing a proof of work can be a random process with low probability so that a lot of trial and error is required on average before a valid proof of work is generated. Bitcoin uses the Hashcash proof of work system.
