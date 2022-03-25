const { contextBridge, ipcRenderer } = require('electron')
contextBridge.exposeInMainWorld(
    "mia_electron_api",
    {
        sendsample:(data)=>ipcRenderer.invoke("sendsample",data),
        onSample:(callback)=>ipcRenderer.on("onSample",(event,argv)=>callback(event,argv))
    }
)