import pynode from '@fukukoussjouhou/pynode';
import IimageCVSelector from './IimageCVSelector';
class A_MIA_R3_PythonWraps implements IimageCVSelector{
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
    public getselectedimg(indexkun:number):string{
        let result_valuekun:string= this.pyinstance.get("getselectedimg").call(indexkun);
        this.pyinstance.get("closeObj").call();
        return result_valuekun;
    }
}
export default A_MIA_R3_PythonWraps;