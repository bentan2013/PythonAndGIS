#!/usr/bin/env python
# -*- coding: utf-8 -*-

# REF
# https://github.com/elliotforbes/Concurrency-With-Python/blob/master/Chapter%2001/concurrentImage.py


import urllib.request
import time
import threading

test_image_url = "http://dimg04.c-ctrip.com/images/fd/hotel/g3/M04/FA/7A/CggYG1adnlmARycYAAF2ezz36-c207_W_1600_1200_Q70.jpg"

def download_image(image_path, file_name):
    urllib.request.urlretrieve(test_image_url, file_name)
    #print(file_name)


def sequential_image():
    for i in range(10):
        image_name = "temp/image-" + str(i) + ".jpg"
        download_image("http://lorempixel.com/400/200/sports", image_name)


def execute_thread(i):
    image_name = "temp/image-" + str(i) + ".jpg"
    download_image("http://lorempixel.com/400/200/sports", image_name)


def concurrent_image():
    threads = []
    for i in range(10):
        thread = threading.Thread(target=execute_thread, args=(i,))
        threads.append(thread)
        thread.start()
    for i in threads:
        i.join()


def calc_time(func):
    start = time.time()
    func()
    end = time.time()
    total_cost_time = end - start
    print("Total execution time of {0}: {1}".format(func.__name__, total_cost_time))

if __name__ == '__main__':
    calc_time(sequential_image)
    calc_time(concurrent_image)
