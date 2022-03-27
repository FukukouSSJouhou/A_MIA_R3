import { contextBridge, ipcRenderer } from 'electron';
contextBridge.exposeInMainWorld(
    "mia_electron_api",
    {
        sendsample:(data:string)=>ipcRenderer.invoke("sendsample",data),
        onSample:(callback:any)=>ipcRenderer.on("onSample",(event,argv)=>callback(event,argv)),
        openVideoFileDialog:async(title:string)=>await ipcRenderer.invoke("openVideoFileDialog",title)
    }
)