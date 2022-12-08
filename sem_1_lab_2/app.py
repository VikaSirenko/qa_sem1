from flask import Flask, request
from file_system import *


app = Flask(__name__)


composite = Composite("file_system")

@app.route('/createdir', methods=['POST'])
def createDir():
    try:
        content = request.json
        dir=Directory("dir")
        dir.create(content['name'], content['path'])
        composite.addSystemComponent(dir)
        return "Created: %s" % dir.path
    except:
        return "Can not create", 400


@app.route('/createbinary', methods=['POST'])
def createBinary():
    try:
        content = request.json
        binary=BinaryFile("binary")
        binary.create(content['name'], content['path'], content['context'])
        composite.addSystemComponent(binary)
        return "Created: %s" % binary.path
    except:
        return "Can not create", 400


@app.route('/createlog', methods=['POST'])
def createLog():
    try:
        content = request.json
        log=LogTextFile("log")
        log.create(content['name'], content['path'], content['context'])
        composite.addSystemComponent(log)
        return "Created: %s" % log.path
    except:
        return "Can not create", 400


@app.route('/createbuffer', methods=['POST'])
def createBuffer():
    try:
        content = request.json
        buffer=BufferFile("buff")
        buffer.create(content['name'], content['path'])
        composite.addSystemComponent(buffer)
        return "Created: %s" % buffer.path
    except:
        return "Can not create", 400


@app.route('/movedir' , methods=['PUT'])
def movesubdir():
    try:
        content = request.json
        old_path=content['old']
        new_path=content['new']
        old_parts= old_path.split("/")
        component=composite.findComponent(old_parts[len(old_parts)-2]) 
        old_root=composite.findComponent(old_parts[len(old_parts)-3]) 
        if(component.path == old_path):
            path= old_root.move(new_path,component,composite)
            return "Moved: %s" % path
        else:
            raise Exception("cannot find dir to move")
    except:
        return "Can not move", 400


@app.route('/movebinary' , methods=['PUT'])
def movebinary():
    try:
        content = request.json
        old_path=content['old']
        new_path=content['new']
        old_parts= old_path.split("/")
        component=composite.findComponent(old_parts[len(old_parts)-2]) 
        old_root=composite.findComponent(old_parts[len(old_parts)-3]) 
        if(component.path == old_path):
            path= component.move(new_path,composite, old_root)
            return "Moved: %s" % path
        else:
            raise Exception("cannot binary file to move")
    except:
        return "Can not move", 400



@app.route('/movelog' , methods=['PUT'])
def movelog():
    try:
        content = request.json
        old_path=content['old']
        new_path=content['new']
        old_parts= old_path.split("/")
        component=composite.findComponent(old_parts[len(old_parts)-2]) 
        old_root=composite.findComponent(old_parts[len(old_parts)-3]) 
        if(component.path == old_path):
            path= component.move(new_path,composite, old_root)
            return "Moved: %s" % path
        else:
            raise Exception("cannot find log text file to move")
    except:
        return "Can not move", 400


@app.route('/movebuffer' , methods=['PUT'])
def movebuffer():
    try:
        content = request.json
        old_path=content['old']
        new_path=content['new']
        old_parts= old_path.split("/")
        component=composite.findComponent(old_parts[len(old_parts)-2]) 
        old_root=composite.findComponent(old_parts[len(old_parts)-3]) 
        if(component.path == old_path):
            path= component.move(new_path,composite, old_root)
            return "Moved: %s" % path
        else:
            raise Exception("cannot find buffer file to move")
    except:
        return "Can not move", 400


@app.route('/getlist' , methods=['GET'])
def getListOfDir():
    try:
        content = request.json
        path=content['path']
        old_parts= path.split("/")
        component=composite.findComponent(old_parts[len(old_parts)-2])  
        if(component.path == path):
            list= component.getListOfComponents()
            string_list=""
            for file in list:
                string_list+=file.name+", "
            return string_list
        else:
            raise Exception("cannot find directory")
    except:
        return "Can not get list of directory` components", 400



@app.route('/readBinary' , methods=['GET'])
def readBinary():
    try:
        content = request.json
        path=content['path']
        old_parts= path.split("/")
        component=composite.findComponent(old_parts[len(old_parts)-2])  
        if(component.path == path):
            context = component.readFile()
            return context
        else:
            raise Exception("cannot find binary file")
    except:
        return "Can not read binary file", 400




@app.route('/readLog' , methods=['GET'])
def readLog():
    try:
        content = request.json
        path=content['path']
        old_parts= path.split("/")
        component=composite.findComponent(old_parts[len(old_parts)-2])  
        if(component.path == path):
            context = component.readFile()
            return context
        else:
            raise Exception("cannot find log file")
    except:
        return "Can not read log file", 400


@app.route('/appendLog' , methods=['PUT'])
def appendLog():
    try:
        content = request.json
        path=content['path']
        old_parts= path.split("/")
        component=composite.findComponent(old_parts[len(old_parts)-2])  
        line=content['line']
        if(component.path == path):
            context_len = component.addLine(line)
            return str(context_len)
        else:
            raise Exception("cannot find log file")
    except:
        return "Can not add line to log file", 400


@app.route('/pushBuffer' , methods=['PUT'])
def pushBuffer():
    try:
        content = request.json
        path=content['path']
        old_parts= path.split("/")
        component=composite.findComponent(old_parts[len(old_parts)-2])  
        push_line=content['push']
        if(component.path == path):
            context_len = component.push(push_line)
            return str(context_len)
        else:
            raise Exception("cannot find buffer file")
    except:
        return "Can not push to buffer file", 400


@app.route('/consumeBuffer' , methods=['GET'])
def consumeBuffer():
    try:
        content = request.json
        path=content['path']
        old_parts= path.split("/")
        component=composite.findComponent(old_parts[len(old_parts)-2])  
        if(component.path == path):
            consume_el= component.consume()
            return consume_el
        else:
            raise Exception("cannot find buffer file")
    except:
        return "Can not consume from buffer file", 400


if __name__ == '__main__':
    app.run(debug=True)

