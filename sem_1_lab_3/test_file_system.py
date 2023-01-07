import pytest
import subprocess


def test_create_dir1():
    response = subprocess.check_output(
        ["python3", "cli.py", "createDir", "dir1",  ""]).decode()
    assert response == "b'Created directory: dir1/'\n"


def test_create_dir2():
    response = subprocess.check_output(
        ["python3", "cli.py", "createDir", "dir2",  "dir1/"]).decode()
    assert response == "b'Created directory: dir1/dir2/'\n"


def test_create_dir3():
    response = subprocess.check_output(
        ["python3", "cli.py", "createDir", "dir3",  "dir1/dir2/"]).decode()
    assert response == "b'Created directory: dir1/dir2/dir3/'\n"


def test_create_binary():
    response = subprocess.check_output(
        ["python3", "cli.py", "createBin", "bin1",  "dir1/", "it is bin1"]).decode()
    assert response == "b'Created binary file: dir1/bin1/'\n"


def test_crete_log():
    response = subprocess.check_output(
        ["python3", "cli.py", "createLog", "log1",  "dir1/dir2/", "it, is, log1, file"]).decode()
    assert response == "b'Created log file: dir1/dir2/log1/'\n"


def test_crete_buffer():
    create_data = {
        "name": "buffer1",
        "path": "dir1/"
    }
    response = subprocess.check_output(
        ["python3", "cli.py", "createBuff", "buffer1",  "dir1/"]).decode()
    assert response == "b'Created buffer file: dir1/buffer1/'\n"


def test_get_list_of_dir_comp():
    response = subprocess.check_output(
        ["python3", "cli.py", "getDirList", "dir1/"]).decode()
    assert response == "b'dir2, bin1, buffer1, '\n"


def test_get_list_of_dir_comp_fail():
    response = subprocess.check_output(
        ["python3", "cli.py", "getDirList", "dir1/dir1/"]).decode()
    assert response == "b'cannot find directory'\n"


def test_read_binary():
    response = subprocess.check_output(
        ["python3", "cli.py", "readBin", "dir1/bin1/"]).decode()
    assert response == "b'it is bin1'\n"


def test_read_log():
    response = subprocess.check_output(
        ["python3", "cli.py", "readLog", "dir1/dir2/log1/"]).decode()
    assert response == "b'it\\n is\\n log1\\n file\\n'\n"


def test_read_log_fail():
    response = subprocess.check_output(
        ["python3", "cli.py", "readLog", "dir3/dir2/log1/"]).decode()
    assert response == "b'cannot find log file'\n"


def test_append_log():
    response = subprocess.check_output(
        ["python3", "cli.py", "appendLog", "dir1/dir2/log1/", "added line!"]).decode()
    assert response == "b'5'\n"


def test_push_buffer():
    response = subprocess.check_output(
        ["python3", "cli.py", "pushBuff", "dir1/buffer1/", "push push"]).decode()
    assert response == "b'1'\n"


def test_push_buffer_fail():
    response = subprocess.check_output(
        ["python3", "cli.py", "pushBuff", "dir1/buffer1/", "push push"]).decode()
    response = subprocess.check_output(
        ["python3", "cli.py", "pushBuff", "dir1/buffer1/", "push push"]).decode()
    response = subprocess.check_output(
        ["python3", "cli.py", "pushBuff", "dir1/buffer1/", "push push"]).decode()
    response = subprocess.check_output(
        ["python3", "cli.py", "pushBuff", "dir1/buffer1/", "push push"]).decode()
    response = subprocess.check_output(
        ["python3", "cli.py", "pushBuff", "dir1/buffer1/", "push push"]).decode()
    response = subprocess.check_output(
        ["python3", "cli.py", "pushBuff", "dir1/buffer1/", "push push"]).decode()
    response = subprocess.check_output(
        ["python3", "cli.py", "pushBuff", "dir1/buffer1/", "push push"]).decode()
    assert response == "b'Can not push to buffer file'\n"


def test_consume_buffer():
    response = subprocess.check_output(
        ["python3", "cli.py", "consumeBuff", "dir1/buffer1/"]).decode()
    assert response == "b'push push'\n"


def test_move_dir():
    response = subprocess.check_output(
        ["python3", "cli.py", "moveDir", "dir1/dir2/dir3/", "dir1/"]).decode()
    assert response == "b'Moved: dir1/dir3/'\n"


def test_move_dir_fail():
    response = subprocess.check_output(
        ["python3", "cli.py", "moveDir", "dir1/dir2/dir3/", "dir1/"]).decode()
    assert response == "b'cannot find dir or file to move'\n"


def test_delete_log():
    response = subprocess.check_output(
        ["python3", "cli.py", "deleteLog", "dir1/dir2/log1/"]).decode()
    assert response == "b'Deleted from: dir1/dir2/'\n"


def test_move_log():
    response = subprocess.check_output(
        ["python3", "cli.py", "moveLog", "dir1/dir2/log1/", "dir1/"]).decode()
    assert response == "b'Can not move'\n"


def test_move_buffer():
    response = subprocess.check_output(
        ["python3", "cli.py", "moveBuff", "dir1/buffer1/", "dir1/dir2/"]).decode()
    assert response== "b'Moved: dir1/dir2/buffer1/'\n"


def test_delete_binary():
    response = subprocess.check_output(
        ["python3", "cli.py", "deleteBin", "dir1/bin1/"]).decode()
    assert response == "b'Deleted from: dir1/'\n"


def test_read_binary_fail():
    response = subprocess.check_output(
        ["python3", "cli.py", "readBin", "dir1/bin1/"]).decode()
    assert response == "b'Can not read binary file'\n"


