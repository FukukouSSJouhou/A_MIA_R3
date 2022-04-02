import pynode from '@fukukoussjouhou/pynode';
class A_MIA_R3_PythonWraps{
    pyinstance:any;
    pyclasskun:any;
    filename:string;
    imagelistsendcallback:(datakun:string)=>void;

    loggerobj=(strkun:string)=>{
        console.log(strkun);
    }
    constructor(){
        pynode.openFile("A_MIA_R3_Core.nodewrap.A_MIR_R3_node")
        this.pyclasskun=pynode.pyimport("A_MIA_R3_Core.nodewrap.A_MIR_R3_node")
        this.pyinstance=this.pyclasskun.get("A_MIR_R3_node2").call(this.loggerobj);
        this.filename="";
        this.imagelistsendcallback=(testvar)=>{
            return
        };
    }
    public async setFilename(filename:string):Promise<string>{
        //return this.pyinstance.get("setFilename").call(filename);
        this.filename=filename;
        return "b"
    }
    public async run():Promise<number>{
        //return this.pyinstance.get("run").call();
        //let objkun22=this.pyinstance.get("get_objkun").call();
        return new Promise((resolve,reject)=>{
            pynode.call("run_super","tdn",(err:any,results:number)=>{
                if(err)reject(err);
                else resolve(results);
            });
        });
    }
    public async Setimagelistsendcallback(callback:(datakun:string)=>void):Promise<string>{
        //return this.pyinstance.get("Setimagelistsendcallback").call(callback);
        this.imagelistsendcallback=callback;
        return "a";
    }
    public async setselectimg(indexkun:number):Promise<void>{
        //this.pyinstance.get("recieve_selectimg").call(indexkun);
        return new Promise((resolve,reject)=>{
            pynode.call("recieve_selectimg",indexkun,(err:any,results:number)=>{
                if(err)reject(err);
                else resolve();
            });
        });
    }
    public async get_objkun():Promise<any>{
        return this.pyinstance.get("get_objkun").call();
    }

}
export default A_MIA_R3_PythonWraps;