import path from "path";
import { ipcMain ,dialog,BrowserWindow,app, IpcMainInvokeEvent } from "electron";
import fs from "fs";
import pynode from '@fukukoussjouhou/pynode';
import A_MIA_R3_PythonWraps from "./python_wraps";

if (process.env.NODE_ENV === 'development') {
  const execPath:string =
    process.platform === 'win32'
      ? '../node_modules/electron/dist/electron.exe'
      : '../node_modules/.bin/electron';

  require('electron-reload')(__dirname, {
    electron: path.resolve(__dirname, execPath),
  });
}

let mainWindow:BrowserWindow;

pynode.startInterpreter();
pynode.appendSysPath('./');
pynode.appendSysPath('./venv/Lib/site-packages');
let classtest=new A_MIA_R3_PythonWraps();
const createWindow=()=> {
    mainWindow = new BrowserWindow(
        {
            width: 900, 
            height: 680,
            webPreferences:{
                nodeIntegration:false,
                contextIsolation:true,
                preload:path.join(__dirname,"preload.js")
            }
        }
    );
    ipcMain.handle("sendsample",(event,data)=>{
        console.log(data)
    })
    ipcMain.handle("openVideoFileDialog",async(event:IpcMainInvokeEvent,title:string)=>{
        const paths=dialog.showOpenDialogSync(mainWindow,
            {
                buttonLabel:"Open",
                filters:[
                        {name:"Video files",extensions:["mp4","mkv","avi","wmv","webm"]},
                        {name:"All files",extensions:["*"]}
                ],
                properties:[
                    "openFile"
                ]
            });
            if(paths===undefined)return({status:undefined,path:""});
            return({
                status:true,
                path:paths[0]
            })
    })
    ipcMain.handle("pathExistsAsync",async(event:IpcMainInvokeEvent,filename:string)=>{
        try{
            return !!(await fs.promises.lstat(filename));
        }catch(e){
            return false;
        }
    });
    ipcMain.handle("fileExistsAsync",async(event:IpcMainInvokeEvent,filename:string)=>{
        try{
            return (await fs.promises.lstat(filename)).isFile();
        }catch(e){
            return false;
        }
    });
    ipcMain.handle("set_filename",async(event:IpcMainInvokeEvent,filename:string)=>{
        return classtest.setFilename(filename);
    });
    ipcMain.handle("Setimagelistsendcallback",async(event:IpcMainInvokeEvent,callback:(datakun:string)=>void)=>{
        classtest.Setimagelistsendcallback(callback);
    });
    ipcMain.handle("setselectimg",async(event:IpcMainInvokeEvent,indexkun:number)=>{
        classtest.setselectimg(indexkun);
    });
    ipcMain.handle("run",async(event:IpcMainInvokeEvent)=>{
        classtest.run();
    });
    setInterval(()=>{
        const date = new Date();
        const currentTime = formattedDateTime(date);
        mainWindow.webContents.send("onSample",currentTime)
        function formattedDateTime(date:Date):string {
          const y = date.getFullYear();
          const m = ('0' + (date.getMonth() + 1)).slice(-2);
          const d = ('0' + date.getDate()).slice(-2);
          const h = ('0' + date.getHours()).slice(-2);
          const mi = ('0' + date.getMinutes()).slice(-2);
          const s = ('0' + date.getSeconds()).slice(-2);
        
          return y + m + d + h + mi + s;
        }
    },2000);
    mainWindow.loadURL(
        process.env.NODE_ENV === 'development'
            ? "http://localhost:3000"
            : `file://${path.join(__dirname, "../build/index.html")}`
    );

}
app.whenReady().then(createWindow);
app.once("window-all-closed",()=>app.quit());