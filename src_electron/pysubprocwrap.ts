import * as childProcess  from "child_process"
import path from "path";
import { processinterface } from "./processinterface";
export default class pysubprocwrap{
    childproc:childProcess.ChildProcess;
    constructor(){
        this.childproc=childProcess.fork(path.join(__dirname,"pythonsubprockun"));
    }
    public async setFilename(filename:string):Promise<string>{
        let sendobj:processinterface={
            command:1,
            data:filename
        }
        this.childproc.send(sendobj);
        return filename;
    }
    public async run():Promise<number>{
        let sendobj:processinterface={
            command:0,
            data:""
        }
        this.childproc.send(sendobj);
        return 0;
    }
    public async Setimagelistsendcallback(callback:(datakun:string)=>void):Promise<string>{
        //return this.pyinstance.get("Setimagelistsendcallback").call(callback);
        this.childproc.on("message",(msg:processinterface)=>{
            switch(msg.command){
                case 810:
                    callback(msg.data);
            }
        });
        return "";
    }
    public async setselectimg(indexkun:number):Promise<void>{
        //this.pyinstance.get("recieve_selectimg").call(indexkun);
        let sendobj:processinterface={
            command:2,
            data:indexkun
        }
        this.childproc.send(sendobj);

    }
}