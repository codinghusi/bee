import hive;


def execute(cmd):
    arg = cmd.split(" ");

    if(arg[0]=="install"):
        user="";
        package="";
        if(arg[1]=="-u"):
            user=arg[2];
            package=arg[3];
        else:
            package=arg[1];

        code = hive.install(user,package);
        if(code==404):
            print("[Error] package not found!");