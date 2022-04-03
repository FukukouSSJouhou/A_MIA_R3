declare global{
    interface Window{
        mia_electron_api:IMIA_ELECTRON_API;
    }
}
export interface IMIA_ELECTRON_API{
    sendsample:(data:string) => void;
    onSample:(callback:(event:any,argv:any)=>void)=>()=>void;
    openVideoFileDialog:(title:string)=>Promise<IOPENVDIALOG_STATUS>;
    pathExistsAsync:(filename:string)=>Promise<boolean>;
    fileExistsAsync:(filename:string)=>Promise<boolean>;
    set_filename:(filename:string)=>Promise<string>;
    Setimagelistsendcallback:(callback:(datakun:string)=>void)=>void;
    setselectimg:(indexkun:number)=>Promise<void>;
    run:()=>Promise<void>;
    getNextImageBase64:()=>Promise<string>;
    create_syoriobj:()=>Promise<void>;
}
export interface IOPENVDIALOG_STATUS{
    status?:Boolean;
    path:string;
}