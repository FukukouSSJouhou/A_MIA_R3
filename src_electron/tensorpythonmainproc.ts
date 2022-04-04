import path from "path";
import {Worker} from "worker_threads";
import * as childProcess from "child_process";
export default class TensorPythonMainProc {

    //childworker:childProcess.ChildProcess=new childProcess.
    //Worker(path.join(__dirname,"tensorpythonchildproc"));
    constructor() {
        
        /*this.childworker.on("message", (message:string) => {
                console.log("graph base64");
                console.log(message);
        });*/
    }
    public start(base64target:string,filename:string,frameper:number){
        let senddtobject={
            base64target:base64target,
            filename:filename,
            frameper:frameper
        }
        //this.childworker.postMessage(senddtobject);
        const childproc=childProcess.spawn("node",[path.join(__dirname,"tensorpythonchildproc.js"),JSON.stringify(senddtobject)]);
        console.log('process id:' + process.pid)
        console.log('child process id:' + childproc.pid)
        childproc.stderr.setEncoding('utf8');
        childproc.stdout.setEncoding('utf8');
        childproc.stdout.on("data",(chunk)=>{
            console.log(chunk);
        });
        childproc.stderr.on("data",(chunk)=>{
            console.error(chunk);
        });
    }
}