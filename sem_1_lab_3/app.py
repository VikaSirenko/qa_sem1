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
        return "Created directory: %s" % dir.path , 201
    except:
        return "Can not create directory", 400


@app.route('/createbinary', methods=['POST'])
def createBinary():
    try:
        content = request.json
        binary=BinaryFile("binary")
        binary.create(content['name'], content['path'], content['context'])
        composite.addSystemComponent(binary)
        return "Created binary file: %s" % binary.path, 201
    except:
        return "Can not create binary file", 400


@app.route('/createlog', methods=['POST'])
def createLog():
    try:
        content = request.json
        log=LogTextFile("log")
        log.create(content['name'], content['path'], content['context'])
        composite.addSystemComponent(log)
        return "Created log file: %s" % log.path, 201
    except:
        return "Can not create log text file", 400


@app.route('/createbuffer', methods=['POST'])
def createBuffer():
    try:
        content = request.json
        buffer=BufferFile("buff")
        buffer.create(content['name'], content['path'])
        composite.addSystemComponent(buffer)
        return "Created buffer file: %s" % buffer.path, 201
    except:
        return "Can not create buffer file", 400


@app.route('/moveNode' , methods=['PUT'])
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
            return "Moved: %s" % path, 200
        else:
            return "cannot find dir or file to move", 404
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
            return string_list, 200
        else:
            return("cannot find directory"), 404
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
            return context, 200
        else:
            return("cannot find binary file"), 404
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
            return context, 200
        else:
            return ("cannot find log file"), 404
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
            return str(context_len), 200
        else:
            return("cannot find log file"), 404
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
            return("cannot find buffer file"), 404
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
            return("cannot find buffer file"), 404
    except:
        return "Can not consume from buffer file", 400


@app.route('/deletedir' , methods=['DELETE'])
def deletedir():
    try:
        content = request.json
        path=content['path']
        parts= path.split("/")
        component=composite.findComponent(parts[len(parts)-2])
        if(parts[len(parts)-3]==""):
            if(component.path == path):
                composite.removeFileSystemComponent(component) 
                return "Deleted", 200
            else:
                return("cannot find dir to delete"), 404
            
        else:
            root=composite.findComponent(parts[len(parts)-3]) 
            if(component.path == path):
                root.delete(component, composite)
                return "Deleted from: %s" % root.path , 200
            else:
                return("cannot find dir to delete"), 404
    except:
        return "Can not delete", 400


@app.route('/deletebinary' , methods=['DELETE'])
def deleteBinary():
    try:
        content = request.json
        path=content['path']
        parts= path.split("/")
        component=composite.findComponent(parts[len(parts)-2]) 
        if(parts[len(parts)-3]==""):
            if(component.path == path):
                composite.removeFileSystemComponent(component) 
                return "Deleted ", 200
            else:
                return("cannot find binary file to delete"), 404
            
        else:
            root=composite.findComponent(parts[len(parts)-3]) 
            if(component.path == path):
                root.delete(component, composite)
                return "Deleted from: %s" % root.path, 200
            else:
                return("cannot find binary file to delete"), 404
    except:
        return "Can not delete", 400

@app.route('/deletelog' , methods=['DELETE'])
def deleteLog():
    try:
        content = request.json
        path=content['path']
        parts= path.split("/")
        component=composite.findComponent(parts[len(parts)-2]) 
        if(parts[len(parts)-3]==""):
            if(component.path == path):
                composite.removeFileSystemComponent(component) 
                return "Deleted ", 200
            else:
                return("cannot find log text file to delete"), 404
            
        else:
            root=composite.findComponent(parts[len(parts)-3]) 
            if(component.path == path):
                root.delete(component, composite)
                return "Deleted from: %s" % root.path, 200
            else:
                return("cannot find log text file to delete"), 404
    except:
        return "Can not delete", 400



@app.route('/deletebuffer' , methods=['DELETE'])
def deleteBuffer():
    try:
        content = request.json
        path=content['path']
        parts= path.split("/")
        component=composite.findComponent(parts[len(parts)-2]) 
        if(parts[len(parts)-3]==""):
            if(component.path == path):
                composite.removeFileSystemComponent(component) 
                return "Deleted ", 200
            else:
                return("cannot find buffer file to delete"), 404
            
        else:
            root=composite.findComponent(parts[len(parts)-3]) 
            if(component.path == path):
                root.delete(component, composite)
                return "Deleted from: %s" % root.path, 200
            else:
                return("cannot find buffer file to delete"), 404
    except:
        return "Can not delete", 400




if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

