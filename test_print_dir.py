import os

def test_print_dir():
    file_string = 'files: '
    dir_string = 'dirs:  '
    unsorted_file_list = os.listdir()
    sortetd_file_list = sorted(unsorted_file_list)
    for index in sortetd_file_list:
        if os.path.isfile(index):
            file_string = file_string + index + ', '
        if os.path.isdir(index):
            dir_string = dir_string + index + ', '
    with open('listdir.txt', 'r') as f:
        file_string_new = f.readline().replace('\n', '')
        dir_string_new = f.readline().replace('\n', '')
        assert file_string_new == file_string
        assert dir_string_new+' ' == dir_string










