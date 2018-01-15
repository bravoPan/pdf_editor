from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import os


class Editor(object):
    # change the pdf to even num
    def convert_even(self, file_path):
        if self.check_pdf_file(file_path):
            input_file = PdfFileReader(open(file_path, "rb"))
            try:
                # MediaBox defines the height and width of this page
                source_file_size = input_file.getPage(0)['/MediaBox']
                height, width = source_file_size[3], source_file_size[2]
                output_stream = self.copy_output_stream(file_path)
                page_num = input_file.numPages
                if page_num % 2 != 0:
                    output_stream.addBlankPage(height=height, width=width)
                return output_stream
            except IndexError:
                print("This size attribute is not right")

    # merge two files and save
    def merge_file(self, file1, file2, saved_dir="./", save_name="merged", single_mode=False):
        if self.check_path(saved_dir) and self.check_pdf_file(file1) and self.check_pdf_file(file2):
            merged_file = PdfFileMerger()
            if single_mode:
                input_stream1 = self.convert_even(file1)
                input_stream2 = self.convert_even(file2)
                input_stream1.write(open("temp1.pdf", "wb"))
                input_stream2.write(open("temp2.pdf", "wb"))
                merged_file.append(open("temp1.pdf", "rb"))
                merged_file.append(open("temp2.pdf", "rb"))
                os.remove("temp1.pdf")
                os.remove("temp2.pdf")
            else:
                out_put_stream1 = PdfFileReader(open(file1, "rb"))
                out_put_stream2 = PdfFileReader(open(file2, "rb"))
                merged_file.append(out_put_stream1)
                merged_file.append(out_put_stream2)
            empty_pdf = open(saved_dir + save_name + ".pdf", "wb")
            merged_file.write(empty_pdf)

    # recursive merge, merge but not save
    def _recursive_merge_two_pdf(self, input_stream, work_list, single_mode=False):
        if not work_list:
            return input_stream
        else:
            if single_mode:
                added_blank = self.convert_even(work_list[0])
                added_blank.write(open("temp.pdf", "wb"))
                input_stream.append(open("temp.pdf", "rb"))
                os.remove("temp.pdf")
            else:
                input_stream.append(open(work_list[0], "rb"))
            del work_list[0]
            return self._recursive_merge_two_pdf(input_stream, work_list)

    # merge a dir containing all pdf files
    def merge_dir(self, dir_path, save_dir="./", save_name="merged", single_mode=False):
        if self.check_path(save_dir):
            if self.check_path(dir_path):
                # do modify to the path and name in order to avoid user add postfix
                if dir_path[-1] != "/":
                    dir_path += "/"
                if ".pdf" not in save_name:
                    save_name += ".pdf"
                pdf_list = []
                for i in os.listdir(dir_path):
                    # check if user add "/" at the end of the path
                    if self.check_pdf_file(dir_path + i):
                        pdf_list.append(dir_path + i)
                merged_files = PdfFileMerger()
                if single_mode:
                    self._recursive_merge_two_pdf(merged_files, pdf_list, single_mode=True)
                else:
                    self._recursive_merge_two_pdf(merged_files, pdf_list)
                merged_files.write(open(save_dir + save_name, "wb"))

    @staticmethod
    def check_path(path):
        if os.path.isdir(path):
            return True
        else:
            print(path + " is not a invalid path!")
            return False

    @staticmethod
    def check_pdf_file(file_path):
        if os.path.isfile(file_path):
            if ".pdf" not in file_path:
                return False
            else:
                return True
        else:
            return False

    @staticmethod
    def copy_output_stream(output_path):
        input_stream = PdfFileWriter()
        out_put_stream = PdfFileReader(output_path)
        for i in range(out_put_stream.numPages):
            input_stream.addPage(out_put_stream.getPage(i))
        return input_stream


if __name__ == "__main__":
    ed = Editor()
    ed.merge_file("/Users/yuanxiansen/Desktop/skill/programming/python/pdf_editor/local/paper2.pdf",
                 "/Users/yuanxiansen/Desktop/skill/programming/python/pdf_editor/local/paper1.pdf", single_mode=True)
