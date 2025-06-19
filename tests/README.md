# Python Playground

## What is this?

I made this repo to play with Python, my second favorite language :)

It's been a while since I've used Python so I also didn't want to get rusty. Here I'm using Python 3.13

## Setup

Start by making a virtual env:

```
python3 -m venv venv 
```

Then activate and install libraries:

```
source venv/bin/activate && pip install -r requirements.txt
```

## Running

Run the tests from the shell:

```shell
./test
```

Run an individual test by it's name using t

```
./t "add_two_numbers_test"
```