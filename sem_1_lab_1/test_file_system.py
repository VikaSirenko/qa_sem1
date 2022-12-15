from file_system import BinaryFile, BufferFile, Directory, LogTextFile
from file_system import Composite
import pytest


def test_create_dir():
    composite = Composite("file_system")
    dir1 = Directory("dir")
    dir1.create("directory1", "")
    composite.addSystemComponent(dir1)
    assert dir1.create("directory1", "")
    assert dir1.path == "directory1/"
    components = composite.getListOfComponents()
    assert len(components) == 1


def test_add_sub_dir():
    composite = Composite("file_system")
    dir1 = Directory("dir")
    dir1.create("directory1", "")
    composite.addSystemComponent(dir1)
    dir2 = Directory("dir")
    dir2.create("directory2", dir1.path)
    dir1.addSystemComponent(dir2)
    assert dir2.path == "directory1/directory2/"
    assert len(dir1.getListOfComponents()) == 1


def test_remove_dir():  
    composite = Composite("file_system")
    dir1 = Directory("dir")
    dir1.create("directory1", "")
    composite.addSystemComponent(dir1)
    dir2 = Directory("dir")
    dir2.create("directory2", dir1.path)
    dir1.addSystemComponent(dir2)
    assert dir1.delete(dir2) == "deleted"
    assert len(dir1.getListOfComponents()) == 0


def test_move_subDir():
    composite = Composite("file_system")
    dir1 = Directory("dir")
    dir1.create("directory1", "")
    composite.addSystemComponent(dir1)
    dir2 = Directory("dir")
    dir2.create("directory2", dir1.path)
    dir1.addSystemComponent(dir2)
    dir3 = Directory("dir")
    dir3.create("directory3", dir1.path)
    dir1.addSystemComponent(dir3)
    new_path = dir1.move("directory1/directory3/", dir2, composite)
    assert new_path == "directory1/directory3/directory2/"
    comp = dir1.getListOfComponents()
    assert len(comp) == 1


def test_create_binaryFile():
    composite = Composite("file_system")
    dir1 = Directory("dir")
    dir1.create("directory1", "")
    composite.addSystemComponent(dir1)
    binF1 = BinaryFile("binary")
    binF1.create("binary1", dir1.path, "It is binary file #1")
    dir1.addSystemComponent(binF1)
    assert binF1.path == "directory1/binary1/"
    assert len(dir1.getListOfComponents()) == 1


def test_move_binaryFile():
    composite = Composite("file_system")
    dir1 = Directory("dir")
    dir1.create("directory1", "")
    composite.addSystemComponent(dir1)
    dir2 = Directory("dir")
    dir2.create("directory2", dir1.path)
    dir1.addSystemComponent(dir2)
    dir3 = Directory("dir")
    dir3.create("directory3", dir1.path)
    dir1.addSystemComponent(dir3)
    binF1 = BinaryFile("binary")
    binF1.create("binary1", dir1.path, "It is binary file #1")
    dir1.addSystemComponent(binF1)
    assert binF1.move("directory1/directory3/",
                      composite, dir1) == "directory1/directory3/binary1/"


def test_read_binaryFile():
    composite = Composite("file_system")
    dir1 = Directory("dir")
    dir1.create("directory1", "")
    binF1 = BinaryFile("binary")
    binF1.create("binary1", dir1.path, "It is binary file #1")
    dir1.addSystemComponent(binF1)
    composite.addSystemComponent(dir1)
    assert binF1.readFile() == "It is binary file #1"



def test_remove_binaryFile():
    composite = Composite("file_system")
    dir1 = Directory("dir")
    dir1.create("directory1", "")
    composite.addSystemComponent(dir1)
    dir2 = Directory("dir")
    dir2.create("directory2", dir1.path)
    dir1.addSystemComponent(dir2)
    dir3 = Directory("dir")
    dir3.create("directory3", dir1.path)
    dir1.addSystemComponent(dir3)
    binF1 = BinaryFile("binary")
    binF1.create("binary1", dir3.path, "It is binary file #1")
    dir3.addSystemComponent(binF1)
    result = dir3.delete(binF1)
    assert result == "deleted"
    assert len(dir3.getListOfComponents()) == 0


def test_create_logFile():
    composite = Composite("file_system")
    dir1 = Directory("dir")
    dir1.create("directory1", "")
    composite.addSystemComponent(dir1)
    dir2 = Directory("dir")
    dir2.create("directory2", dir1.path)
    dir1.addSystemComponent(dir2)
    logF1 = LogTextFile("log")
    context = ["it", "is", "log", "file"]
    logF1.create("log1", dir2.path, context)
    dir2.addSystemComponent(logF1)
    assert logF1.path == "directory1/directory2/log1/"
    assert len(dir2.getListOfComponents()) == 1


