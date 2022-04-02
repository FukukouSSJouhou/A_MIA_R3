import pynode from '@fukukoussjouhou/pynode';
import path from "path";

import {Worker} from "worker_threads"
const wait = async (ms:number) => new Promise(resolve => setTimeout(resolve, ms));
class A_MIA_R3_PythonWraps{
    pyinstance:any;
    pyclasskun:any;
    loggerobj=(strkun:string)=>{
        console.log(strkun);
    }
    currentindexkun:number;
    iscompletedkun:boolean;
    callback_setkun:(datakun:string)=>void;
    callback_setimagekun_other=(datakun:string):number=>{
        this.callback_setkun(datakun);
        while (true){
            wait(1000);
            if(this.iscompletedkun){
                return this.currentindexkun;
                break;
            }
        }
        return this.currentindexkun;
    }
    constructor(){
        this.pyclasskun=pynode.pyimport("A_MIA_R3_Core.nodewrap.A_MIR_R3_node")
        this.pyinstance=this.pyclasskun.get("A_MIR_R3_node2").call(this.loggerobj);
        this.callback_setkun=(datakun:string)=>{
        };
        this.currentindexkun=0;
        this.iscompletedkun=false;
    }
    public setFilename(filename:string):string{
        return this.pyinstance.get("setFilename").call(filename);
    }
    public run():number{
        console.log("called run");
        return this.pyinstance.get("run").call();
    }
    public Setimagelistsendcallback(callback:(datakun:string)=>void):string{
        //return this.pyinstance.get("Setimagelistsendcallback").call(callback);
        this.callback_setkun=callback;
        return this.SetimagelistsendandwaitCallback(this.callback_setimagekun_other);
    }
    public SetimagelistsendandwaitCallback(callback:(datakun:string)=>void):string{
        return this.pyinstance.get("SetimagelistsendandwaitCallback").call(callback);
    }
    public setselectimg(indexkun:number):void{
        /*console.log("called setselectimg");
        this.pyinstance.get("recieve_selectimg").call(indexkun);*/
        this.currentindexkun=indexkun;
        this.iscompletedkun=true;
    }
}
export default A_MIA_R3_PythonWraps;