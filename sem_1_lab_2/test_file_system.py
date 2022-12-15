import pytest
from app import *

app.testing = True
client = app.test_client()


def test_create_dir1():
    create_data = {
        "name": "dir1",
        "path": ""
    }

    response = client.post('/createdir', json=create_data)
    assert response.status_code == 201
    assert response.data.decode('utf-8') == "Created directory: dir1/"


def test_create_dir2():
    create_data = {
        "name": "dir2",
        "path": "dir1/"
    }

    response = client.post('/createdir', json=create_data)
    assert response.status_code == 201
    assert response.data.decode('utf-8') == "Created directory: dir1/dir2/"


def test_create_dir3():
    create_data = {
        "name": "dir3",
        "path": "dir1/dir2/"
    }

    response = client.post('/createdir', json=create_data)
    assert response.status_code == 201
    assert response.data.decode(
        'utf-8') == "Created directory: dir1/dir2/dir3/"


def test_create_binary():
    create_data = {
        "name": "bin1",
        "path": "dir1/",
        "context": "it is bin1"
    }

    response = client.post('/createbinary', json=create_data)
    assert response.status_code == 201
    assert response.data.decode('utf-8') == "Created binary file: dir1/bin1/"


def test_crete_log():
    create_data = {
        "name": "log1",
        "path": "dir1/dir2/",
        "context": ["it", "is", "log1", "file"]
    }
    response = client.post('/createlog', json=create_data)
    assert response.status_code == 201
    assert response.data.decode('utf-8') == "Created log file: dir1/dir2/log1/"


def test_crete_buffer():
    create_data = {
        "name": "buffer1",
        "path": "dir1/"
    }
    response = client.post('/createbuffer', json=create_data)
    assert response.status_code == 201
    assert response.data.decode(
        'utf-8') == "Created buffer file: dir1/buffer1/"


def test_get_list_of_dir_comp():
    get_data = {
        "path": "dir1/"
    }
    response = client.get('/getlist', json=get_data)
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "dir2, bin1, buffer1, "


def test_get_list_of_dir_comp_fail():
    get_data = {
        "path": "dir1/dir1/"
    }
    response = client.get('/getlist', json=get_data)
    assert response.status_code == 404
    assert response.data.decode('utf-8') == "cannot find directory"


def test_read_binary():
    get_data = {
        "path": "dir1/bin1/"
    }
    response = client.get('/readBinary', json=get_data)
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "it is bin1"


def test_read_log():
    get_data = {
        "path": "dir1/dir2/log1/"
    }
    response = client.get('/readLog', json=get_data)
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "it\nis\nlog1\nfile\n"


def test_read_log_fail():
    get_data = {
        "path": "dir3/dir2/log1/"
    }
    response = client.get('/readLog', json=get_data)
    assert response.status_code == 404
    assert response.data.decode('utf-8') == "cannot find log file"


def test_append_log():
    put_data = {
        "path": "dir1/dir2/log1/",
        "line": "added line!"
    }
    response = client.put('/appendLog', json=put_data)
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "5"


def test_push_buffer():
    put_data = {
        "path": "dir1/buffer1/",
        "push": "push push"
    }
    response = client.put('/pushBuffer', json=put_data)
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "1"


def test_push_buffer_fail():
    put_data = {
        "path": "dir1/buffer1/",
        "push": "push push"
    }
    response = client.put('/pushBuffer', json=put_data)
    response = client.put('/pushBuffer', json=put_data)
    response = client.put('/pushBuffer', json=put_data)
    response = client.put('/pushBuffer', json=put_data)
    response = client.put('/pushBuffer', json=put_data)
    response = client.put('/pushBuffer', json=put_data)
    response = client.put('/pushBuffer', json=put_data)
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "Can not push to buffer file"


def test_consume_buffer():
    get_data = {
        "path": "dir1/buffer1/"
    }
    response = client.get('/consumeBuffer', json=get_data)
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "push push"


def test_move_dir():
    put_data = {
        "old": "dir1/dir2/dir3/",
        "new": "dir1/"
    }
    response = client.put('/moveNode', json=put_data)
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Moved: dir1/dir3/"


def test_move_dir_fail():
    put_data = {
        "old": "dir1/dir2/dir3/",
        "new": "dir1/"
    }
    response = client.put('/moveNode', json=put_data)
    assert response.status_code == 404
    assert response.data.decode('utf-8') == "cannot find dir or file to move"


def test_delete_log():
    delete_data = {
        "path": "dir1/dir2/log1/"
    }
    response = client.delete('/deletelog', json=delete_data)
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Deleted from: dir1/dir2/"


def test_move_log():
    put_data = {
        "old": "dir1/dir2/dir3/",
        "new": "dir1/"
    }
    response = client.put('/moveNode', json=put_data)
    assert response.status_code == 404
    assert response.data.decode('utf-8') == "cannot find dir or file to move"


def test_move_buffer():
    put_data = {
        "old": "dir1/buffer1/",
        "new": "dir1/dir2/"
    }
    response = client.put('/moveNode', json=put_data)
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Moved: dir1/dir2/buffer1/"


def test_delete_binary():
    delete_data = {
        "path": "dir1/bin1/"
    }
    response = client.delete('/deletelog', json=delete_data)
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Deleted from: dir1/"



def test_read_binary_fail():
    get_data = {
        "path": "dir1/bin1/"
    }
    response = client.get('/readBinary', json=get_data)
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "Can not read binary file"