def test_move_logFile():
    composite = Composite("file_system")
    dir1 = Directory("dir")
    dir1.create("directory1", "")
    composite.addSystemComponent(dir1)
    dir2 = Directory("dir")
    dir2.create("directory2", dir1.path)
    dir1.addSystemComponent(dir2)
    dir3 = Directory("dir")
    dir3.create("directory3", dir1.path)
    dir1.addSystemComponent(dir3)
    logF1 = LogTextFile("log")
    context = ["it", "is", "log", "file"]
    logF1.create("log1", dir3.path, context)
    dir3.addSystemComponent(logF1)
    assert logF1.move("directory1/",
                      composite, dir3) == "directory1/log1/"


def test_remove_logFile():
    composite = Composite("file_system")
    dir1 = Directory("dir")
    dir1.create("directory1", "")
    composite.addSystemComponent(dir1)
    dir2 = Directory("dir")
    dir2.create("directory2", dir1.path)
    dir1.addSystemComponent(dir2)
    dir3 = Directory("dir")
    dir3.create("directory3", dir2.path)
    dir2.addSystemComponent(dir3)
    logF1 = LogTextFile("log")
    context = ["it", "is", "log", "file"]
    logF1.create("log1", dir2.path, context)
    dir2.addSystemComponent(logF1)
    assert dir2.delete(logF1) == "deleted"
    assert len(dir2.getListOfComponents()) == 1


def test_read_logFile():
    composite = Composite("file_system")
    dir1 = Directory("dir")
    dir1.create("directory1", "")
    composite.addSystemComponent(dir1)
    logF1 = LogTextFile("log")
    context = ["it", "is", "log", "file"]
    logF1.create("log1", dir1.path, context)
    dir1.addSystemComponent(logF1)
    contextOfFile = ""
    for line in context:
        contextOfFile += line+"\n"
    assert logF1.readFile() == contextOfFile


def test_addNewLine_LogFile():
    composite = Composite("file_system")
    dir1 = Directory("dir")
    dir1.create("directory1", "")
    composite.addSystemComponent(dir1)
    logF1 = LogTextFile("log")
    context = ["it", "is", "log", "file"]
    leng = len(context)
    logF1.create("log1", dir1.path, context)
    dir1.addSystemComponent(logF1)
    assert logF1.addLine("Hello World") == leng+1


def test_create_buffer_file():
    composite = Composite("file_system")
    dir1 = Directory("dir")
    dir1.create("directory1", "")
    composite.addSystemComponent(dir1)
    dir2 = Directory("dir")
    dir2.create("directory2", dir1.path)
    dir1.addSystemComponent(dir2)
    bufferF1 = BufferFile("buffer")
    bufferF1.create("buffer1", dir2.path)
    dir2.addSystemComponent(bufferF1)
    assert bufferF1.path == "directory1/directory2/buffer1/"
    assert len(dir2.getListOfComponents()) == 1


def test_move_BufferFile():
    composite = Composite("file_system")
    dir1 = Directory("dir")
    dir1.create("directory1", "")
    composite.addSystemComponent(dir1)
    dir2 = Directory("dir")
    dir2.create("directory2", dir1.path)
    dir1.addSystemComponent(dir2)
    dir3 = Directory("dir")
    dir3.create("directory3", dir1.path)
    dir1.addSystemComponent(dir3)
    bufferF1 = BufferFile("buffer")
    bufferF1.create("buffer1", dir2.path)
    dir2.addSystemComponent(bufferF1)
    assert bufferF1.move("directory1/directory3/",
                         composite, dir2) == "directory1/directory3/buffer1/"


def test_remove_bufferFile():  
    composite = Composite("file_system")
    dir1 = Directory("dir")
    dir1.create("directory1", "")
    composite.addSystemComponent(dir1)
    dir2 = Directory("dir")
    dir2.create("directory2", dir1.path)
    dir1.addSystemComponent(dir2)
    dir3 = Directory("dir")
    dir3.create("directory3", dir1.path)
    dir1.addSystemComponent(dir3)
    bufferF1 = BufferFile("buffer")
    bufferF1.create("buffer1", dir1.path)
    dir1.addSystemComponent(bufferF1)
    result = dir1.delete(bufferF1)
    assert result == "deleted"
    assert len(dir1.getListOfComponents()) == 2


def test_pushEl_BufferFile():
    composite = Composite("file_system")
    dir1 = Directory("dir")
    dir1.create("directory1", "")
    composite.addSystemComponent(dir1)
    bufferF1 = BufferFile("buffer")
    bufferF1.create("buffer1", dir1.path)
    dir1.addSystemComponent(bufferF1)
    assert bufferF1.push("hi") == 1
    assert bufferF1.push("hi") == 2
    assert bufferF1.push("hi") == 3
    assert bufferF1.push("hi") == 4
    assert bufferF1.push("hi") == 5
    assert bufferF1.push("hi") == "can not add new data"
    


def test_consumeEl_bufferFile():
    composite = Composite("file_system")
    dir1 = Directory("dir")
    dir1.create("directory1", "")
    composite.addSystemComponent(dir1)
    bufferF1 = BufferFile("buffer")
    bufferF1.create("buffer1", dir1.path)
    dir1.addSystemComponent(bufferF1)
    bufferF1.push("hi")
    assert bufferF1.consume() == "hi"
