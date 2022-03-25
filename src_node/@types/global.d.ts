declare global{
    interface Window{
        mia_electron_api:IMIA_ELECTRON_API;
    }
}
export interface IMIA_ELECTRON_API{
    sendsample:(data:string) => void;
    onSample:(callback:(event:any,argv:any)=>void)=>()=>void;
}