# Blockchain
Blockchain simulation with a web interface on Flask.

## How it works
### Main view
<img src="https://i.ibb.co/TR3XyJW/photo-2023-05-01-14-51-24.jpg" alt="" height="500">

### Checking the integrity of 4 newly created blocks
<img src="https://i.ibb.co/27q9Ccx/photo-2023-05-01-14-51-26.jpg" alt="" height="500">

### All blocks are mined
<img src="https://i.ibb.co/RH1cFcS/photo-2023-05-01-14-51-27.jpg" alt="" height="500">

### The last block is manually corrupted in `./blocks` and new block is added
<img src="https://i.ibb.co/vBgJWcK/photo-2023-05-01-14-51-28.jpg" alt="" height="500">

### What is blockchain?

**Blockchain** –  is a continuously growing list of records, called blocks, which are linked and secured using cryptography hash. Each block typically contains a hash pointer as a link to a previous block and a timestamp. By design, blockchains are inherently resistant to modification of the data. For getting hash used _SHA-256_

### What is POW

**POW** _(proof of work)_ is a piece of data which is difficult (costly, time-consuming) to produce but easy for others to verify and which satisfies certain requirements. Producing a proof of work can be a random process with low probability so that a lot of trial and error is required on average before a valid proof of work is generated. Bitcoin uses the Hashcash proof of work system.

## How to run

```
pip install -r requirements.txt

python server.py
```

Now head over to http://127.0.0.1:5000/, and you should see main page of blockchain, where you can add new block, check blocks integrity and mined blocks using POW algorithm.


