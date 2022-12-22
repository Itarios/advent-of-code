class Santa_File:
    def __init__(self, name, size=0, type="file") -> None:
        self.name=name
        self.size=size
        self.type=type
    
    def __str__(self) -> str:
        return f'{self.name} ({self.type}, size= {self.size})'

class Santa_Directory(Santa_File):

    def __init__(self, name, parent) -> None:
        super().__init__(name,type="dir")
        self.parent=parent
        self.contents={}
    
    def __str__(self) -> str:
        # drop_down='\n\t'.join([str(file) for file in self.contents.values()])
        # return (f'{self.name}({self.type}, size={self.size}):\n\t{drop_down}' )
        return (f'{self.name}({self.type}, size= {self.size}):' )


    def add_file(self,file):
        self.contents[file.name]=file
        self.size+=file.size
    
    def move_up(self):
        self.parent.size+=self.size
        # self.update_size_parent()
        return self.parent
    
    def update_size_parent(self):
        if(self.parent==None):
            return None
        self.parent.size+=self.size
        self.parent.update_size_parent()

    def print_directory(self,indentation=0):
        # tab="\t"
        tab="  "
        print( tab*indentation, str(self))
        indentation+=1
        for file in self.contents.values():
            if(file.type=="dir"):
                file.print_directory(indentation)
                continue
            print(tab*indentation,file)

if __name__ == "__main__":
    # f = open("input", "r")
    f = open("test", "r")

    ls="ls"
    cd="cd"
    # commands=[ls,cd]
    dir="dir"
    up=".."

    line=f.readline().split()
    root_directory=Santa_Directory(line[2],None)
    current_directory=root_directory
    result=0
    temp=0

    for line in f:
        info, *command , name=line.split()
        # print(info, command,name)
        
        if(info==dir):
            current_directory.add_file( Santa_Directory(name,current_directory) )
            continue
        if(info.isnumeric()):
            temp+=int(info)
            current_directory.add_file( Santa_File(name,int(info)) )
            continue
        if( cd in command ):
            if( name==up ):
                if(current_directory.size<100_000):
                    result+=current_directory.size
                current_directory=current_directory.move_up()
                # print(str(current_directory))
                continue
            current_directory=current_directory.contents[name]
        # if( ls in command ):
        #     print(str(current_directory))
    
    current_directory.update_size_parent()
    if(current_directory.size<100_000):
        result+=current_directory.size

    root_directory.print_directory()
    print(result)

    f.close()