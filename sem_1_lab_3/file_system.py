
class Composite(object):

    __fileSystemcomponents = []
    _nodes = []
    type = ""
    name = ""
    path = ""

    def __init__(self, type):
        self.type = type
        self._nodes = []

    def addSystemComponent(self, component):
        self._nodes.append(component)
        parts = component.path.split("/")
        if(parts[0]==component.name):
            self.__fileSystemcomponents.append(component)
        else:
            root = self.findComponent(parts[len(parts)-3])
            if root.path+component.name+"/" == component.path:
                root.addSystemComponent(component)
            else:
                raise Exception("Can not add")

    def removeFileSystemComponent(self, component):
        self.__fileSystemcomponents.remove(component)
        if(component.type=="dir"):
            parts= component.getListOfComponents()
            for p in parts:
                self.delete(p)
        self.delete(component)
    
    def delete(self, component):
        self._nodes.remove(component)

    def findComponent(self, name):
        for component in self._nodes:
            if component.name == name:
                return component

    def getListOfComponents(self):
        for component in self.__fileSystemcomponents:
            returnComponents = component.getListOfComponents()
            for file in returnComponents:
                self._nodes.append(file)
            self._nodes.append(component)
        return self._nodes


class Directory(object):

    _nodes = []
    type = ""
    name = ""
    path = ""
    max_num = 5

    def __init__(self, type):
        self.type = type
        self._nodes = []

    def create(self, name, path):
        self.name = name
        self.path = path+name+"/"
        return self.path

    def move(self, new_path, component, composite):
        parts = new_path.split("/")
        newRoot = composite.findComponent(parts[len(parts)-2])
        if newRoot.path == new_path:
            newRoot.addSystemComponent(component)
            self._nodes.remove(component)
            component.path = newRoot.path+component.name+"/"
            return (component.path)
        else:
            raise Exception("can not move")

    def addSystemComponent(self, component):
        if (len(self._nodes) >= self.max_num):
            raise Exception ("can not add")

        self._nodes.append(component)

    def removeFileSystemComponent(self, composite):
        parts = self.path.split("/")
        root = composite.findComponent(parts[len(parts)-3])
        root._nodes.remove(self)

    def findComponent(self, name):
        for component in self._nodes:
            if component.name == name:
                return component

    def getListOfComponents(self):
        return self._nodes

    def delete(self, component, composite):
        try:
            self._nodes.remove(component)
            composite.delete(component)
            return ("deleted")
        except:
            raise Exception("can not delete")


class BinaryFile(object):

    __context = ""
    _nodes = []
    type = ""
    name = ""
    path = ""

    def __init__(self, type):
        self.type = type
        self._nodes = []

    def create(self, name, path, context):
        self.name = name
        self.path = path+name+"/"
        self.__context = context

    def addSystemComponent(self, component):
        raise Exception("operation is not possible")

    def move(self, new_path, composite, root):
        parts = new_path.split("/")
        newRoot = composite.findComponent(parts[len(parts)-2])
        if newRoot.path == new_path:
            # component = composite.findComponent(self.name)
            newRoot.addSystemComponent(self)
            root.delete(self)
            self.path = newRoot.path+self.name+"/"
            return (self.path)
        else:
            raise Exception("can not move")

    def getListOfComponents(self):
        raise Exception("operation is not possible")

    def findComponent(self, name):
        raise Exception("operation is not possible")

    def readFile(self):
        return self.__context


class LogTextFile(object):

    __context = []

    _nodes = []
    type = ""
    name = ""
    path = ""

    def __init__(self, type):
        self.type = type
        self._nodes = []

    def create(self, name, path, context):
        self.name = name
        self.path = path+name+"/"
        self.__context = context

    def addSystemComponent(self, component):
        raise Exception("operation is not possible")

    def move(self, new_path, composite, root):
        parts = new_path.split("/")
        newRoot = composite.findComponent(parts[len(parts)-2])
        if newRoot.path == new_path:
            # component = composite.findComponent(self.name)
            newRoot.addSystemComponent(self)
            root.delete(self)
            self.path = newRoot.path+self.name+"/"
            return (self.path)
        else:
            raise Exception("can not move")

    def getListOfComponents(self):
        raise Exception("operation is not possible")

    def findComponent(self, name):
        raise Exception("operation is not possible")

    def readFile(self):
        contextOfFile = ""
        for line in self.__context:
            contextOfFile += line+"\n"
        return contextOfFile

    def addLine(self, newLine):
        self.__context.append(newLine)
        return len(self.__context)


class BufferFile(object):

    __context = []

    _nodes = []
    type = ""
    name = ""
    path = ""
    max_num = 5

    def __init__(self, type):
        self.type = type
        self._nodes = []

    def create(self, name, path):
        self.name = name
        self.path = path+name+"/"

    def addSystemComponent(self, component):
        raise Exception("operation is not possible")

    def move(self, new_path, composite, root):
        parts = new_path.split("/")
        newRoot = composite.findComponent(parts[len(parts)-2])
        if newRoot.path == new_path:
            # component = composite.findComponent(self.name)
            newRoot.addSystemComponent(self)
            root.delete(self)
            print(newRoot.path)
            self.path = newRoot.path+self.name+"/"
            return (self.path)
        else:
            return ("can not move")

    def getListOfComponents(self):
        raise Exception("operation is not possible")

    def findComponent(self, name):
        raise Exception("operation is not possible")

    def readFile(self):
        contextOfFile = ""
        for line in self.__context:
            contextOfFile += line+"\n"
        return contextOfFile

    def push(self, newLine):
        if (len(self.__context) >= self.max_num):
            raise ("can not add new data")

        self.__context.append(newLine)
        return len(self.__context)

    def consume(self):
        try:
            consumeEl = self.__context[0]
            self.__context.pop(0)
            return consumeEl
        except:
            return Exception("buffer file is empty") , 204



