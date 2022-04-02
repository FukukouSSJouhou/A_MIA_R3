import { contextBridge, ipcRenderer, IpcRendererEvent } from 'electron';
contextBridge.exposeInMainWorld(
    "mia_electron_api",
    {
        sendsample: (data: string) => ipcRenderer.invoke("sendsample", data),
        onSample: (callback: any) => ipcRenderer.on("onSample", (event, argv) => callback(event, argv)),
        openVideoFileDialog: async (title: string) => await ipcRenderer.invoke("openVideoFileDialog", title),
        pathExistsAsync: async (filename: string): Promise<boolean> =>
            await ipcRenderer.invoke("pathExistsAsync", filename),
        fileExistsAsync: async (filename: string): Promise<boolean> =>
            await ipcRenderer.invoke("fileExistsAsync", filename),
        onSetimagelistRecieved: (callback: (datakun: string) => void) => {
            console.log()
            ipcRenderer.on("onSetimagelistRecieved", (event: IpcRendererEvent, datakun22: string) => {
                callback(JSON.stringify(datakun22))
            });
            return () => {
                ipcRenderer.removeAllListeners("onSetimagelistRecieved");
            };
        }
    }
)