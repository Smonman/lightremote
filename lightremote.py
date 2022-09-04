#!/usr/bin/python

import argparse
import queue
import time
from os import system, name

import cv2 as cv
import mouse

__author__ = "Simon Josef Kreuzpointner"


class SummaryQueue(queue.Queue):
    def __init__(self, size: int):
        super().__init__(size)

    def put(self, item, block: bool = ..., timeout: float | None = ...) -> None:
        if self.full():
            self.get()
        super().put(item, block, timeout)

    def sum(self):
        return sum(list(self.queue))


def main():
    args = handle_args()
    reaction_threshold, cycle_threshold, sampling_rate, history_length = args.values()
    cycle = 0
    camera = cv.VideoCapture(0)
    sq = SummaryQueue(history_length)
    try:
        while True:
            clear_screen()
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


def handle_args():
    parser = argparse.ArgumentParser(description="A simple brightness-change detector",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-r", "--reaction-threshold", nargs="?", type=float,
                        help="The threshold for a change in brightness.\n" +
                             "A larger change in brightness would result in an action",
                        default="0.3")
    parser.add_argument("-c", "--cycle-threshold", nargs="?", type=int,
                        help="Number of cycles to be omitted after a positive signal.\n" +
                             "This helps preventing multiple reactions to the same change in brightness.",
                        default="2")
    parser.add_argument("-s", "--sampling-rate", nargs="?", type=int,
                        help="Approximation of how many times per second a sample should be taken.\n" +
                             "This also controls the cycles.",
                        default="2")
    parser.add_argument("-l", "--history-length", nargs="?", type=int,
                        help="Length in cycles of the history for the average brightness.",
                        default="5")
    return vars(parser.parse_args())


def check_for_action(brightness, sq, reaction_threshold, cycle_threshold, cycle):
    avg_brightness = sq.sum() / sq.qsize() if sq.qsize() > 0 else 0
    sq.put(brightness, False, None)
    print_info(brightness, avg_brightness)
    return (abs(brightness - avg_brightness) > reaction_threshold) and (cycle_threshold < cycle) and (sq.full())


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


def clear_screen():
    if name == "nt":
        system("cls")
    else:
        system("clear")


if __name__ == "__main__":
    main()
