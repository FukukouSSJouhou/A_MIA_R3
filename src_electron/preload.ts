import { contextBridge, ipcRenderer } from 'electron';
contextBridge.exposeInMainWorld(
    "mia_electron_api",
    {
        sendsample:(data:string)=>ipcRenderer.invoke("sendsample",data),
        onSample:(callback:any)=>ipcRenderer.on("onSample",(event,argv)=>callback(event,argv)),
        openVideoFileDialog:async(title:string)=>await ipcRenderer.invoke("openVideoFileDialog",title),
        pathExistsAsync:async(filename:string):Promise<boolean>=>
            await ipcRenderer.invoke("pathExistsAsync",filename),
        fileExistsAsync:async(filename:string):Promise<boolean>=>
            await ipcRenderer.invoke("fileExistsAsync",filename),
        set_filename:async(filename:string):Promise<string>=>
            await ipcRenderer.invoke("set_filename",filename)
    }
)