# pdf_editor
a python based pdf toolkit command line tool 

## basic use

#### -s 

> is the single file mode, think about this situation, you want to print out these meregd file,
but these the odd file would be printed on the same paper of the next file, but you just want to 
merely merge files which equals submit every pdf in the printer and printed out, so `-s` is just 
created for this special situation, it will eliminate this condition when merging multiple pdf files,
the workflow is adding blank page after one odd files. In this way, the merged two files/dir will be printed 
out and the same as printed once at time. 

```command line 
python3 controller -s (-m/-d)
```

#### merge two files 

```command line 
python3 controller -m [file1_path] [file2_path]
```

#### merge a dir 

```command line 
python3 controller -d [filename1] [filename2]
```

