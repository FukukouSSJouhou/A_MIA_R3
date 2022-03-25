import { Button } from '@mui/material';
import React, * as react from 'react';
export default function IndexPage():React.ReactElement{
    const [textdata,settextdata]=React.useState<string>(null!);
    React.useEffect(()=>{
        function onRecievedkun(event:any,args:any){
            settextdata(args);
        }
        window.mia_electron_api.onSample(
            onRecievedkun
        )
    },[]);
    const button_clicked=()=>{
        console.log("tintin")
        window.mia_electron_api.sendsample("tintin");
    }
    return(
        <>
            <h1>Hello World</h1>
            {textdata}
            <Button onClick={button_clicked}>
                tintin
            </Button>
        </>
    );
}