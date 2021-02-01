# Implementatin of cache replacement algorithms in Python

## Why this project exists

As my final task at the ending of cource "Operating systems" I got task to implement LRU and LFU cache replacement algorithms. While I was completing my task I noticed that
this is such an interesting topic and I decided to expand my project, add some more functionality to it and place on GitHub.

## What you will find in this repository

You can find implementation of two cache replacement algorithms and report that explains how them work. Report is writen in Polish, implementation of both algorithms is in English,
all code and comments are in English.

### What is the main idea of LRU cache replacement algorithm

The idea of LRU (Least Recently Used) cache replacement algorithm is to delete the one page from cache memory (in case of lack of free pages in cache memory), that has not beed used for the longest period of time.

### What is the main idea of LFU cache replacement algorithm

The idea of LFU (LFU (Least Frequently Used) cache replacement algorithm is to delete from cache memory the page with fewest number of requests to it.

## Is there some features in this program?

Yes, I implemented function that allows you to write down data of all processes that you tested to CSV file, and function that reads this data ftom CSV file.
