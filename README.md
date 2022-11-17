# Hadoop MapReduce
##### Map Reduce Algorithm with word count
This was a project for my data science class using the power of Hadoop MapReduce to partition the amount of word occurences in a text file. This project helped gain insite into 

- Hadoop and it's cool library of tools
- Scaling big data
- Parallel computing tricks
- MapReduce paradigm

## Installation
* Install [Hadoop](https://hadoop.apache.org/releases.html) and set up environment inlcuding built-in jars for the mapreduce executable. To use in a terminal instance, you can type:
```bash
export HADOOP_CLASSPATH=/usr/lib/jvm/java/lib/tools.jar
``` 

* Once installed, download source repo and navigate to destination folder. 

## Usage
```bash
mapred streaming -mapper mapper.py -reducer reducer.py -input words-input -output words-output
```

## Output
```bash
_words-input/part-00000
a 84	
ability 1	
about 3	
abstractions 1	
access 4	
accessible 1	
according 1	
achieved 1	
achieves 1	
across 7	
actions 1	
active 1	
acts 1	
actual 3	
add 1	
added 1	
adding 1	
addition 2	
additional 1	
advantage 3	
after 1	
against 1	
aggregate 1	
aims 1	
algorithms 1	
alive 1	
all 4	
allocate 1	
```

## License
[MIT](https://choosealicense.com/licenses/mit/)