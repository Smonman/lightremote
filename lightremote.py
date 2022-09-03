#!/usr/bin/python

import argparse
import os
import queue
import time

import cv2 as cv
import mouse

__author__ = "Simon Josef Kreuzpointner"


class SizedQueue:
    def __init__(self, size: int):
        self.q = queue.Queue(size)

    def put(self, item):
        if self.q.full():
            self.q.get()
        self.q.put(item)


class SummaryQueue(SizedQueue):
    def __init__(self, size: int):
        self.size = size
        SizedQueue.__init__(self, size)

    def sum(self):
        return sum(list(self.q.queue))


def handle_args():
    parser = argparse.ArgumentParser(description="A primitive light-change sensor",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-r", "--reaction-threshold", nargs="?", type=float,
                        help="the threshold for a change in brightness",
                        default="0.3")
    parser.add_argument("-c", "--cycle-threshold", nargs="?", type=int,
                        help="number of cycles to be omitted after a positive signal",
                        default="2")
    parser.add_argument("-s", "--sampling-rate", nargs="?", type=int,
                        help="approx. of how many times per second a sample should be taken",
                        default="2")
    parser.add_argument("-l", "--history-length", nargs="?", type=int,
                        help="length of the history for the average brightness",
                        default="5")
    return vars(parser.parse_args()).values()


def main():
    reaction_threshold, cycle_threshold, sampling_rate, history_length = handle_args()
    cycle = 0
    camera = cv.VideoCapture(0)
    sq = SummaryQueue(history_length)
    try:
        while True:
            os.system("cls")
            print("Type ^C to exit")
            return_value, image = camera.read()
            if return_value:
                b = process_image(image)
                if check_for_action(b, sq, reaction_threshold, cycle_threshold, cycle):
                    print("CLICK")
                    mouse.click("left")
                    cycle = 0
                cycle += 1
            time.sleep(1 / sampling_rate)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        camera.release()


def check_for_action(brightness, sq, reaction_threshold, cycle_threshold, cycle):
    avg_brightness = sq.sum() / sq.size
    sq.put(brightness)
    print_info(brightness, avg_brightness)
    return (abs(brightness - avg_brightness) > reaction_threshold) and (cycle_threshold < cycle)


def print_info(brightness, avg_brightness):
    print(
        f"{'current brightness:'.ljust(25)}{brightness:0.5f}\n" +
        f"{'last avg brightness:'.ljust(25)}{avg_brightness:0.5f}\n" +
        f"{'abs. difference:'.ljust(25)}{abs(brightness - avg_brightness):0.5f}")


def process_image(image):
    resized_image = resize_image(image, 0.333)
    gray_scale_image = cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY)
    return get_image_brightness(gray_scale_image)


def resize_image(image, factor):
    new_width = int(image.shape[0] * factor)
    new_height = int(image.shape[1] * factor)
    new_dimensions = (new_width, new_height)
    return cv.resize(image, new_dimensions)


def get_image_brightness(gray_scale_image):
    s = sum(gray_scale_image[..., 2])
    return s / gray_scale_image.size


if __name__ == "__main__":
    main()
