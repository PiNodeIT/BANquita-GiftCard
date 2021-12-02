# BANquita Python GiftCard Generator

This is a Python scrypt to generate banquita-themed BANANO giftcards 

**ATTENTION**
This scrypt **<u>does not generate</u>** wallet, but only the giftcard, this means that **YOU must have the seed** (there are many tools to create banano wallet, both random and vanity).

### Requirements

- Python 3.7+
- qrcode lib
- PIL lib

### Installation

install qrcode and PIL

```python
pip install Pillow
```
```python
pip install QRcode
```

### Usage instructions 

Clone the repo or download it
you will find 1 File (the Python script) and 2 Folders
The folder "src" contains the base image 
The folder "GiftCard" is where the giftcards in PNG format will be saved.

Once you start the script it will ask you to enter the SEED and finally a name you want to give the file (without extension) 

that's it, now inside the folder "GiftCard" you will find your giftcard 

### Final comments

I know the scrypt could be much more elegant and functional than this, unfortunately I'm not a programming expert, so **feel free to improve it**
