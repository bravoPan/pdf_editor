#! /usr/bin/env python3
import optparse
from pdf_main import Editor


class Controller(object):
    def __init__(self):
        self.opt = optparse.OptionParser()
        self._add_options()
        self.pdf_editor = Editor()
        self.event_trigger()

    def _add_options(self):
        self.opt.add_option("--merge-two-file", '-m', default=None,
                            help="merge two pdf files, the default path is in current dir, you can also specify"
                                 "a new dir.", dest="filename", nargs=2)
        self.opt.add_option("--merge-directory", "-d", help="merge a directory pdf files into one.",
                            dest="directory_name", default=None)
        self.opt.add_option("--single-mode", "-s",
                            help="merge file which is beneficial for printing, add blank paper if the "
                                 "original pdf is odd", default=True, dest="single_mode")
        self.options, self.arguments = self.opt.parse_args()
        print(self.opt.largs)

    # event_trigger, calling the functions according to options

    def event_trigger(self):
        if self.options.directory_name:
            self.merge_dir()
        if self.options.filename:
            self.merge_two_files()

    """
    Following are all functions from pdf_main, applying all pdf functions into command
    line, to control the different functions. 
    merge_two_files: extended from Editor, merging two files, adding single-mode 
    """

    def merge_two_files(self):
        save_dest = input("Do you want to save at current directory?y/s ")
        if save_dest == "y":
            self.pdf_editor.merge_file(self.options.filename[0], self.options.filename[1])
        else:
            save_dest = input("Where else do you want to save? ")
            self.pdf_editor.merge_file(self.options.filename[0], self.options.filename[1], save_dest)

    def merge_dir(self):
        save_dest = input("Do you want to save at current directory?y/s ")
        if save_dest == "y":
            self.pdf_editor.merge_dir(self.options.directory_name)
        else:
            save_dest = input("Where else do you want to save? ")
            self.pdf_editor.merge_dir(self.options.directory_name, save_dest)


def main():
    editor = Editor()
    p = optparse.OptionParser()
    p.add_option('--person', '-p', default=None,
                 help="the test for the person!\nthe test for the person!\nthe test for the person!\n")
    p.add_option('--name', '-n', default=None)
    p.add_option("--merge-two-file", '-m', default="./",
                 help="merge two pdf files, the default path is in current dir, you can also specify"
                      "a new dir.", dest="filename", nargs=2)
    p.add_option("--single-mode", "-s", default=True, dest="single-mode")
    options, arguments = p.parse_args()
    print(options)

    editor.merge_file(options.filename[0], options.filename[1])


if __name__ == '__main__':
    test = Controller()
