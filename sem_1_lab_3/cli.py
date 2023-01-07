import click
from flask.cli import with_appcontext
import requests
from flask import Flask, request


app = Flask(__name__)


@click.group()
def cli():
    pass


@click.command(name="createBin")
@click.argument('name')
@click.argument('path')
@click.argument('context')
@with_appcontext
def createBin(name, path, context):
    create_data = {
        "name": f"{name}",
        "path": f"{path}",
        "context": f"{context}"
    }

    response = requests.post(
        'http://127.0.0.1:5000/createbinary', json=create_data)
    print(response.content)



@click.command(name="createDir")
@click.argument('name')
@click.argument('path')
def createDir(name, path):
    create_data = {
        "name": f"{name}",
        "path": f"{path}"
    }
    response = requests.post(
        'http://127.0.0.1:5000/createdir', json=create_data)
    print(response.content)



@click.command(name="createLog")
@click.argument('name')
@click.argument('path')
@click.argument('context')
def createLog(name, path, context):
    text = context.split(",")
    create_data = {
        "name": f"{name}",
        "path": f"{path}",
        "context": text
    }
    response = requests.post(
        'http://127.0.0.1:5000/createlog', json=create_data)
    print(response.content)


@click.command(name="createBuff")
@click.argument('name')
@click.argument('path')
def createBuff(name, path):
    create_data = {
        "name": f"{name}",
        "path": f"{path}"
    }
    response = requests.post(
        'http://127.0.0.1:5000/createbuffer', json=create_data)
    print(response.content)


@click.command(name="getDirList")
@click.argument('path')
def getDirList(path):
    get_data = {
        "path": f"{path}"
    }
    response = requests.get('http://127.0.0.1:5000/getlist', json=get_data)
    print(response.content)


@click.command(name="readBin")
@click.argument('path')
def readBin(path):
    get_data = {
        "path": f"{path}"
    }
    response = requests.get('http://127.0.0.1:5000/readBinary', json=get_data)
    print(response.content)


@click.command(name="readLog")
@click.argument('path')
def readLog(path):
    get_data = {
        "path": f"{path}"
    }
    response = requests.get('http://127.0.0.1:5000/readLog', json=get_data)
    print(response.content)


@click.command(name="appendLog")
@click.argument('path')
@click.argument("line")
def appendLog(path, line):
    put_data = {
        "path": f"{path}",
        "line": f"{line}"
    }
    response = requests.put('http://127.0.0.1:5000/appendLog', json=put_data)
    print(response.content)


@click.command(name="pushBuff")
@click.argument('path')
@click.argument("push")
def pushBuff(path, push):
    put_data = {
        "path": f"{path}",
        "push": f"{push}"
    }
    response = requests.put('http://127.0.0.1:5000/pushBuffer', json=put_data)
    print(response.content)


@click.command(name="consumeBuff")
@click.argument('path')
def consumeBuff(path):
    get_data = {
        "path": f"{path}"
    }
    response = requests.get(
        'http://127.0.0.1:5000/consumeBuffer', json=get_data)
    print(response.content)


@click.command(name="moveDir")
@click.argument('old')
@click.argument('new')
def moveDir(old, new):
    put_data = {
        "old": f"{old}",
        "new": f"{new}"
    }
    response = requests.put('http://127.0.0.1:5000/moveNode', json=put_data)
    print(response.content)


@click.command(name="moveLog")
@click.argument('old')
@click.argument('new')
def moveLog(old, new):
    put_data = {
        "old": f"{old}",
        "new": f"{new}"
    }
    response = requests.put('http://127.0.0.1:5000/moveNode', json=put_data)
    print(response.content)


@click.command(name="moveBuff")
@click.argument('old')
@click.argument('new')
def moveBuff(old, new):
    put_data = {
        "old": f"{old}",
        "new": f"{new}"
    }
    response = requests.put('http://127.0.0.1:5000/moveNode', json=put_data)
    print(response.content)


@click.command(name="moveBin")
@click.argument('old')
@click.argument('new')
def moveBin(old, new):
    put_data = {
        "old": f"{old}",
        "new": f"{new}"
    }
    response = requests.put('http://127.0.0.1:5000/moveNode', json=put_data)
    print(response.content)


@click.command(name="deleteLog")
@click.argument('path')
def deleteLog(path):
    delete_data = {
        "path": f"{path}"
    }
    response = requests.delete(
        'http://127.0.0.1:5000/deletelog', json=delete_data)
    print(response.content)


@click.command(name="deleteBin")
@click.argument('path')
def deleteBin(path):
    delete_data = {
        "path": f"{path}"
    }
    response = requests.delete(
        'http://127.0.0.1:5000/deletebinary', json=delete_data)
    print(response.content)


@click.command(name="deleteDir")
@click.argument('path')
def deleteDir(path):
    delete_data = {
        "path": f"{path}"
    }
    response = requests.delete(
        'http://127.0.0.1:5000/deletedir', json=delete_data)
    print(response.content)


@click.command(name="deleteBuff")
@click.argument('path')
def deleteBuff(path):
    delete_data = {
        "path": f"{path}"
    }
    response = requests.delete(
        'http://127.0.0.1:5000//deletebuffer', json=delete_data)
    print(response.content)


cli.add_command(createDir)
cli.add_command(deleteDir)
cli.add_command(moveDir)
cli.add_command(getDirList)

cli.add_command(createBin)
cli.add_command(deleteBin)
cli.add_command(moveBin)
cli.add_command(readBin)

cli.add_command(createLog)
cli.add_command(deleteLog)
cli.add_command(moveLog)
cli.add_command(readLog)
cli.add_command(appendLog)

cli.add_command(createBuff)
cli.add_command(deleteBuff)
cli.add_command(moveBuff)
cli.add_command(pushBuff)
cli.add_command(consumeBuff)


if __name__ == '__main__':
    cli()
