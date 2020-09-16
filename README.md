# fibonacci-calculator

Fibonacci sequence calculator and check whether a number is part of the Fibonacci sequence or not

## Build Docker image
```bash
git clone https://github.com/irajtaghlidi/fibonacci-calculator.git
cd fibonacci-calculator

docker build . -t fibonacci:latest
```

## Usage
showing how to work with program.
```bash
docker run --rm fibonacci:latest --help
```

The  ```---calc``` argument is used to calculate and show reverese order of specific number of Fibonacci sequence.
For example to calculate first 20 Fibonacci numbers:
```bash
docker run --rm fibonacci:latest --calc 10
```
OUTPUT:
```bash
34
21
13
8
5
3
2
1
1
0
```

The ```---check``` argument is used to check whether a number is part of the Fibonacci sequence or not.
For example to check number 55 is part of Fibonacci sequence or not:
```bash
docker run --rm fibonacci:latest --check 34
```

## Debug
the ```-v``` or ```--verbose``` argument is used to show more details in outputs.
for example in ```--calc``` argument we can see index numbers too.
```bash
docker run --rm fibonacci:latest --calc 10 --verbose
```
OUTPUT:
```
#10: 34
#9: 21
#8: 13
#7: 8
#6: 5
#5: 3
#4: 2
#3: 1
#2: 1
#1: 0
```

and also in ```--check``` argument we can see index of input number if it is part of Fibonacci sequence.

```bash
docker run --rm fibonacci:latest --check 34 --verbose
```

OUTPUT:
```
True: This number is #9 in Fibonacci sequent
```


## TODO:
* we can use 'fast doubling Fibonacci algorithm' to achive a lower time complexity but in my benchmarks the current method is fast enough for now.
* adding more verbose levels.
* add test methods for python scripts.
* add a Bash script to build docker image easily.
* ANYTHINK YOU LIKE! your contribution is welcome.