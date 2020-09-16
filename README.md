# fibonacci-calculator
Fibonacci sequence calculator and check whether a number is part of the Fibonacci sequence or not.

## Build Docker image

Use Git hub version
```bash
git clone https://gitlab.com/irajtaghlidi/fibonacci-calculator.git
cd fibonacci-calculator
docker build . -t fibonacci-calculator:local
```
OR
use the online Docker Hub Image.
**this image is builded, tested and pushed to Docker Hub with GitLab CI/CD (`.gitlab-ci.yml` file).**
```bash
docker pull irajtaghlidi/fibonacci-calculator:latest
```

## Usage
Show help of application from local builed image:
```bash
docker run --rm irajtaghlidi/fibonacci-calculator:latest --help
```
The ```---calc``` argument is used to calculate and show reverese order of specific number of Fibonacci sequence.

For example to calculate first 10 Fibonacci numbers:
```bash
docker run --rm irajtaghlidi/fibonacci-calculator:latest --calc 10
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

Example 1: Check number 36 is part of Fibonacci sequence or not:
```bash
docker run --rm irajtaghlidi/fibonacci-calculator:latest --check 36
```
OUTPUT:
```bash
0
```
Example 2: Check number 55 is part of Fibonacci sequence or not:
```bash
docker run --rm irajtaghlidi/fibonacci-calculator:latest --check 55
```
OUTPUT:
```bash
1
```

## Debug
the ```-v``` or ```--verbose``` argument is used to show more details in outputs.
for example in ```--calc``` argument we can see index numbers too.
```bash
docker run --rm irajtaghlidi/fibonacci-calculator:latest --calc 10 --verbose
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
docker run --rm irajtaghlidi/fibonacci-calculator:latest --check 34 --verbose
```

OUTPUT:
```
True: This number is #10 in Fibonacci sequent
```
## Test
To run Unit test:
```bash
python test.py
```
## TODO:
* we can use 'fast doubling Fibonacci algorithm' to achive a lower time complexity but in my benchmarks the current method is fast enough for now.
* adding more verbose levels.
* add a Bash script to build docker image easily.
* ANYTHINK YOU LIKE! your contribution is welcome.