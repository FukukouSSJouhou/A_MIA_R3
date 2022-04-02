import pynode from '@fukukoussjouhou/pynode';
import path from "path";

import {Worker} from "worker_threads"
class A_MIA_R3_PythonWraps{
    pyinstance:any;
    pyclasskun:any;
    loggerobj=(strkun:string)=>{
        console.log(strkun);
    }
    constructor(){
        this.pyclasskun=pynode.pyimport("A_MIA_R3_Core.nodewrap.A_MIR_R3_node")
        this.pyinstance=this.pyclasskun.get("A_MIR_R3_node2").call(this.loggerobj);
    }
    public setFilename(filename:string):string{
        return this.pyinstance.get("setFilename").call(filename);
    }
    public run():number{
        return this.pyinstance.get("run").call();
    }
    public Setimagelistsendcallback(callback:(datakun:string)=>void):string{
        return this.pyinstance.get("Setimagelistsendcallback").call(callback);
    }
    public setselectimg(indexkun:number):void{
        this.pyinstance.get("recieve_selectimg").call(indexkun);
    }
}
export default A_MIA_R3_PythonWraps;