import { contextBridge, ipcRenderer, IpcRendererEvent } from 'electron';
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
            await ipcRenderer.invoke("set_filename",filename),
        setselectimg:async(indexkun:number):Promise<void>=>
            await ipcRenderer.invoke("setselectimg",indexkun),
        run:async():Promise<number>=>
            await ipcRenderer.invoke("run"),
        onSetimagelistRecieved:(callback:(datakun:string)=>void)=>
            ipcRenderer.on("onSetimagelistRecieved",(event,datakun22)=>callback(datakun22))
    }
)