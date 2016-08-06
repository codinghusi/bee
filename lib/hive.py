import urllib.request;
import zipfile,sys;
try:
    import cStringIO as StringIO;
except ImportError:
    try:
        import StringIO;
    except ImportError:
        import io as StringIO;


#HelpFunctions
def unzipStr(string):
    strFile = StringIO.StringIO(string);
    if(not zipfile.is_zipfile(strFile)):
        strFile.close();
        return string;
    zippedFile = zipfile.ZipFile(strFile,"r");
    unzipped = zipFile.read();
    zipFile.close();
    strFile.close();
    return unzipped;

def zipStr(string):
    strFile = StringIO.StringIO();
    if(zipfile.is_zipfile(strFile)):
        strFile.close();
        return string;
    zipFile = zipfile.ZipFile(strFile,"w");
    zipFile.writestr(zipFile,string);
    unzipped = strFile.output();
    zipFile.close();
    strFile.close();
    return unzipped;


def http_get(url):
    try:
        req=urllib.request.urlopen(url).read().decode();
    except:
        req="Error";
    return req;


#Error Functions
def installerGetErrorCode(error):
    if(type(error) is tuple):
        return "[Error]"+str(error[0].__name__)+": "+str(error[1]);
    if(error==0):
        return "WorkerBee successfully installed!";
    elif(error==1):
        return "WorkerBee not found!";
    elif(error==2):
        return "WorkerBee isn't a valid file";
    elif(error==3):
        return "Is not an ext of a WorkerBee";
    else:
        return "Unknown Error";





def install(workerName,user="Husi012"):
    try:
        if(workerName[-4:]!=".wkb"):
            return 3;
        url="https://raw.githubusercontent.com/"+user+"/bee/master/workers/"+workerName;
        
        workerBee=http_get(url);
        if(workerBee=="Error"):
            return 1; #File not Found

        workerBee = zipStr(workerBee);
        workerBee = unzipStr(workerBee);
        header = workerBee;
        
        if(header[:10]!="#StartHead"):
            return 2; #Not a valid worker bee
        header = header[10:header.index("#EndHead")];
        print("Header:\n",header);
        
    except:
        return sys.exc_info();#Fatal Error while installing worker bee
    return 0;


err = install("testfile.wkb");
print(installerGetErrorCode(err));
    
