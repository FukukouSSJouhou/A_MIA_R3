import TENSORPYTHONPROCINTERFACE from "./tensorpythonproc_interface";

process.on("message",(message:TENSORPYTHONPROCINTERFACE)=>{
    let base64target=message.base64target;
    let filename=message.filename;
    let perframe=message.frameper;
    
});