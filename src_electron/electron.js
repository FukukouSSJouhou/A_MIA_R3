const electron = require("electron");
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;
const path = require("path");
const isDev = require("electron-is-dev");
const { ipcMain } = require("electron");
let mainWindow;
function createWindow() {
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
    setInterval(()=>{
        const date = new Date();
        const currentTime = formattedDateTime(date);
        mainWindow.webContents.send("onSample",currentTime)
        function formattedDateTime(date) {
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
        isDev
            ? "http://localhost:3000"
            : `file://${path.join(__dirname, "../build/index.html")}`
    );
    mainWindow.on("closed", () => (mainWindow = null));

}
app.on("ready", createWindow);
app.on("window-all-closed", () => {
    if (process.platform !== "darwin") {
        app.quit();
    }
});
app.on("activate", () => {
    if (mainWindow === null) {
        createWindow();
    }
})