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
    public async setFilename(filename:string):Promise<string>{
        return this.pyinstance.get("setFilename").call(filename);
    }
    public run():number{
        return this.pyinstance.get("run").call();
    }
    public async Setimagelistsendcallback(callback:(datakun:string)=>void):Promise<string>{
        return this.pyinstance.get("Setimagelistsendcallback").call(callback);
    }
    public async setselectimg(indexkun:number):Promise<void>{
        this.pyinstance.get("recieve_selectimg").call(indexkun);
    }
}
export default A_MIA_R3_PythonWraps;