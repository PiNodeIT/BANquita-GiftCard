![alt text](https://github.com/PiNodeIT/BANquita-GiftCard/blob/main/src/bg.png)

# BANquita Python GiftCard Generator

This is a Python scrypt to generate banquita-themed BANANO giftcards 

**ATTENTION**
This scrypt **<u>does not generate</u>** wallet, but only the giftcard, this means that **YOU must have the seed** (there are many tools to create banano wallet, both random and vanity).

## How to generate a seed/address pair

- Go to https://nanoo.tools/quick-banano-account

- Click Random Seed

Now you have the seed and the address.

- The seed must be entered when prompted by the banquita-gift script to put the seed into the GiftCard
- The public address is the address to send the ban to load the giftcard

Seed generation and banquita-gift script execution can be performed <u>offline</u> **<u>(for security reasons offline execution is strongly recommended)</u>**

### Requirements

- Python 3.7+
- qrcode lib
- Pillow lib

### Installation

install the requirements

```sh
pip install -r requirements.txt
```

### Usage instructions 

Clone the repo or download it
you will find 1 File (the Python script) and 2 Folders
The folder "src" contains the base image 
The folder "GiftCard" is where the giftcards in PNG format will be saved.

Once you start the script it will ask you to enter the SEED , the DEPOSIT address and finally a name you want to give the file (without extension) 

that's it, now inside the folder "GiftCard" you will find 2 file :
  - (name)_GiftCard.png is the giftcard
  - (name)_Deposit.png is the deposit address qrcode (to put some BAN in the giftcard)

### Final comments

I know the scrypt could be much more elegant and functional than this, unfortunately I'm not a programming expert, so **feel free to improve it**

## What is BANANO?
https://banano.cc/

### credits :
the original image is by : https://banano.cc/paperwallet/
