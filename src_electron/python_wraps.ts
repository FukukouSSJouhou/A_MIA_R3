import pynode from '@fukukoussjouhou/pynode';
class A_MIA_R3_PythonWraps{
    pyinstance:any;
    pyclasskun:any;
    loggerobj=(strkun:string)=>{
        console.log(strkun);
    }
    constructor(){
        this.pyclasskun=pynode.pyimport("A_MIA_R3_Core.nodewrap.A_MIR_R3_nodev2")
        this.pyinstance=this.pyclasskun.get("A_MIR_R3_node2").call(this.loggerobj);
    }
    public async setFilename(filename:string):Promise<string>{
        return this.pyinstance.get("setFilename").call(filename);
    }
    public async run():Promise<number>{
        return this.pyinstance.get("run").call();
    }
    public async Setimagelistsendcallback(callback:(datakun:string)=>void):Promise<void>{
        //this.pyinstance.get("Setimagelistsendcallback").call(callback);
    }
    public async setselectimg(indexkun:number):Promise<void>{
        //this.pyinstance.get("recieve_selectimg").call(indexkun);
        this.pyinstance.get("setselectimg").call(indexkun);
    }
    public getNextImageBase64():string{
        return this.pyinstance.get("getNextImageBase64").call();
    }
    public async create_syoriobj():Promise<void>{
        return this.pyinstance.get("create_syoriobj").call();
    }
}
export default A_MIA_R3_PythonWraps;